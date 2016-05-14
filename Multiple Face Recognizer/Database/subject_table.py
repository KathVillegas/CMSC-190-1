import MySQLdb

db = MySQLdb.connect("localhost", "root", "root", "attendancemonitoringsystem")
cursor = db.cursor()

sql = """ CREATE TABLE SUBJECT (
			id INT AUTO_INCREMENT KEY,
			subject VARCHAR(50),
			section VARCHAR(50)
		)"""

cursor.execute(sql)

db.close()