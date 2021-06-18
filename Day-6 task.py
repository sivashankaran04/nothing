Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Write a Python script to merge two Python dictionaries
>>> 
>>> anime={'Onepiece':'Monkey.D.Luffy','AOT':'Eren','Blackclover':'Asta'}
>>> anime
{'Onepiece': 'Monkey.D.Luffy', 'AOT': 'Eren', 'Blackclover': 'Asta'}
>>> 
>>> anime2={'Mobpsycho100':'Mob','Jujutsu Kaisen':'Yuji Itadori'}
>>> anime2
{'Mobpsycho100': 'Mob', 'Jujutsu Kaisen': 'Yuji Itadori'}
>>> 
>>> anime.update(anime2)
>>> anime
{'Onepiece': 'Monkey.D.Luffy', 'AOT': 'Eren', 'Blackclover': 'Asta', 'Mobpsycho100': 'Mob', 'Jujutsu Kaisen': 'Yuji Itadori'}
>>> 
>>> # Python program to remove a key from a dictionary
>>> 
>>> del anime['AOT']
>>> anime
{'Onepiece': 'Monkey.D.Luffy', 'Blackclover': 'Asta', 'Mobpsycho100': 'Mob', 'Jujutsu Kaisen': 'Yuji Itadori'}
>>> 
>>> anime.pop('Jujutsu Kaisen')
'Yuji Itadori'
>>> anime
{'Onepiece': 'Monkey.D.Luffy', 'Blackclover': 'Asta', 'Mobpsycho100': 'Mob'}
>>> 
>>> # Python program to map two lists into a dictionary
>>> 
>>> list1=['deepak','akki','shiva','balaji']
>>> list2=[100,100,9,100]
>>> 
>>> dictionary=dict(zip(list1,list2))
>>> dictionary
{'deepak': 100, 'akki': 100, 'shiva': 9, 'balaji': 100}
>>> 
>>> # Python program to find the length of a set
>>> 
>>> sets={'deepak','akki','shiva','balaji'}
>>> print('length of a set:',len(sets))
length of a set: 4
>>> 
>>> # Python program to remove the intersection of a 2nd set from the 1st set
>>> 
>>> set1={1,2,3,5,4,7,8,9,6,468,16}
>>> set2={2,3,16,9,88,55}
>>> print('intersection are:',set1.intersection(set2))
intersection are: {16, 9, 2, 3}
>>> 