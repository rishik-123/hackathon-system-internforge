import requests

N8N_URL = "http://localhost:5678/webhook-test/hackathon-submit"

def invite_students(student_email):
    data = {
        "email": student_email,
        "subject": "Hackathon Invitation",
        "message": "You are invited to participate in the hiring hackathon"
    }

    try:
        requests.post(N8N_URL, json=data)
        print("Invitation sent")
    except Exception as e:
        print("Error sending invite:", e)