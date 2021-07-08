# Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.

a = ('Deepak', 'Akkilan', 'Shiva', 'Balaji')
b = ('BSC-CS, MCA', 'BCA, MCA', 'BCA, MCA', 'BCA, MCA')
z = list(zip(a, b))
print(z)

# First create a range from 1 to 8.Then using zip, merge the given list and the range together to create a new list of tuples.

list1 = ['Barath', 'Rajesh', 'Deepak', 'kishore', 'Deepak', 'Akkilan', 'Shiva', 'Balaji']
range1 = list(range(1, 8))
zipped = tuple(zip(list1, range1))
print(zipped)

# Using sorted() function, sort the list in ascending order.

list2 = [9, 8, 7, 4, 6, 2, 1, 3, 5, 8, 1, 6, 13, 4, 64, 61, 46, 16, 4, 1]
print('Ascending Order :', sorted(list2))

# Write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list.

lst1 = [22, 100, 19, 13, 11, 1, 4, 66, 50, 49, 93, 69, 15]
lst2 = list(filter(lambda x: x % 2 == 1, lst1))
print('Odd Numbers :', lst2)
