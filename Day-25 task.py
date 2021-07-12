
# 1. Write a Python program to convert a string to datetime

from datetime import datetime

date_string = "Aug 28 2021 8:15AM"
print('String : ', date_string)
D = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print('String to datetime : ', D)

# 2.Write a Python program to subtract five days (last working day) from current date

from datetime import date, timedelta

dt = date.today() - timedelta(5)
print('Current Date :', date.today())
print('5 days before Current Date  is :', dt)

# 3.Write a Python program to convert the date to datetime using a function

from datetime import datetime

delta = date.today()
print(datetime.combine(delta, datetime.max.time()))

# 4. Write a Python program to print next 7 days (week) starting from today

import datetime

base = datetime.datetime.today()
for x in range(0, 7):
    print(base + datetime.timedelta(days=x))
