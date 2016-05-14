import MySQLdb

db = MySQLdb.connect("localhost", "root", "root", "attendancemonitoringsystem")
cursor = db.cursor()

sql = """ CREATE TABLE ATTENDANCE (
			id INT AUTO_INCREMENT KEY,
			student_id INT,
			subject VARCHAR(50),
			section VARCHAR(50),
			attendance_date DATE
		)"""

cursor.execute(sql)

db.close()