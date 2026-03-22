import requests

def sendsubmissionmail(email,score,status):

    url = "http://localhost:5678/webhook-test/hackathon-submit"

    data = {
        "email": email,
        "score": score,
        "status": status
    }

    try:
        requests.post(url,json=data)
        print("Webhook sent to n8n")

    except Exception as e:
        print("Webhook error:",e)