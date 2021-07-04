import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="deepak#$1238220994412")
mycursor = mydb.cursor()
db = mydb.cursor()
db.execute("CREATE DATABASE Employee_Management")
db = mydb.cursor()
db.execute("SHOW DATABASES")
for entry in db:
    print(entry)
mydb = mysql.connector.connect(host="localhost", user="root", password="deepak#$1238220994412",
                               database="employee_management")
db = mydb.cursor()
db.execute("CREATE TABLE Employees (EMP_ID INT , EMP_NAME VARCHAR(255),EMP_SALARY DOUBLE )")
db.execute("SHOW TABLES")
for value in db:
    print(value)
db = mydb.cursor()
sql = "INSERT INTO employees (EMP_ID , EMP_NAME , EMP_SALARY) VALUES (%s,%s,%s)"
val = [('1', 'ZORO', '1500000.0'), ('2', 'LUFFY', '15000.0'), ('3', 'SANJI', '70800.0'), ('4', 'DEEPAK', '80000.0'),
       ('5', 'AKKILAN', '89000.0'), ('6', 'BARATH', '50000.0'), ('7', 'BALAJI', '56000.0'), ('8', 'SHIVA', '47000.0'),
       ('9', 'RAJESH', '26000.0'), ('10', 'KISHORE', '15000.0'), ('11', 'DEEPAK', '50500.0'), ('12', 'DHARANI DHARAN', '40500.0'),
       ('13', 'HEMA PRAKASH', '25000.0'), ('14', 'PREM', '20500.0'), ('15', 'RAJ', '10000.0')]
db.executemany(sql, val)
mydb.commit()
print(db.rowcount, "was inserted.")

# a. Write a query to get the maximum and minimum salary from employees table

mycursor = mydb.cursor()
mycursor.execute("SELECT EMP_NAME,EMP_SALARY FROM employees where EMP_SALARY = (select max(EMP_SALARY) from employees)")
result = mycursor.fetchall()
for x in result:
    print(x)
mycursor.execute("SELECT EMP_NAME,EMP_SALARY FROM employees where EMP_SALARY = (select min(EMP_SALARY) from employees)")
result = mycursor.fetchall()
for x in result:
    print(x)

# b. Write a query to get the number of employees working with the company

mycursor = mydb.cursor()
mycursor.execute("SELECT COUNT(*) from employees")
res = mycursor.fetchall()
for x in res:
    print(x)

# c. Write a query to get the first 3 characters of first name from employees table

mycursor = mydb.cursor()
mycursor.execute("SELECT * from employees WHERE EMP_NAME LIKE('DEE%')")
result = mycursor.fetchall()
for x in result:
    print(x)
