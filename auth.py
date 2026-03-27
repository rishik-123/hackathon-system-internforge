import mysql.connector
import tkinter as tk
from tkinter import messagebox
# import role

window = tk.Tk()
window.title("Sign In")
window.geometry("400x300")
window.configure(bg='#67a69e')

# Title Label
tk.Label(
    window,
    text="Sign In",
    bg="#cfc6b0",
    fg="#2F3E46",
    font=("Segoe UI", 22, "bold italic"),
    padx=10,
    pady=5
).pack(pady=20)

# Password Label
passwordLabel = tk.Label(
    window,
    text="Enter the password",
    bg="#cfc6b0",
    fg="#2F3E46",
    font=("Segoe UI", 12, "bold italic")
)
passwordLabel.pack(pady=5)

# Password Entry
passwordField = tk.Entry(
    window,
    show="*",
    font=("Segoe UI", 12),
    bd=2,
    relief="solid"
)
passwordField.pack(pady=10, ipadx=10, ipady=3)


def authvalues():
    passvalues = passwordField.get()

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rishik@12345",
        database="studentregister"
    )

    cursor = conn.cursor()

    sql = "SELECT password FROM main_auth WHERE password=%s"
    cursor.execute(sql, (passvalues,))

    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", "Login Successful")
        window.destroy()
        role.role_page()   # function inside role.py
    else:
        messagebox.showerror("Error", "Wrong Password")

    cursor.close()
    conn.close()


# Login Button
loginbtn = tk.Button(
    window,
    text="LOGIN",
    command=authvalues,
    bg="#dddecc",
    fg="#2F3E46",
    relief="raised",
    bd=2,
    font=("Segoe UI", 12, "bold italic"),
    activebackground="#cfc6b0",
    width=15
)
loginbtn.pack(pady=20)

window.mainloop()