import tkinter as tk
from tkinter import messagebox
import time
import random
# import mysql.connector
# import camera_proctor
# import hackathon_engine

start_time = None

# 🔹 Fetch Questions from Database
def get_random_questions():
    # ------------------ Database logic commented for GUI test ------------------
    """
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rishik@12345",
            database="studentregister"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT question FROM hackathon_questions")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        questions = [row[0] for row in data]
        if len(questions) < 3:
            messagebox.showerror("Error", "Not enough questions in database")
            return []
        return random.sample(questions, 3)
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return []
    """
    # 🔹 Dummy questions for GUI
    questions = [
        "What is Python?",
        "Explain OOP concepts.",
        "Describe a hackathon workflow."
    ]
    return questions

# 🔹 Start Hackathon UI
def start_hackathon(email):
    global start_time

    window = tk.Toplevel()
    window.title("Hackathon Round")
    window.geometry("650x550")
    window.configure(bg="#67a69e")

    questions = get_random_questions()
    if not questions:
        return

    entries = []
    y = 20

    label_style = {"bg": "#cfc6b0", "fg": "#2F3E46", "font": ("Segoe UI", 10, "bold italic")}
    entry_font = ("Segoe UI", 10)

    # 🔹 Show Questions
    for q in questions:
        tk.Label(window, text=q, wraplength=550, justify="left", **label_style).place(x=20, y=y)
        entry = tk.Entry(window, width=70, font=entry_font)
        entry.place(x=20, y=y + 30)
        entries.append(entry)
        y += 80

    start_time = time.time()

    # 🔹 Submit Function
    def submit():
        answers = [entry.get().strip() for entry in entries]
        if "" in answers:
            messagebox.showerror("Error", "All questions must be answered")
            return

        # ------------------ Database & AI logic commented ------------------
        """
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
            for q, ans in zip(questions, answers):
                cursor.execute(
                    "INSERT INTO hackathon_answers(student_email, question, answer, time_taken, attempt_done) VALUES(%s,%s,%s,%s,%s)",
                    (email, q, ans, time_taken, 1)
                )
            conn.commit()
            cursor.close()
            conn.close()
            score, status = hackathon_engine.process_hackathon(email, questions, answers)
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
            return
        """

        # 🔹 Dummy result for GUI test
        score = random.randint(50, 100)
        status = "Pass" if score >= 60 else "Fail"

        messagebox.showinfo("Hackathon Result", f"Your Score: {score}\nStatus: {status}")
        window.destroy()

    # 🔹 Submit Button
    tk.Button(
        window,
        text="Submit",
        command=submit,
        bg="#dddecc",
        fg="#2F3E46",
        font=("Segoe UI", 10, "bold italic"),
        relief="raised",
        bd=2,
        width=15
    ).place(x=260, y=470)

    window.mainloop()


# ------------------ Run Directly ------------------
if __name__ == "__main__":
    start_hackathon("student@example.com")