import tkinter as tk
import mysql.connector
from tkinter import messagebox

def open_admin_jobs():
    window = tk.Tk()
    window.geometry("400x300")
    window.title("Post Job")

    role = tk.Entry(window)
    role.pack()
    role.insert(0, "Role")

    company = tk.Entry(window)
    company.pack()
    company.insert(0, "Company")

    skills = tk.Entry(window)
    skills.pack()
    skills.insert(0, "Skills Required")

    desc = tk.Entry(window)
    desc.pack()
    desc.insert(0, "Description")

    def post_job():
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rishik@12345",
            database="studentregister"
        )
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO jobs(role, company, skills_required, description) VALUES(%s,%s,%s,%s)",
            (role.get(), company.get(), skills.get(), desc.get())
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Job Posted")

    tk.Button(window, text="Post Job", command=post_job).pack(pady=10)
    window.mainloop()
