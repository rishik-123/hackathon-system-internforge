import tkinter as tk
import mysql.connector
from tkinter import messagebox
import recruiter_request
import student_invite


def open_recruiter_page(recruiter_id):

    window = tk.Tk()
    window.title("InternForge - Recruiter Page")
    window.geometry("500x650")

    current_job_id = None

    # ------------------ Form Fields ------------------

    tk.Label(window, text="Recruiter Name").place(x=20, y=20)
    recruiternameField = tk.Entry(window)
    recruiternameField.place(x=220, y=20)

    tk.Label(window, text="Company Name").place(x=20, y=60)
    companynameTextField = tk.Entry(window)
    companynameTextField.place(x=220, y=60)

    tk.Label(window, text="Job Role").place(x=20, y=100)
    jobroleTextField = tk.Entry(window)
    jobroleTextField.place(x=220, y=100)

    tk.Label(window, text="Primary Skill").place(x=20, y=140)
    primaryskillTextField = tk.Entry(window)
    primaryskillTextField.place(x=220, y=140)

    tk.Label(window, text="Minimum CGPA").place(x=20, y=180)
    min_cgpaTextField = tk.Entry(window)
    min_cgpaTextField.place(x=220, y=180)

    tk.Label(window, text="Required Branch").place(x=20, y=220)
    branchTextField = tk.Entry(window)
    branchTextField.place(x=220, y=220)

    # ------------------ MAIN FUNCTION ------------------

    def register_recruiter():

        nonlocal current_job_id

        recruiter_name = recruiternameField.get().strip()
        company_name = companynameTextField.get().strip()
        job_role = jobroleTextField.get().strip()
        primary_skill = primaryskillTextField.get().strip()
        branch = branchTextField.get().strip()

        # 🔴 Validation
        if not all([recruiter_name, company_name, job_role, primary_skill, branch]):
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            min_cgpa = float(min_cgpaTextField.get())
        except:
            messagebox.showerror("Error", "Invalid CGPA")
            return

        try:

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="rishik@12345",
                database="studentregister"
            )

            cursor = conn.cursor()

            # 🔹 Insert job
            cursor.execute(
                """INSERT INTO recruiter_requirements
                (recruiter_id,recruiter_name,company_name,job_role,primary_skill,min_cgpa,branch)
                VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                (recruiter_id, recruiter_name, company_name,
                 job_role, primary_skill, min_cgpa, branch)
            )

            conn.commit()
            current_job_id = cursor.lastrowid

            messagebox.showinfo("Success", "Job Posted Successfully")

            # 🔹 Consultancy Request
            REQUIRED = 10
            INVITE_COUNT = 50

            recruiter_request.store_request(
                company_name,
                job_role,
                REQUIRED,
                INVITE_COUNT,
                "recruiter@email.com"  # later dynamic
            )

            # 🔹 Get matching students
            cursor.execute(
                """SELECT name,email,cgpa 
                   FROM student 
                   WHERE branch=%s AND cgpa >= %s
                   LIMIT %s""",
                (branch, min_cgpa, INVITE_COUNT)
            )

            students = cursor.fetchall()

            if not students:
                messagebox.showinfo("Info", "No matching students found")
                return

            # 🔹 Show invited students
            result_window = tk.Toplevel(window)
            result_window.title("Invited Candidates")
            result_window.geometry("400x350")

            tk.Label(result_window,
                     text="Students Invited for Hackathon",
                     font=("Arial", 12, "bold")).pack(pady=10)

            for student in students:
                name, email, cgpa = student

                tk.Label(result_window,
                         text=f"{name} | {email} | CGPA: {cgpa}").pack()

                # 🔥 Send invitation
                try:
                    student_invite.invite_students(email)
                except Exception as e:
                    print("Mail error:", e)

            messagebox.showinfo("Success", "Invitations sent successfully")

            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    # ------------------ INFO BUTTON ------------------

    def info_message():
        messagebox.showinfo(
            "Hackathon Info",
            "Students will receive email.\nThey will start hackathon from dashboard.\nSystem will auto-evaluate and shortlist."
        )

    # ------------------ BUTTONS ------------------

    tk.Button(window,
              text="Post Job & Invite Students",
              command=register_recruiter,
              bg="green",
              fg="white",
              width=25).place(x=130, y=500)

    tk.Button(window,
              text="Hackathon Info",
              command=info_message,
              bg="blue",
              fg="white",
              width=25).place(x=130, y=550)

    window.mainloop()


# Run directly
if __name__ == "__main__":
    open_recruiter_page(1)