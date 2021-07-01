# Create a connection for DB and print the version using a python program

import mysql.connector

mydata = mysql.connector.connect(host='localhost', user='root', password='deepak#$1238220994412')
curs = mydata.cursor()
curs.execute("SELECT VERSION()")
data = curs.fetchone()
print("Version :", data)


# 2 Create a multiple tables & insert data in table

curs.execute('CREATE DATABASE mydbase')
conn = mysql.connector.connect(host='localhost', user='root', password='deepak#$1238220994412', database='mydbase')
curs = conn.cursor(buffered=True)
curs.execute('CREATE TABLE student(Stu_Id INTEGER(7), Stu_Name VARCHAR(255), Stu_Dept VARCHAR(255))')
curs.execute('CREATE TABLE staff(Staff_Id INTEGER(7), Staff_Name VARCHAR(255), Staff_Dept VARCHAR(255))')
curs.execute("SHOW TABLES")
for value in curs:
    print(value)
query = 'INSERT INTO student(Stu_Id, Stu_Name, Stu_Dept) VALUES(%s, %s, %s)'
data = [(234, 'Deepak', 'MCA'), (535, 'Akki', 'MCA'), (782, 'Shiva', 'MCA')]
for value in data:
    curs.execute(query, value)
query = 'INSERT INTO staff(Staff_Id, Staff_Name, Staff_Dept) VALUES(%s, %s, %s)'
data = [(922, 'David', 'CSE'), (452, 'Rose', 'ECE')]
for value in data:
    curs.execute(query, value)
curs.execute('SELECT * from student')
student = curs.fetchall()
print(f'Students\n{"-"*8}')
for details in student:
    print(details)

# Create an employee table and read all the employee names in the table using for loop

curs.execute('CREATE TABLE Employee(Id INTEGER(7), Name VARCHAR(255), Salary INTEGER(7))')
sql = 'INSERT INTO Employee(Id, Name, Salary) VALUES(%s, %s, %s)'
data = [(2634, 'Deepak', 250000), (5135, 'Akki', 25000), (7682, 'Shiva', 34000), (3482, 'Balaji', 45000)]
for value in data:
    curs.execute(sql, value)
curs.execute('SELECT Name from Employee')
employee = curs.fetchall()
print(f'Employees\n{"-"*9}')
for name in employee:
    print(name[0])
