Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> nums=[11,22,33,44,55,66,77,88,99]
>>> nums
[11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> 
>>> # Add an item in to the list (using function)
>>> nums.append(5423)
>>> nums
[11, 22, 33, 44, 55, 66, 77, 88, 99, 5423]
>>> 
>>>  numb=['deepak','akki','shiva','balaji']
 
SyntaxError: unexpected indent
>>> numb=['deepak','akki','shiva','balaji']
>>> nums.extend(numb)
>>> nums
[11, 22, 33, 44, 55, 66, 77, 88, 99, 5423, 'deepak', 'akki', 'shiva', 'balaji']
>>> 
>>> nums.insert(10,'names')
>>> nums
[11, 22, 33, 44, 55, 66, 77, 88, 99, 5423, 'names', 'deepak', 'akki', 'shiva', 'balaji']
>>> 
>>> # Delete (using function)
>>> 
>>> del nums[4]
>>> nums
[11, 22, 33, 44, 66, 77, 88, 99, 5423, 'names', 'deepak', 'akki', 'shiva', 'balaji']
>>> 
>>> del nums[4:6]
>>> nums
[11, 22, 33, 44, 88, 99, 5423, 'names', 'deepak', 'akki', 'shiva', 'balaji']
>>> 
>>> nums.pop()
'balaji'
>>> 
>>> nums.pop(-4)
'names'
>>> 
>>> nums.remove(99)
>>> nums
[11, 22, 33, 44, 88, 5423, 'deepak', 'akki', 'shiva']
>>> 
>>> #Store the largest number from the list to a variable
>>> 
>>> list=[20,30,400,150,890]
>>> a=max(list)
>>> print('largest number:',a)
largest number: 890
>>> 
>>> b=min(list)
>>> #Store the largest number from the list to a variable
>>> print('Smallest number:',b)
Smallest number: 20
>>> 
>>> #Create a tuple and print the reverse of the created tuple
>>> 
>>> t=(1,2,3,4,5,6,7,8,9,10)
>>> t
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
>>> type(t)
<class 'tuple'>
>>> 
>>> print('tuple in reverse:',t[::-1])
tuple in reverse: (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
>>> 
>>> #Create a tuple and convert tuple into list
>>> 
>>> t=(1,2,3,4,5,6,7,8,9,10)
>>> t
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
>>> 
>>> list=[*t]
>>> print('tuple into list:',list)
tuple into list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> t
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
>>> list
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 