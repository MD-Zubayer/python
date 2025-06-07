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
print(a.upper())
b = "HELLO"
print(b.lower())
print(a.title())
print(b.title())
print(b.capitalize())
print(a.strip())
print(b.replace('L', 'l'))
print(b.split('L'))
print("-".join(['2025', '01', '01']))
s = a.find('hello')
z = a.index('hello')
l = b.casefold()
print(s)
print(z)
print(l)
print(b.center(40, '*'))
print(b.count('L'))