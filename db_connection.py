import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rishik@12345",
        database="studentregister"
    )
    return conn