import json
x = '{"Sem_1":98, "Sem_2":97, "Sem_3":97, "Total":292, "Percentage":98.33, "Passed":"True"}'
json.loads(x)

import mysql.connector as msq
db = msq.connect(host='localhost', user='root', password='deepak#$1238220994412', database='json')
curs = db.cursor(buffered=True)

# Creating table - 'student'
std_q = 'CREATE TABLE student(Id int auto_increment primary key, details json)'
curs.execute(std_q)

query = '''insert into student(details) values
        ('{"student":"(Deepak)", "marks":{"Sem_1":98, "Sem_2":97, "Sem_3":97}, 
        "Total":292, "Percentage":98.33, "Passed":"True"}'),
        ('{"student":"(Akkilan)", "marks":{"Sem_1":45, "Sem_2":40, "Sem_3":60}, 
        "Total":145, "Percentage":48.33, "Passed":"False"}'),
        ('{"student":"(Shiva)", "marks":{"Sem_1":82, "Sem_2":76, "Sem_3":85}, 
        "Total":242, "Percentage":80.67, "Passed":"True"}')'''
curs.execute(query)
db.commit()

data = 'SELECT * FROM student'
curs.execute(data)
details = curs.fetchall()
print(f'STUDENT DETAILS:\n{"-"*16}')
for detail in details:
    print(detail)

marks = "select id, details->'$.marks' from student"
curs.execute(marks)
details = curs.fetchall()
print(f'Id, Marks\n{"-"*9}')
for detail in details:
    print(detail)

perc = "select id, details->'$.Percentage' from student"
curs.execute(perc)
details = curs.fetchall()
print(f'Id, Percentage\n{"-"*14}')
for detail in details:
    print(detail)

curs.execute('DROP TABLE student')
curs.close()
db.close()
