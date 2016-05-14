import MySQLdb
from PIL import Image
import PIL.Image

db = MySQLdb.connect("localhost", "root", "root","attendancemonitoringsystem")
cursor = db.cursor()

data = [
		(1, 'Rayhan', 'Sajorda', 'BSBio', 'CAS'),
		(2, 'Christien', 'Casidsid', 'BSN', 'CHE'),
		(3, 'Merven', 'Medrano', 'BSN', 'CHE'),
		(4, 'Joseph', 'Valenzuela', 'PREVM', 'CVM'),
		(5, 'Angelica', 'Encarnacion', 'PREVM', 'CVM'),
		(6, 'Vinz', 'Leonardo', 'BSN', 'CHE')
	   ]
template = ','.join(['%s'] * len(data))
query = 'INSERT INTO IT1Y (student_id, first_name, last_name, course, college) values {0}'.format(template)

try:
	cursor.execute(query, data)
	db.commit()
except:
	db.rollback()
	
db.close()