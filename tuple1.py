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

# remove tuple item
y = list(tuple4)
y.remove('apple')
x = tuple(y)
print(x)
del x

# Unpack Tuples
fruits = ('apple', 'banana', 'cherry')
(grenn, yellow, red) = fruits
print(grenn)
print(yellow)
print(red)

# using asterisk*
number = (1,2,3,4,5,6,7)
(num1, num2, *num3) = number
print(num1)
print(num2)
print(num3)
number2 = (4,5,67,8,8,9)
(num4, *num5, num6) = number2
print(num4)
print(num5)
print(num6)

# Loop throuth a Tuple
str_tuple = ('apple', 'banana', 'cherry')
for x in str_tuple:
    print(x)
# loop through the index numbers
for i in range(len(str_tuple)):
    print(str_tuple[i])

i = 0
while i < len(str_tuple):
    print(str_tuple[i])
    i += 1

# join tow tuple
strnum = number + str_tuple
print(strnum)

# Multiply Tuples
mltpule = str_tuple * 3
print(mltpule)

# list2 = [4,5,6]
# mllist = list2 * 3
# print(mllist)

# Tuple method
tuple10 =  (1,2,3,4,4,4,5,5,6,67)
print(tuple10.count(4))
print(tuple10.index(5))
