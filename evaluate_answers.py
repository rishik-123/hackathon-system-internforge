import mysql.connector

def evaluate_student(email):

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rishik@12345",
        database="studentregister"
    )

    cursor = conn.cursor()

    cursor.execute("""
    SELECT answer FROM hackathon_answers
    WHERE student_email=%s
    """, (email,))

    answers = cursor.fetchall()

    score = 0

    # 
    for ans in answers:
        if ans[0] and len(ans[0]) > 5:
            score += 1

    cursor.close()
    conn.close()

    return score