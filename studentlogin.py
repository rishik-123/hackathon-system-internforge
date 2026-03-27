import tkinter
import mysql.connector
from tkinter import messagebox
# import studentdashboard   # correct import

def open_login_window():
    window = tkinter.Tk()
    window.title("Student Login")
    window.geometry("400x200")
    window.configure(bg="#67a69e")

    label_style = {"bg": "#cfc6b0", "fg": "#2F3E46", "font": ("Segoe UI", 10, "bold italic")}

    tkinter.Label(window, text="Enter the email", **label_style).place(x=15, y=10)
    emailtxt = tkinter.Entry(window, font=("Segoe UI", 10))
    emailtxt.place(x=200, y=10)

    tkinter.Label(window, text="Enter the password", **label_style).place(x=15, y=40)
    passwordtxt = tkinter.Entry(window, show="*", font=("Segoe UI", 10))
    passwordtxt.place(x=200, y=40)

    def loginvalues():
        email = emailtxt.get()
        password = passwordtxt.get()

        # try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rishik@12345",
            database="studentregister"
        )

        cursor = conn.cursor()

        cursor.execute(
            "SELECT name, email FROM student WHERE email=%s AND password=%s",
            (email, password)
        )

        result = cursor.fetchone()

        if result:
            name = result[0]
            email = result[1]

            messagebox.showinfo("Success", "Login Successful")

            window.destroy()

            # dashboard open
            studentdashboard.open_dashboard(name, email)

        else:
            messagebox.showerror("Error", "Invalid email or password")

        cursor.close()
        conn.close()

        # except Exception as e:
        #     messagebox.showerror("Database Error", str(e))

    tkinter.Button(
        window,
        text="LOGIN",
        command=loginvalues,
        bg="#dddecc",
        fg="#2F3E46",
        font=("Segoe UI", 10, "bold italic"),
        relief="raised",
        bd=2,
        activebackground="#cfc6b0"
    ).place(x=160, y=80)

    window.mainloop()