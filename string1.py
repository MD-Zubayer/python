a = "hello world"
print(a[0])  # h
print(a[2:4])

# multilline string
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

# raw string
c = "raw\nstring"
print(c)

s4 = r"Raw\nString"
print(s4)  # Raw\nString

# indexing and slicing
s1 = "hello world"
print(s1[0])
print(s1[-1])
print(s1[0:5])
print(s1[:7])
print(s1[6:])
# print(s1[-5:-1])
print(s1[::2])
print(s1[::-1])

# simple oparation
# concatenation
a = "                  hello "
b = "world"
c = a + " " + b
print(c)

# repetition
d = a * 3
print(d)

# membership
print("h" in a)
print("x" not in a)

# string methods
# Case
print(a.upper())
b = "HELLO"
print(b.lower())
print(a.title())
print(b.title())
print(b.capitalize())
l = b.casefold()
print(l)
print('heLLo'.swapcase())
print('HEllo'.istitle())

# Boolean Tests
print("abs344".isalnum())
print('hello'.isalpha())
print('32342'.isdigit())
print('hello!'.isascii())
print('23'.isdecimal())
print('-434'.isnumeric())
print('hello'.islower())
print('HELLO'.isupper())
print('\n\t'.isspace())
print('hsks\n'.isprintable())
print('var_1'.isidentifier())







# print(a.strip())
# print(b.replace('L', 'l'))
# print(b.split('L'))
# print("-".join(['2025', '01', '01']))
# s = a.find('hello')
# z = a.index('hello')
# print(s)
# print(z)
# print(b.center(40, '*'))
# print(b.count('L'))