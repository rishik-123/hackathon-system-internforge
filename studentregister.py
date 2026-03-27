# studentregister.py

import tkinter as tk
import mysql.connector
from tkinter import messagebox
import studentlogin
def open_register_window():

    window = tk.Tk()
    window.geometry("400x430")
    window.title("InternForge - Student Registration")

    # ------------------ Labels & Entry Fields ------------------

    tk.Label(window, text="Enter your name").place(x=15, y=10)
    nameTextField = tk.Entry(window)
    nameTextField.place(x=200, y=10)

    tk.Label(window, text="Enter your email").place(x=15, y=40)
    emailTextField = tk.Entry(window)
    emailTextField.place(x=200, y=40)

    tk.Label(window, text="Enter your mobile number").place(x=15, y=70)
    mobileTextField = tk.Entry(window)
    mobileTextField.place(x=200, y=70)

    tk.Label(window, text="Enter your password").place(x=15, y=100)
    passTextField = tk.Entry(window, show="*")
    passTextField.place(x=200, y=100)

    tk.Label(window, text="Enter the college name").place(x=15, y=130)
    academicTextField = tk.Entry(window)
    academicTextField.place(x=200, y=130)

    tk.Label(window, text="Enter the degree you pursuing").place(x=15, y=160)
    degreeTextField = tk.Entry(window)
    degreeTextField.place(x=200, y=160)

    tk.Label(window, text="Enter the branch").place(x=15, y=190)
    branchTextField = tk.Entry(window)
    branchTextField.place(x=200, y=190)

    tk.Label(window, text="Enter the Course duration year").place(x=15, y=220)
    yearTextField = tk.Entry(window)
    yearTextField.place(x=200, y=220)

    tk.Label(window, text="Enter your CGPA").place(x=15, y=250)
    CGPATextField = tk.Entry(window)
    CGPATextField.place(x=200, y=250)

    tk.Label(window, text="Enter your current skills").place(x=15, y=280)
    skillsTextField = tk.Entry(window)
    skillsTextField.place(x=200, y=280)

    tk.Label(window, text="Enter your primary(job-focused) skill").place(x=15, y=310)
    primaryTextField = tk.Entry(window)
    primaryTextField.place(x=200, y=310)

    tk.Label(window, text="Enter the level(beginner/intermediate/advanced)").place(x=15, y=340)
    levelTextField = tk.Entry(window)
    levelTextField.place(x=200, y=340)

    # ------------------ Register Function ------------------

    def register_student():

        name = nameTextField.get()
        email = emailTextField.get()
        phone_number = mobileTextField.get()
        password = passTextField.get()
        college_name = academicTextField.get()
        branch = branchTextField.get()
        degree = degreeTextField.get()
        year = yearTextField.get()
        CGPA = CGPATextField.get()
        skills = skillsTextField.get()
        primary_skill = primaryTextField.get()
        skill_level = levelTextField.get()

        if year == "" or CGPA == "":
            messagebox.showerror("Error", "Year and CGPA cannot be empty")
            return

<<<<<<< HEAD
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="rishik@12345",
                database="studentregister"
            )

            cursor = conn.cursor()

            sql = """INSERT INTO student
            (name,email,phone_number,password,college_name,branch,year,CGPA,
             skills,primary_skill,skill_level,degree)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

            values = (
                name, email, phone_number, password, college_name, branch,
                year, CGPA, skills, primary_skill, skill_level, degree
            )

            cursor.execute(sql, values)
            conn.commit()

            cursor.close()
            conn.close()
=======
        # try:
        #     conn = mysql.connector.connect(
        #         host="localhost",
        #         user="root",
        #         password="rishik@12345",
        #         database="studentregister"
        #     )

        #     cursor = conn.cursor()

        #     sql = """INSERT INTO student
        #     (name,email,phone_number,password,college_name,branch,year,CGPA,
        #      skills,primary_skill,skill_level,degree)
        #     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        #     values = (
        #         name, email, phone_number, password, college_name, branch,
        #         year, CGPA, skills, primary_skill, skill_level, degree
        #     )

        #     cursor.execute(sql, values)
        #     conn.commit()

        #     cursor.close()
        #     conn.close()
>>>>>>> b1e2a6f (Added requirement.txt)

            messagebox.showinfo("Success", "Registration successful!")

            window.destroy()
            studentlogin.open_login_window()

<<<<<<< HEAD
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
=======
        # except Exception as e:
        #     messagebox.showerror("Database Error", str(e))
>>>>>>> b1e2a6f (Added requirement.txt)

    # ------------------ Register Button ------------------

    tk.Button(window, text="REGISTER", command=register_student).place(x=50, y=380)
    tk.Button(window,text="LOGIN",command=studentlogin.open_login_window).place(x=250,y=380)
    window.mainloop()


# Only run if file executed directly
if __name__ == "__main__":
    open_register_window()
