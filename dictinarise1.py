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

# Change Value
dic4['name'] = 'abdullah'
print(dic4)

dic4.update({'city': 'borishall'})
print(dic4)
# Removing Items
# The pop() method removes the item with the specified key name:

dic4.pop('color')
print(dic4)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
dic4.popitem()
print(dic4)
# del dic4
dic4.clear()
print(dic4)

# Loop through a dictionary
# get keys
for x in dic3:
    print(x)
for x in dic3.keys():
    print(x)
# get values
for x in dic3:
    print(dic3[x])
for x in dic3.values():
    print(x)
# get keys and values
for x, y in dic3.items():
    print(x, y)
    print(x)
    print(y)

# Copy a dictionary
dict3 = dic3.copy()
print(dict3)

# using dict()
dict4 = dict(dic3)
print(dict4)

#Nested Dictionary
# way 1
myfamily = {
    'child1': {
        'name': 'Emil',
        'age': 22
    },
    'child2': {
        'name': 'ahmad',
        'age': 33
    },
    'child3': {
        'name': 'hasan',
        'age': 44
    }
} 

# way 2
cl1 = {
    'name': 'abdullah',
    'age': 11
}
cl2 = {
    'name': 'shohel',
    'age': 23
}
cl3 = {
    'name': 'ahsan',
    'age': 12
}

myfamily2 = {
    'child4': cl1,
    'child5': cl2,
    'child6': cl3
}

# Access items in Nested dictionary
print(myfamily['child1']['name'])
print(myfamily2['child4']['name'])

# Loop Through Nested dictionary
for x , obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])
for x, obj in myfamily2.items():
    print(x)
    for y in obj:
        print(obj[y])

# dictionary formkeys()
k = ('key1', 'key2', 'key3' )
v = 12
d = dict.fromkeys(k,v)
print(d)
ks = dict.fromkeys(k)
print(ks)
x = d.get('key1')
print(x)
x = d.get('key4', 333)
print(x)

z = d.setdefault('key1', 100)
print(z)
zs = d.setdefault('key4', 1000)
print(zs)