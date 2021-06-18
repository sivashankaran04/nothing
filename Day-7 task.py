a = int(input("Enter the 1st value : "))
b = int(input("Enter the 2nd value : "))
function = input("Enter '+' for addition , '-' for Subration ,'*' for multiplication, '/' for division : ")


def fun(a, b, sign):
    if sign == '+':
        print("Addition of a and b is : ", str(a+b))
    elif sign == '-':
        print("Subraction of a and b is : ", str(a-b))
    elif sign == '*':
        print("Multiplication of a and b is : ", str(a*b))
    elif sign == '/':
        print("Division of a and b is : ", str(a/b))


fun(a, b, function)


def covid(name, temp):
    print('patient name : ', name)
    if temp == '':
        print('Body temprature : 98 degree')
    else:
        print("Body temprature : ", temp, 'degree')


name = input("enter patient name : ")
temp = input('enter body temprature : ')
covid(name, temp)

