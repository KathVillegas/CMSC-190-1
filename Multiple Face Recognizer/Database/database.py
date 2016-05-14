import MySQLdb

#creating a database
db = MySQLdb.connect("localhost", "root", "root")
cursor = db.cursor()
sql = 'CREATE DATABASE attendancemonitoringsystem'
cursor.execute(sql)
