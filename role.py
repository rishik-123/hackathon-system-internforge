import tkinter as tk
# import studentlogin
# import admin
# import studentregister


def role_page():

    window = tk.Tk()
    window.title("InternForge")
    window.geometry("350x250")
    window.configure(bg='#67a69e')

    def student_login():
        window.destroy()
        studentregister.open_register_window()

    def admin_login():
        window.destroy()
        admin.adminlogin()

    # Title Label
    tk.Label(
        window,
        text="Login As",
        fg='#2F3E46',
        bg="#cfc6b0",
        font=("Segoe UI", 22, "bold italic"),
        padx=10,
        pady=5
    ).pack(pady=20)

    # Student Button
    tk.Button(
        window,
        text="Student",
        width=20,
        command=student_login,
        bg="#dddecc",
        fg="#2F3E46",
        relief="raised",
        bd=2,
        font=("Segoe UI", 12, "bold italic"),
        activebackground="#cfc6b0"
    ).pack(pady=10)

    # Admin Button
    tk.Button(
        window,
        text="Recruiter / Admin",
        width=20,
        command=admin_login,
        bg="#dddecc",
        fg="#2F3E46",
        relief="raised",
        bd=2,
        font=("Segoe UI", 12, "bold italic"),
        activebackground="#cfc6b0"
    ).pack(pady=10)

    window.mainloop()


# Only run when role.py is executed directly
if __name__ == "__main__":
    role_page()