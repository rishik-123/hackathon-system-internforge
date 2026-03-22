import mysql.connector
import tkinter as tk
from tkinter import messagebox
import role

window = tk.Tk()
window.title("Sign In")
window.geometry("400x300")

# Password Label
passwordLabel = tk.Label(window, text="Enter the password")
passwordLabel.place(x=140, y=100)

# Password Entry
passwordField = tk.Entry(window, show="*")
passwordField.place(x=120, y=130, width=160)


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
loginbtn = tk.Button(window, text="LOGIN", command=authvalues)
loginbtn.place(x=160, y=180)

window.mainloop()