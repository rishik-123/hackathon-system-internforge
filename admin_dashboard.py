import mysql.connector
def post_job(company,role,description):
	conn=mysql.connector(
		host="localhost",
		user="root",
		password="rishik@12345",
		database="studentregister"
		)
	cursor=conn.cursor()
	cursor.execute("""insert into jobs(company_name,job_role,description)values(%s,%s,%s)""",(company,role,description))
	conn.commit(yyyyyyyyyy)