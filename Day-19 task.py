import pandas as pd
data = pd.read_excel('student_data.xlsx')
print(data)

import xlrd
book = xlrd.open_workbook('student_data.xlsx')
sheet = book.sheet_by_name('Sheet1')

import mysql.connector as msq
db = msq.connect(host='localhost', user='root', password='deepak#$1238220994412', database='mydb')
curs = db.cursor(buffered=True)
tab_q = 'CREATE TABLE student(StudentID varchar(50), FirstName varchar(50), LastName varchar(50),\
         DateOfBirth varchar(50), Email varchar(50), Phone varchar(50), Address varchar(50))'
curs.execute(tab_q)
query = 'INSERT INTO student(StudentID, FirstName, LastName, DateOfBirth, Email, Phone, Address)\
         VALUES (%s, %s, %s, %s, %s, %s, %s)'
for r in range(1, sheet.nrows):
    StudentID = sheet.cell(r, 0).value
    FirstName = sheet.cell(r, 1).value
    LastName = sheet.cell(r, 2).value
    DateOfBirth = sheet.cell(r, 3).value
    Email = sheet.cell(r, 4).value
    Phone = sheet.cell(r, 5).value
    Address = sheet.cell(r, 6).value
    values = (StudentID, FirstName, LastName, DateOfBirth, Email, Phone, Address)
    curs.execute(query, values)
db.commit()
print(f'Successfully inserted {sheet.nrows} rows and {sheet.ncols} columns into the student table!')
query = 'SELECT * FROM student'
curs.execute(query)
details = curs.fetchall()
print(f'STUDENT DETAILS:\nStudent ID, First Name, Last Name, Date of Birth, Email, Phone, Address\n{"-" * 71}')
for detail in details:
    print(detail)
query = "SELECT StudentID, FirstName, Address FROM student WHERE address LIKE '%deepak%'"
curs.execute(query)
students = curs.fetchall()
print('DETAILS OF STUDENTS WHO ARE FROM deepak')
print(f'Student ID, First Name, Address\n{"-" * 31}')
for student in students:
    print(student)
curs.close()
db.close()
