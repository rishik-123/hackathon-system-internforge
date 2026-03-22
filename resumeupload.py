import tkinter as tk
from tkinter import filedialog, messagebox
import mysql.connector
import PyPDF2
from docx import Document
def extract_text_from_resume(filepath):
    text = ""

    try:
        if filepath.endswith(".pdf"):
            with open(filepath, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    if page.extract_text():
                        text += page.extract_text()

        elif filepath.endswith(".docx"):
            doc = Document(filepath)
            for para in doc.paragraphs:
                text += para.text + " "

    except Exception as e:
        print("Error reading file:", e)

    return text.lower()
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
def resumeupload(name, email):
    window = tk.Tk()
    window.geometry("400x250")
    window.title("Resume Upload")
    filelabel = tk.Label(window, text="No file selected")
    filelabel.pack(pady=20)
    def resumeUpload():
        filepath = filedialog.askopenfilename(
            title="Select Resume",
            filetypes=[("Resume Files", "*.pdf *.docx")]
        )

        if not filepath:
            messagebox.showerror("Error", "No file selected")
            return

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
            match_percentage = match_resume_with_requirements(
                resume_text, requirements
            )
            filelabel.config(text=f"File path:\n{filepath}")
            messagebox.showinfo(
                "Match Result",
                f"Resume uploaded successfully!\n\nMatch Score: {match_percentage:.2f}%"
            )

            cursor.close()
            conn.close()

            window.destroy()

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    uploadbtn = tk.Button(window, text="Upload Resume", command=resumeUpload)
    uploadbtn.pack(pady=10)

    window.mainloop()
