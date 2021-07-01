# 1
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = []
for i in list1:
    num.append(i + 2)

print('Looped list : ', num)
print()

# 2
for i in range(5):
    for j in range(5-i-1, -1, -1):
        print(j+1, end=" ")
    print()

# 3
def fib(n):
    c = []
    a = 0
    b = 1
    if n < 0:
        print('Incorrect input !!')
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for x in range(2, n):
            c = a+b
            a = b
            b = c
            print(c)


fib(int(input('Enter how many numbers you want get fibonacci series : ')))

# 4
number = int(input('Enter a number : '))


def arms(num1):
    if num1 in range(1, 10):
        return True
    order = len(str(num1))
    sum1 = 0
    original = num1
    while num1 > 0:
        digit = num1 % 10
        sum1 += digit ** order
        num1 = num1 // 10
    if sum1 == original:
        return True
    else:
        return False


if arms(number):
    print(number, 'is a armstrong number')
else:
    print(number, 'is not a armstrong number')

# 5

for i in range(1, 11):
    print('9 *', i, '=', 9*i)

# 6
numb = int(input("Enter a number : "))
if numb >= 0:
    print(numb, 'is a Positive number ')
else:
    print(numb, 'is a Negative number ')

# 7
def ages(days):
    print(f'{days} in age: {days/365} years')
days = int(input('Enter the no of days:'))
print(ages(days))

# 8
import math
def trigonometry(n, m):
    if n == 'sin':
        return math.sin(m)
    elif n == 'cos':
        return math.cos(m)
    elif n == 'tan':
        return math.tan(m)


print(trigonometry('sin', 37))
print(trigonometry('cos', 90))
print(trigonometry('tan', 90))

# 9
def calculate():
    print('+', "," '-', "," '*', "," '/', "," '%', "," '**')
    operation = input("Select an operator :")
    print("Enter two numbers:")
    number1 = int(input('1st number :'))
    number2 = int(input('2nd number :'))
    if operation == '+':
        print('Addition: ', number1 + number2)
    elif operation == '-':
        print('Subtraction: ', number1 - number2)
    elif operation == '*':
        print('Multiplication: ', number1 * number2)
    elif operation == '/':
        print('Division: ', number1 / number2)
    elif operation == '%':
        print('Modulus: ', number1 % number2)
    elif operation == '**':
        print('Exponentiation: ', number1 ** number2)
    else:
        return 'Invalid Input'


print(calculate())
