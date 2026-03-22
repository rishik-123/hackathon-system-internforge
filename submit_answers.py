from db_connection import get_connection

def save_answers(email, answers):
    conn = get_connection()
    cursor = conn.cursor()

    for qid, ans in answers.items():

        cursor.execute("""
        INSERT INTO hackathon_answers
        (student_email, question_id, student_answer)
        VALUES (%s,%s,%s)
        """,(email, qid, ans))

    conn.commit()

    cursor.close()
    conn.close()