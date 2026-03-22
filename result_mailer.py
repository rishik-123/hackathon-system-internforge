import requests

def send_results(email, students):
    data = {
        "email": email,
        "subject": "Shortlisted Students",
        "students": str(students)
    }

    try:
        requests.post("http://localhost:5678/webhook-test/hackathon-submit", json=data)
        print("Results sent")
    except Exception as e:
        print("Error sending results:", e)