import tkinter as tk
# import resumeupload
# import hackathon_ui

def open_dashboard(name, email):   # ✅ 2 parameters

    window = tk.Tk()
    window.title("Student Dashboard")
    window.geometry("400x300")

    tk.Label(window, text=f"Welcome {name}", font=("Arial", 14)).pack(pady=20)

    # ✅ Resume Upload Button
    tk.Button(window,
              text="Upload Resume",
              width=20,
              command=lambda: resumeupload.resumeupload(name, email)
              ).pack(pady=10)

    # ✅ Hackathon Button
    tk.Button(window,
              text="Start Hackathon",
              width=20,
              command=lambda: hackathon_ui.start_hackathon(email)
              ).pack(pady=10)

    window.mainloop()