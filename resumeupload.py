import tkinter as tk
from tkinter import filedialog, messagebox
# import mysql.connector
# import PyPDF2
# from docx import Document

# ------------------ Extract text from PDF or DOCX ------------------
def extract_text_from_resume(filepath):
    text = ""
    try:
        if filepath.endswith(".pdf"):
            # with open(filepath, "rb") as file:
            #     reader = PyPDF2.PdfReader(file)
            #     for page in reader.pages:
            #         if page.extract_text():
            #             text += page.extract_text()
            text = "dummy pdf text for GUI test"
        elif filepath.endswith(".docx"):
            # doc = Document(filepath)
            # for para in doc.paragraphs:
            #     text += para.text + " "
            text = "dummy docx text for GUI test"
    except Exception as e:
        print("Error reading file:", e)
    return text.lower()

# ------------------ Match resume text with requirements ------------------
def match_resume_with_requirements(resume_text, requirements):
    score = 0
    total_keywords = 0
    for req in requirements:
        for keyword in req:
            if keyword:
                total_keywords += 1
                if keyword.lower() in resume_text:
                    score += 1
    if total_keywords == 0:
        return 0
    return (score / total_keywords) * 100

# ------------------ Resume Upload GUI ------------------
def resumeupload(name, email):
    window = tk.Tk()
    window.geometry("450x300")
    window.title("Resume Upload")
    window.configure(bg="#67a69e")

    label_style = {"bg": "#cfc6b0", "fg": "#2F3E46", "font": ("Segoe UI", 10, "bold italic")}

    # File path label
    filelabel = tk.Label(window, text="No file selected", **label_style, wraplength=400, justify="center")
    filelabel.pack(pady=20)

    # ------------------ Upload Function ------------------
    def resumeUpload():
        # ------------------ File selection ------------------
        filepath = filedialog.askopenfilename(
            title="Select Resume",
            filetypes=[("Resume Files", "*.pdf *.docx")]
        )

        if not filepath:
            messagebox.showerror("Error", "No file selected")
            return

        # ------------------ Database interaction commented ------------------
        """
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="rishik@12345",
                database="studentregister"
            )
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO uploadresume (name, email, file_path) VALUES (%s, %s, %s)",
                (name, email, filepath)
            )
            conn.commit()

            resume_text = extract_text_from_resume(filepath)
            cursor.execute(
                "SELECT primary_skill, job_role, degree, branch FROM recruiter_requirements"
            )
            requirements = cursor.fetchall()
            match_percentage = match_resume_with_requirements(resume_text, requirements)
            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
            return
        """
        # 🔹 Dummy match percentage for GUI test
        match_percentage = 75.0

        filelabel.config(text=f"File path:\n{filepath}")
        messagebox.showinfo(
            "Match Result",
            f"Resume uploaded successfully!\n\nMatch Score: {match_percentage:.2f}%"
        )

    # ------------------ Upload Button ------------------
    uploadbtn = tk.Button(
        window,
        text="Upload Resume",
        command=resumeUpload,
        bg="#dddecc",
        fg="#2F3E46",
        font=("Segoe UI", 10, "bold italic"),
        relief="raised",
        bd=2,
        width=20
    )
    uploadbtn.pack(pady=10)

    window.mainloop()

# ------------------ Run directly for GUI test ------------------
if __name__ == "__main__":
    resumeupload("Test Student", "test@student.com")