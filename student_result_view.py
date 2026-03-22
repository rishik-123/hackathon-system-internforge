from db_connection import get_connection

def show_results():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT student_email,score,time_taken,status
    FROM hackathon_results
    ORDER BY score DESC
    """)

    results = cursor.fetchall()

    for r in results:
        print(r[0], r[1], r[2], r[3])