# lambda function that multiplies argument x with argument y

a = lambda x, y: x * y
print('Multiplication of X and Y : ', a(651, 7))

# Python program to create Fibonacci series to n using Lambda

from functools import reduce
n = int(input('Enter the limit : '))
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
print('Fibonacci series : ', fib(n))

# Python program that multiply each number of given list with a given number

list1 = [5, 6, 7, 12, 84, 93, 651]
m = int(input('Enter a number to multiply : '))
z = list(map(lambda v: v*m, list1))
print('multiplied list : ', z)

# Python program to find numbers divisible by 9 from a list of numbers

lit = [27, 99, 47, 23, 65, 81, 18]
print('List :', lit)
div = list(filter(lambda c: (c % 9 == 0), lit))
print('Numbers divided by 9 are : ', div)

# Python program to count the even numbers in a given list of integers

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 99, 88, 77]
even = list(filter(lambda x: x % 2 == 0, l1))
print('Even numbers are : ', even)
print('Count of even numbers : ', len(even))
