import tkinter as tk
# import mysql.connector
# from tkinter import messagebox

def open_admin_jobs():
    window = tk.Tk()
    window.geometry("400x350")
    window.title("Post Job")
    window.configure(bg="#67a69e")

    label_style = {"bg": "#cfc6b0", "fg": "#2F3E46", "font": ("Segoe UI", 10, "bold italic")}
    entry_font = ("Segoe UI", 10)

    # ------------------ Labels & Entry Fields ------------------
    tk.Label(window, text="Role", **label_style).pack(pady=5)
    role = tk.Entry(window, font=entry_font)
    role.pack()
    role.insert(0, "Role")

    tk.Label(window, text="Company", **label_style).pack(pady=5)
    company = tk.Entry(window, font=entry_font)
    company.pack()
    company.insert(0, "Company")

    tk.Label(window, text="Skills Required", **label_style).pack(pady=5)
    skills = tk.Entry(window, font=entry_font)
    skills.pack()
    skills.insert(0, "Skills Required")

    tk.Label(window, text="Description", **label_style).pack(pady=5)
    desc = tk.Entry(window, font=entry_font)
    desc.pack()
    desc.insert(0, "Description")

    # ------------------ Button Function ------------------
    def post_job():
        # ------------------ Database Logic (Commented for GUI test) ------------------
        """
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
        """
        tk.messagebox.showinfo("Success", "Job Posted (GUI Mode)")

    # ------------------ Post Button ------------------
    tk.Button(
        window,
        text="Post Job",
        command=post_job,
        bg="#dddecc",
        fg="#2F3E46",
        font=("Segoe UI", 10, "bold italic"),
        relief="raised",
        bd=2,
        width=20
    ).pack(pady=10)

    window.mainloop()

# ------------------ Main Guard ------------------
if __name__ == "__main__":
    open_admin_jobs()