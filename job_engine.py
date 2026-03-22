import mysql.connector

def post_job(company, role, description):

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rishik@12345",
        database="studentregister"
    )

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO jobs(company_name,job_role,description)
    VALUES(%s,%s,%s)
    """,(company,role,description))

    conn.commit()
    conn.close()

    print("Job Posted Successfully")