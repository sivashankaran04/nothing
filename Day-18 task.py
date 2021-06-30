# Create a DB with doctor and doctor ID & patients visited

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="deepak#$1238220994412")
db = mydb.cursor()
db.execute("CREATE DATABASE Doctors")
db = mydb.cursor()
db.execute("SHOW DATABASES")
for entry in db:
    print(entry)
mydb = mysql.connector.connect(host="localhost", user="root", password="deepak#$1238220994412", database="Doctors")
db = mydb.cursor()
db.execute("CREATE TABLE Doctors (dr_id VARCHAR(255), Patient_visited VARCHAR(255))")
db = mydb.cursor()
db.execute("SHOW TABLES")
for value in db:
    print(value)
db = mydb.cursor()
sql = "INSERT INTO Doctors (dr_id , Patient_visited) VALUES (%s,%s)"
val = [('ID01', '10'), ('ID02', '3'), ('ID03', '8'), ('ID05', '0'), ('ID123', '15'), ('ID26', '9'), ('ID78', '0'),
       ('ID65', '0'), ('ID23', '15'), ('ID262', '9'), ('ID783', '0'), ('ID651', '0'), ('ID13', '19'), ('ID267', '7'),
       ('ID08', '0'), ('ID59', '0')]
db.executemany(sql, val)
mydb.commit()
print(db.rowcount, "was inserted.")

# Get the doctor(s) who have more than 5 patients visited

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Doctors where Patient_visited >5")
result = mycursor.fetchall()
for x in result:
    print(x)

# Get the doctors with no patients visit

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Doctors where Patient_visited=0")
res = mycursor.fetchall()
for x in res:
    print(x)
