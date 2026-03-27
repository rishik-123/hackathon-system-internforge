import tkinter as tk
# import resumeupload
# import hackathon_ui

def open_dashboard(name, email):

    # ------------------ Main Window ------------------
    window = tk.Tk()
    window.title("Student Dashboard")
    window.geometry("450x300")
    window.configure(bg="#67a69e")  # Background color

    label_style = {"bg": "#cfc6b0", "fg": "#2F3E46", "font": ("Segoe UI", 12, "bold italic")}

    # ------------------ Welcome Label ------------------
    tk.Label(window, text=f"Welcome {name}", **label_style, wraplength=400, justify="center").pack(pady=20)

    button_style = {
        "bg": "#dddecc",
        "fg": "#2F3E46",
        "font": ("Segoe UI", 10, "bold italic"),
        "relief": "raised",
        "bd": 2,
        "width": 25
    }

    # ------------------ Resume Upload Button ------------------
    tk.Button(
        window,
        text="Upload Resume",
        command=lambda: resumeupload.resumeupload(name, email),
        **button_style
    ).pack(pady=10)

    # ------------------ Hackathon Button ------------------
    tk.Button(
        window,
        text="Start Hackathon",
        command=lambda: hackathon_ui.start_hackathon(email),
        **button_style
    ).pack(pady=10)

    window.mainloop()

# ------------------ Run directly for GUI test ------------------
if __name__ == "__main__":
    open_dashboard("Test Student", "test@student.com")