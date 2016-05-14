import MySQLdb

db = MySQLdb.connect("localhost", "root", "root","attendancemonitoringsystem")
cursor = db.cursor()

data = [
		('IT1', 'X'),
		('IT1', 'Y'),
		('IT1', 'Z')
	   ]
template = ','.join(['%s'] * len(data))
query = 'INSERT INTO SUBJECT (subject, section) values {0}'.format(template)

try:
	cursor.execute(query, data)
	db.commit()
except:
	db.rollback()
	
db.close()