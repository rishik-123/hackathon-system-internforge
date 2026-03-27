import tkinter as tk
import mysql.connector
from tkinter import messagebox
# import recruiter_request
# import student_invite

def open_recruiter_page(recruiter_id):
    window = tk.Tk()
    window.title("InternForge - Recruiter Page")
    window.geometry("500x650")
    window.configure(bg="#67a69e")

    current_job_id = None
    label_style = {"bg": "#cfc6b0", "fg": "#2F3E46", "font": ("Segoe UI", 10, "bold italic")}
    entry_font = ("Segoe UI", 10)

    # ------------------ Form Fields ------------------
    tk.Label(window, text="Recruiter Name", **label_style).place(x=20, y=20)
    recruiternameField = tk.Entry(window, font=entry_font)
    recruiternameField.place(x=220, y=20)

    tk.Label(window, text="Company Name", **label_style).place(x=20, y=60)
    companynameTextField = tk.Entry(window, font=entry_font)
    companynameTextField.place(x=220, y=60)

    tk.Label(window, text="Job Role", **label_style).place(x=20, y=100)
    jobroleTextField = tk.Entry(window, font=entry_font)
    jobroleTextField.place(x=220, y=100)

    tk.Label(window, text="Primary Skill", **label_style).place(x=20, y=140)
    primaryskillTextField = tk.Entry(window, font=entry_font)
    primaryskillTextField.place(x=220, y=140)

    tk.Label(window, text="Minimum CGPA", **label_style).place(x=20, y=180)
    min_cgpaTextField = tk.Entry(window, font=entry_font)
    min_cgpaTextField.place(x=220, y=180)

    tk.Label(window, text="Required Branch", **label_style).place(x=20, y=220)
    branchTextField = tk.Entry(window, font=entry_font)
    branchTextField.place(x=220, y=220)

    # ------------------ MAIN FUNCTION ------------------
    def register_recruiter():
        nonlocal current_job_id
        recruiter_name = recruiternameField.get().strip()
        company_name = companynameTextField.get().strip()
        job_role = jobroleTextField.get().strip()
        primary_skill = primaryskillTextField.get().strip()
        branch = branchTextField.get().strip()

        if not all([recruiter_name, company_name, job_role, primary_skill, branch]):
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            min_cgpa = float(min_cgpaTextField.get())
        except:
            messagebox.showerror("Error", "Invalid CGPA")
            return

        # ------------------ Database Operations (Commented for GUI test) ------------------
        """
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="rishik@12345",
                database="studentregister"
            )
            cursor = conn.cursor()
            cursor.execute(
                \"\"\"INSERT INTO recruiter_requirements
                (recruiter_id,recruiter_name,company_name,job_role,primary_skill,min_cgpa,branch)
                VALUES (%s,%s,%s,%s,%s,%s,%s)\"\"\",
                (recruiter_id, recruiter_name, company_name,
                 job_role, primary_skill, min_cgpa, branch)
            )
            conn.commit()
            current_job_id = cursor.lastrowid
            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
            return
        """

        messagebox.showinfo("Success", "Job Posted Successfully (GUI Mode)")

        # ------------------ Info / Invitations ------------------
        info_message()

    # ------------------ INFO BUTTON ------------------
    def info_message():
        messagebox.showinfo(
            "Hackathon Info",
            "Students will receive email.\nThey will start hackathon from dashboard.\nSystem will auto-evaluate and shortlist."
        )

    # ------------------ BUTTONS ------------------
    tk.Button(
        window,
        text="Post Job & Invite Students",
        command=register_recruiter,
        bg="#dddecc",
        fg="#2F3E46",
        font=("Segoe UI", 10, "bold italic"),
        relief="raised",
        bd=2,
        width=25
    ).place(x=130, y=500)

    tk.Button(
        window,
        text="Hackathon Info",
        command=info_message,
        bg="#dddecc",
        fg="#2F3E46",
        font=("Segoe UI", 10, "bold italic"),
        relief="raised",
        bd=2,
        width=25
    ).place(x=130, y=550)

    window.mainloop()


#  Main guard for direct execution
if __name__ == "__main__":
    open_recruiter_page(1)