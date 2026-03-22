import mysql.connector

def rank_students():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rishik@12345",
        database="studentregister"
    )

    cursor = conn.cursor()

    cursor.execute("""
    SELECT student_email, score, time_taken
    FROM hackathon_results
    ORDER BY score DESC, time_taken ASC
    """)

    students = cursor.fetchall()

    top_students = students[:10]   # 🔥 top 10

    for student in students:

        email = student[0]

        if student in top_students:
            status = "Selected"
        else:
            status = "Rejected"

        cursor.execute("""
        UPDATE hackathon_results
        SET status=%s
        WHERE student_email=%s
        """, (status, email))

    conn.commit()

    cursor.close()
    conn.close()

    print("Ranking Done")