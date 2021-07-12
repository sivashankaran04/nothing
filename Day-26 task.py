
# Enumerate a python list and try to print the counter with the list value

list1 = ['Deepak', 'Akkilan', 'Shiva', 'Balaji', 'Barath', 'Rajesh', 'Kishore']
print(enumerate(list1))

# converting to list
print(list(enumerate(list1)))

# changing the default counter
print(list(enumerate(list1, start=1)))

# Enumerate a python tuple and try to print the counter with the tuple value

tuple1 = ['Deepak', 'Akkilan', 'Shiva', 'Balaji', 'Barath', 'Rajesh', 'Kishore']
print(enumerate(tuple1))

# converting to tuple
print(tuple(enumerate(tuple1)))

# changing the default counter
print(tuple(enumerate(tuple1, start=10)))
