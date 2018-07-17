from bs4 import BeautifulSoup
import re
import MySQLdb
import warnings
import hashlib
import uuid
import random
out = open("new.txt", "w")
html_page = open("Buckton_Castle.html")
soup = BeautifulSoup(html_page, "lxml")
for link in soup.findAll('a'):
	l = link.get('href')
	if l != None:
		print(l, file = out)


db =  MySQLdb.connect("localhost","root","root")
cursor = db.cursor()
sql = "CREATE DATABASE IF NOT EXISTS users"
cursor.execute(sql)
cursor.execute('USE users')
sql1 = "CREATE TABLE IF NOT EXISTS user(interestid VARCHAR(50), interestname VARCHAR(20), userid VARCHAR(50))"
cursor.execute(sql1) 
for i in range(100000):
	userid = uuid.uuid4()
	result = hashlib.md5(str(userid).encode())
	interestid = result.hexdigest()
	name = ["Projects", "Startups", "Travel", "Food", "Music", "Pets", "Relationships"]
	interestname = random.choice(name)
	interestid = str(interestid)
	userid = str(userid)
	sql2  = "INSERT INTO user(interestid, interestname, userid) VALUES(" +interestid+ ", " +interestname+ ", " +userid+ ")"
	try:
		cursor.execute(sql2)
		db.commit()
	except:
		db.rollback()
db.close()
warnings.filterwarnings("ignore", "users")
