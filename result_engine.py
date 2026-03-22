import mysql.connector
from evaluate_answers import evaluate_student

def process_result(email, time_taken):

    score = evaluate_student(email)   # 🔥 Gemini से score आएगा

    # simple shortlist logic
    if score >= 3:
        status = "Selected"
    else:
        status = "Rejected"

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rishik@12345",
        database="studentregister"
    )

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO hackathon_results(student_email, score, time_taken, status)
    VALUES (%s,%s,%s,%s)
    """, (email, score, time_taken, status))

    conn.commit()

    cursor.close()
    conn.close()

    return score, status