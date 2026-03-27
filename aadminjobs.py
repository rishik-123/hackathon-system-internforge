import tkinter as tk
# import mysql.connector
# from tkinter import messagebox

def open_admin_jobs():
    window = tk.Tk()
    window.geometry("400x300")
    window.title("Post Job")
    window.configure(bg="#67a69e")

    label_style = {"bg": "#cfc6b0", "fg": "#2F3E46", "font": ("Segoe UI", 10, "bold italic")}

    tk.Label(window, text="Role", **label_style).pack(pady=5)
    role = tk.Entry(window, font=("Segoe UI", 10))
    role.pack()

    tk.Label(window, text="Company", **label_style).pack(pady=5)
    company = tk.Entry(window, font=("Segoe UI", 10))
    company.pack()

    tk.Label(window, text="Skills Required", **label_style).pack(pady=5)
    skills = tk.Entry(window, font=("Segoe UI", 10))
    skills.pack()

    tk.Label(window, text="Description", **label_style).pack(pady=5)
    desc = tk.Entry(window, font=("Segoe UI", 10))
    desc.pack()

    def post_job():
        # try:
        # conn = mysql.connector.connect(
        #     host="localhost",
        #     user="root",
        #     password="rishik@12345",
        #     database="studentregister"
        # )
        # cursor = conn.cursor()
        # cursor.execute(
        #     "INSERT INTO jobs(role, company, skills_required, description) VALUES(%s,%s,%s,%s)",
        #     (role.get(), company.get(), skills.get(), desc.get())
        # )
        # conn.commit()
        # conn.close()
        # messagebox.showinfo("Success", "Job Posted")
        pass  # placeholder for DB code

    tk.Button(
        window,
        text="Post Job",
        command=post_job,  #  fix here: no parentheses
        bg="#dddecc",
        fg="#2F3E46",
        font=("Segoe UI", 10, "bold italic"),
        relief="raised",
        bd=2,
        activebackground="#cfc6b0"
    ).pack(pady=10)

    window.mainloop()

# Main guard so GUI opens when running directly
if __name__ == "__main__":
    open_admin_jobs()