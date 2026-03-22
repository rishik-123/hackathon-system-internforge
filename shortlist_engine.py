import mysql.connector

def select_top_students(limit):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rishik@12345",
        database="studentregister"
    )

    cursor = conn.cursor()

    query = """
    SELECT student_id, SUM(score) AS total
    FROM hackathon_attempts
    GROUP BY student_id
    ORDER BY total DESC
    LIMIT %s
    """

    cursor.execute(query, (limit,))
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result