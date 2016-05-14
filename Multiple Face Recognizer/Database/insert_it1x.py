import MySQLdb
from PIL import Image
import PIL.Image

db = MySQLdb.connect("localhost", "root", "root","attendancemonitoringsystem")
cursor = db.cursor()

data = [
		(7, 'Sheena', 'De Jesus', 'BSN', 'CHE'),
		(8, 'Raiza', 'Cusi', 'BSBio', 'CAS'),
		(9, 'Shane', 'Taggueg', 'BSN', 'CHE'),
		(10, 'Steffi', 'Villaruz', 'BSN', 'CHE'),
		(11, 'Gabriel', 'Comota', 'PREVM', 'CVM'),
		(12, 'Czarina', 'Sillos', 'BSN', 'CHE')
	   ]
template = ','.join(['%s'] * len(data))
query = 'INSERT INTO IT1X (student_id, first_name, last_name, course, college) values {0}'.format(template)

try:
	cursor.execute(query, data)
	db.commit()
except:
	db.rollback()
	
db.close()