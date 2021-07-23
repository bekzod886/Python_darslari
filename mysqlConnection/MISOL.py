import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",

)
mycursor = mydb.cursor()

mycursor.execute("show databases")
db = []
for x in mycursor:
     db.append(x[0])


if "test" in db:
    print("bor")
else:print("yuq")
