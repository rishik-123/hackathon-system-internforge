import tkinter as tk
import mysql.connector
from tkinter import messagebox
# import adminhomepage  # uncomment when adminhomepage.py exists

def adminlogin():
    window = tk.Tk()
    window.geometry("300x200")
    window.title("Admin Login")
    window.configure(bg="#67a69e")

    label_style = {"bg": "#cfc6b0", "fg": "#2F3E46", "font": ("Segoe UI", 10, "bold italic")}

    tk.Label(window, text="Email", **label_style).pack(pady=5)
    email = tk.Entry(window, font=("Segoe UI", 10))
    email.pack(pady=5)

    tk.Label(window, text="Password", **label_style).pack(pady=5)
    password = tk.Entry(window, show="*", font=("Segoe UI", 10))
    password.pack(pady=5)

    def login():
        # try:
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
            # adminhomepage.open_recruiter_page(recruiter_id)
        else:
            messagebox.showerror("Error", "Invalid admin login")

        conn.close()
        # except Exception as e:
        #     messagebox.showerror("Database Error", str(e))

    tk.Button(
        window,
        text="LOGIN",
        command=login,
        bg="#dddecc",
        fg="#2F3E46",
        font=("Segoe UI", 10, "bold italic"),
        relief="raised",
        bd=2,
        activebackground="#cfc6b0"
    ).pack(pady=10)

    window.mainloop()
if __name__ == "__main__":
    adminlogin()