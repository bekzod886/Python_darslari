import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="school"

)
mycursor = mydb.cursor()

print("--Ismlar jadvali--")
print("1. jadvalni ko'rish;")
print("2. ism qo'shish")
print("3. ism o'zgartirish")
print("4. ism o'chirish")
print("0. chiqish")
while True:
    n= int(input("Kerakli raqamni tanlang:"))
    if n==1:
        mycursor.execute("select * from ismlar")
        j=0
        for i in mycursor:
            print(i)
        if j==0:
            print("bosh")
