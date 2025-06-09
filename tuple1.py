# Ordered, unchangeable, allow duplicates
tuple1 = (4,5,6,7)
print(tuple1)
print(type(tuple1))

tuple2 = (3,3,4,5,6,6,7,8)
print(tuple2)

print(len(tuple2))
tuple3 = ('apple',)
print(tuple3)
print(type(tuple3))

tuple4 = (34,5,6,'apple', 'banana', True, False)
print(tuple4)

# use tuple()
tuple5 = tuple((4,5,6,7))
print(tuple5)

# access tuple items
print(tuple1[0])
print(tuple2[-2])
print(tuple2[2:6])
print(tuple2[:-1])

# check if item exists
if 'apple' in tuple4:
    print('Yes, apple is in the tuple4')

# update tupe value
# change tuple values
x = (4,5,6,7)
y = list(x)
y[1] = 8
x = tuple(y)
print(x)

y = list(x)
y.append(10)
x = tuple(y)
print(x)

