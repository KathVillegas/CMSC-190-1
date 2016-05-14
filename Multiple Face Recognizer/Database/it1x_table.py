import MySQLdb

db = MySQLdb.connect("localhost", "root", "root", "attendancemonitoringsystem")
cursor = db.cursor()

sql = """ CREATE TABLE IT1X (
			id INT AUTO_INCREMENT KEY,
			student_id INT,
			first_name VARCHAR(50),
			last_name VARCHAR(50),
			course VARCHAR(50),
			college VARCHAR(50)
		)"""

cursor.execute(sql)
db.close()