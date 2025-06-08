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

# search
print('hello'.find('l'))
print('helgljjlo'.rfind('l'))
print('hello'.index('l'))
print('helgljjlo'.rindex('l'))
print('hello'.startswith('he'))
print('hello'.endswith('lo'))
print('a,b,c'.split(','))
print('a,b,c'.rsplit(','))
print('a,b,\nc'.splitlines())

# Trim & align
print('   hello   '.strip())
print('         hello      '.lstrip())
print('             hello                  '.rstrip())
print('hello'.center(20, '*'))
print('hello'.ljust(20, '#'))
print('hello'.rjust(20, '-'))
print('hello'.zfill(10))
print('\thello'.expandtabs(8))

#conversion & Formating
a = 'hello world'
b = a.encode(encoding='utf-8', errors='strict')
d = a.encode(encoding='utf-8', errors='ignore')
c = b.decode()
print(a.encode())
print(b)
print(c)
print(d)
print('Hi {}, age {}'.format('Alice', 30))
print('Hi {name}, age {age}'.format(name='Hasan', age=45))
print('Hi {1}, age {0}'.format(30, 'Alice'))
print('Hi {name}, age {age}'.format_map({'name': 'Hsan', 'age': 33}))

# maketrans(x, y=None, z=None)	translation table তৈরি করে, translate()-এর সাথে ব্যবহারযোগ্য	str.maketrans("ae","12") → {97:49, 101:50}
# translate(table)	maketrans()-এর table অনুযায়ী অক্ষর বদলে দেয়	"apple".translate({97:49}) → "1pple"
table = str.maketrans('abcdeh', '342569')
print(table)
s = 'hello'
print(s.translate(table))
table2 = str.maketrans('', '', 'aeiou')  # remove vowels
print(s.translate(table2))
print(s.translate(table2))
table3 = str.maketrans('sl', '46', 'aeiou')  # replace 's' with '4', 'l' with '6', and remove vowels
print(s.translate(table3))

# partition
n = 'hello-world*python'
m = 'hello world'
print(n.partition('*'))
print(n.rpartition('-'))
print(m.partition('-'))

print(a.strip())
print(b.replace('L', 'l'))
print(b.split('L'))
print("-".join(['2025', '01', '01']))
s = a.find('hello')
z = a.index('hello')
print(s)
print(z)
print(b.center(40, '*'))
print(b.count('L'))