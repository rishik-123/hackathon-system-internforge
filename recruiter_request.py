import mysql.connector

def store_request(company, role, required, invite, email):

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rishik@12345",
        database="studentregister"
    )

    cursor = conn.cursor()

    query = """
    INSERT INTO recruiter_requests
    (compnay_name, role, students_required, invite_count, email, status)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(query, (company, role, required, invite, email, "pending"))

    conn.commit()

    cursor.close()
    conn.close()