# 1
import re
def allcase(text):
    pattern = '^[a-zA-Z0-9]+$'
    match = bool(re.match(pattern, text))
    print(f'{text}: {match}')
print(allcase('Java Programming'))
print(allcase('deepak77'))
print(allcase('python Programming'))
print(allcase('reg 28 ex'))


# 2
def mat(text):
    patterns = '\w*ab.\w*'
    if re.search(patterns, text):
        print(f'{text}:match found!')
    else:
        print(f'{text}:match not found!')
print(mat("Python program"))
print(mat("ababbbabab"))

# 3
def num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False
print(num('My number is 014'))
print(num('aot 05'))
print(num('Hi 6 !'))

# 4
results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
print("Number of length 1 to 3")
for n in results:
    print(n.group(0))

# 5
def uppercase(text):
    pattern = '^[A-Z]+$'
    match = bool(re.match(pattern, text))
    print(f'{text}: {match}')
print(uppercase('PYTHON'))
print(uppercase('Python'))
print(uppercase('deepak'))
print(uppercase('DEEPAK'))
