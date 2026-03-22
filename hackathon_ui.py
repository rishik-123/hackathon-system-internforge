import tkinter as tk
from tkinter import messagebox
import time
import random
import mysql.connector

import camera_proctor
import hackathon_engine

start_time = None


# 🔹 Fetch Questions from Database
def get_random_questions():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rishik@12345",
            database="studentregister"
        )

        cursor = conn.cursor()

        # Fetch all questions
        cursor.execute("SELECT question FROM hackathon_questions")
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        # Convert [(q1,), (q2,)] → [q1, q2]
        questions = [row[0] for row in data]

        # Ensure at least 3 questions exist
        if len(questions) < 3:
            messagebox.showerror("Error", "Not enough questions in database")
            return []

        return random.sample(questions, 3)

    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return []


# 🔹 Start Hackathon UI
def start_hackathon(email):
    global start_time

    # 🔴 Start camera in background
    try:
        camera_proctor.start_camera_thread()
    except:
        messagebox.showerror("Error", "Camera not detected")
        return

    window = tk.Toplevel()
    window.title("Hackathon Round")
    window.geometry("650x550")

    questions = get_random_questions()

    # 🔴 If DB failed
    if not questions:
        camera_proctor.stop_camera()
        return

    entries = []
    y = 20

    # 🔹 Show Questions
    for q in questions:
        tk.Label(window, text=q, wraplength=550, justify="left").place(x=20, y=y)

        entry = tk.Entry(window, width=70)
        entry.place(x=20, y=y + 30)

        entries.append(entry)

        y += 80

    start_time = time.time()

    # 🔹 Submit Function
    def submit():
        answers = []

        # 🔴 Validate
        for entry in entries:
            ans = entry.get().strip()
            if ans == "":
                messagebox.showerror("Error", "All questions must be answered")
                return
            answers.append(ans)

        end_time = time.time()
        time_taken = end_time - start_time

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="rishik@12345",
                database="studentregister"
            )

            cursor = conn.cursor()

            # 🔹 Check attempt_done
            cursor.execute(
                "SELECT attempt_done FROM hackathon_answers WHERE student_email=%s LIMIT 1",
                (email,)
            )

            result = cursor.fetchone()

            # 🔴 Already attempted
            if result and result[0] == 1:
                messagebox.showwarning("Warning", "You already completed the hackathon")

                score, status = hackathon_engine.process_hackathon(
                    email, questions, answers
                )

                messagebox.showinfo(
                    "Result",
                    f"Score: {score}\nStatus: {status}"
                )

                cursor.close()
                conn.close()
                camera_proctor.stop_camera()
                window.destroy()
                return

            # 🔹 Insert answers
            for q, ans in zip(questions, answers):
                cursor.execute(
                    """INSERT INTO hackathon_answers
                    (student_email, question, answer, time_taken, attempt_done)
                    VALUES (%s, %s, %s, %s, %s)""",
                    (email, q, ans, time_taken, 1)
                )

            conn.commit()
            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror("Database Error", str(e))
            camera_proctor.stop_camera()
            return

        # 🔹 Evaluate using AI
        try:
            score, status = hackathon_engine.process_hackathon(
                email, questions, answers
            )

        except Exception as e:
            messagebox.showerror("Evaluation Error", str(e))
            camera_proctor.stop_camera()
            return

        # 🔹 Show Result
        messagebox.showinfo(
            "Hackathon Result",
            f"Your Score: {score}\nStatus: {status}"
        )

        # 🔴 Stop camera
        camera_proctor.stop_camera()

        window.destroy()

    # 🔹 Submit Button
    tk.Button(
        window,
        text="Submit",
        command=submit,
        bg="green",
        fg="white",
        width=15
    ).place(x=260, y=470)

    window.mainloop()