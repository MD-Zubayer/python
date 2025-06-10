dic1 = {
    'brand': 'Ford',
    'model': 'mustang',
    'year' : 1933
}
print(dic1)
print(type(dic1))
print(dic1['brand'])
print(dic1['model'])
print(dic1['year'])

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# changeable, duplicate not allow
dic2 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1933,
    'year': 2000
}
print(dic1)
print(len(dic2))

# dictionary item types
dic3 = {
    'brand': 'Ford',
    'electric': False,
    'year': 2000,
    'colors': ['red', 'white', 'blue']
}
print(dic3)
print(dic3['colors'])

dic4 = dict(name = 'hasan', age = 23, country = 'Bangladesh')
print(dic4)
# get keys
x = dic4.keys()
print(x)
dic4['city'] = 'Dhaka'
print(x)

# get valus
z = dic4.values()
print(z)
dic4['age'] = 33
print(z)
dic4['color'] = 'white'
print(z)
y = dic4.items()
print(y)

# check if key Exists
if 'name' in dic4:
    print('Yes, "name" is one of the keys in the dic4 dictionary')
    