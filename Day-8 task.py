# 1

anime = {'One piece': 'Monkey.D.Luffy', 'AOT': 'Eren', 'Black clover': 'Asta'}
anime2 = {'Mobpsycho100': 'Mob', 'Jujutsu Kaisen': 'Yuji Itadori'}
anime.update(anime2)
print("Merged dictionaries : ", anime)

# 2

list1 = [100, 69, 5584, 1, 32, 55, 5, 62, 15]
list1.sort(reverse=True)
print('Descending order : ', list1)
s = set(list1)
print('list to set : ', s)

# 3

anime = {'One piece': [10, 1, 5], 'AOT': [12, 67, 54, 43],
         'Black clover': 'Asta'}
result = {k: sorted(anime[k]) for k in sorted(anime)}
print('With function:', result)


def function1(wof):
    res = dict()
    for key in sorted(wof):
        res[key] = sorted(wof[key])
    return res


print('Without function:', function1(anime))

# 4


def fun1():
    str1 = input('char_name : ')
    str2 = 'char_name is the strongest !! '
    return str2.replace('char_name', str1)


print(fun1())

# 5

import string
user = input('Enter the string : ')
print(string.capwords(user))

# 6

from collections import Counter
# list_1 = input('enter the list : ')
list_1 = [1, 2, 5, 4, 7, 7, 4, 1, 2, 9, 5, 3, 1, 5, 5, 1, 2]
d = Counter(list_1)
new_l1 = list([item for item in d if d[item] > 1])
print('Repeated items in a list : ', new_l1)

# 7

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))
d = a+b+c
print('Sum of three values : ', d)
user = int(input("Enter the number to divide sum : "))
if d % user == 0:
    print("The given input divide the sum ! ")
else:
    print("The given input does not divide the sum ! ")

# 8


def mean(l1):
    total = 0
    for x in l1:
        total += x
    mean1 = total / len(l1)
    return mean1


def median(l1):
    l1.sort()
    if len(l1) % 2 != 0:
        median1 = l1[int(len(l1) / 2)]
    else:
        median1 = l1[(int(len(l1) / 2)) - 1] + l1[int(len(l1) / 2)]
        median1 = median1 / 2
    return median1


def mode(l1):
    counter = 0
    num = l1[0]
    for i in l1:
        frequency = l1.count(i)
        if frequency > counter:
            counter = frequency
            num = i
        if len(set(l1)) == len(l1):
            return 'There is no MODE'
    return num


number_list = []
while True:
    ask = input('Enter a number and say "stop" to end : ')
    if ask == 'stop':
        break
    number_list.append(int(ask))

mean = str(mean(number_list))
median = str(median(number_list))
mode = str(mode(number_list))

print('Mode : ' + mean + '\n' + 'Median : ' + median + '\n' + 'Mode : '
      + mode)

# 9

s1 = input('enter the text : ')
print('swap case :', s1.swapcase())

# 10

num1 = int(input('Enter a number : '))
print('Int to Binary : ', bin(num1))

num2 = int(input('Enter a number : '))
print('Int to Octa Decimal : ', oct(num2))
