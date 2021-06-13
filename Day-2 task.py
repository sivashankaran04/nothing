Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> print("30 days 30 hour challenge")
30 days 30 hour challenge
>>> print('30 days 30 hour challenge')
30 days 30 hour challenge
>>> 
>>> hours = "thirty"
>>> print(hours)
thirty
>>> 
>>> days="thirty days"
>>> print(days[0])
t
>>> name="Deepak"
>>> print(name[4])
a
>>> challenge='I will win'
>>> print(challenge[7:10])
win
>>> 
>>> challenge='I will win'
>>> print(len(challenge))
10
>>> 
>>> challenge='I Will Win'
>>> print(challenge.lower())
i will win
>>> 
>>> a='30 days'
>>> b='30 hours'
>>> c=a+b
>>> print(c)
30 days30 hours
>>> 
>>> a='30 days'
>>> b='30 hours'
>>> c=a+" "+b
>>> print(c)
30 days30 hours
>>> a="30 days"
>>> b="30 hours"
>>> c= a+" "+b
>>> print(c)
30 days 30 hours
>>> 
>>> text="thirty days thirty hours"
>>> x=text.casefold()
>>> print(x)
thirty days thirty hours
>>> 
>>> text="thirty days thirty hours"
>>> x=text.capitalize()
>>> print(x)
Thirty days thirty hours
>>> 
>>> text="thirty days thirty hours"
>>> x=text.find()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    x=text.find()
TypeError: find() takes at least 1 argument (0 given)
>>> x=text.find(days)
>>> print(x)
0
>>> x=text.find(thirty)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    x=text.find(thirty)
NameError: name 'thirty' is not defined
>>> 
>>> text="thirty days thirty hours"
>>> x=text.isalpha()
>>> print(x)
False
>>> 
>>> text="thirty days thirty hours"
>>> x=text.isalnum()
>>> print(x)
False
>>> 