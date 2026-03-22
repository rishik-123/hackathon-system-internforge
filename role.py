import tkinter as tk
import studentlogin
import admin
import studentregister


def role_page():

    window = tk.Tk()
    window.title("InternForge")
    window.geometry("300x200")

    def student_login():
        window.destroy()
        studentregister.open_register_window()

    def admin_login():
        window.destroy()
        admin.adminlogin()

    tk.Label(window, text="Login As").pack(pady=20)

    tk.Button(window, text="Student", width=15, command=student_login).pack(pady=5)
    tk.Button(window, text="Recruiter / Admin", width=15, command=admin_login).pack(pady=5)

    window.mainloop()


# Only run when role.py is executed directly
if __name__ == "__main__":
    role_page()