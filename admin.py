import tkinter as tk
import mysql.connector
from tkinter import messagebox
import adminhomepage 

def adminlogin():
    window = tk.Tk()
    window.geometry("300x200")
    window.title("Admin Login")

    tk.Label(window, text="Email").pack()
    email = tk.Entry(window)
    email.pack(pady=5)

    tk.Label(window, text="Password").pack()
    password = tk.Entry(window, show="*")
    password.pack(pady=5)

    def login():
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rishik@12345",
            database="studentregister"
        )
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id FROM recruiter_register WHERE email=%s AND password=%s",
            (email.get(), password.get())
        )

        result = cursor.fetchone()

        if result:
            recruiter_id = result[0]
            window.destroy()
            adminhomepage.open_recruiter_page(recruiter_id)
        else:
            messagebox.showerror("Error", "Invalid admin login")

        conn.close()

    tk.Button(window, text="LOGIN", command=login).pack(pady=10)

    window.mainloop()
