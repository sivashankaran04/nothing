# 1
# Name error
list=12
print(list1)

# Type error
a='123'
a+=123

# Syntax error
for i range(1,10):
    print(i)

# index error
l=[1,2,3,4,5,56,6,7]
for i in range(len(l)):
     print(l[i+1])

# Module not found error
import numpys

# Key error
dict1=dict()
dict1={1:12,11:12,13:14}
print(dict1[23])

# Import error
from math import x

# Value error
int("abc")

# Zero Division Error
100/0

# 2
def calculate():
    try:
        print('+', '-', '*', '/', '%', '**')
        op = input("Select an operator : ")
        print("Enter two numbers : ")
        num_1 = int(input())
        num_2 = int(input())
        if op == '+':
            print(num_1 + num_2)
        elif op == '-':
            print(num_1 - num_2)
        elif op == '*':
            print(num_1 * num_2)
        elif op == '/':
            print(num_1 / num_2)
        elif op == '%':
            print(num_1 % num_2)
        elif op == '**':
            print(num_1 ** num_2)
        else:
            print('Invalid Input')
    except Exception as e:
        print(e)
print(calculate())

# 3
try:
    print(d)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# 5
try:
    x = int(input('enter a number : '))
except:
    print("Invalid value !!")
finally:
    print("You entered is : ", x)
