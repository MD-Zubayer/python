# the list is ordered, changeable, and allow duplicate values   
list1 = ['apple', 'banana', 'cherry']
print(list1)
list2 = [34,5,5,6,7,8,9]
print(list2)
print(len(list1))
lsit3 = [True, False, True]
print(lsit3)
list4 = [4,5, 'apple', 6.7, True]
print(list4)
print(type(list4))
list5 = list((3,4,5,6))
print(list5)
# accessing elements
print(list1[0])
print(list1[-1])
print(list1[1:3])
print(list2[:4])
print(list2[-5:-1])
# cheek if item exists
if 'apple' in list1:
    print('Yes, apple is in the list')
# change list item 
list1[1] = 'orange '
print(list1)
list2[2:-1] = [10, 11, 12,4,5]
print(list2)
# insert item
list1.insert(2,'kiwi')
print(list1)
# append item
list1.append('mango')
print(list1)
list1.append(['pear', 'peach'])
print(list1)
# extend list
list1.extend(list2)
print(list1)
# Remove specified item
list1.remove('apple')
print(list1)
print(len(list1))
# Remove item by index
del list1[0]
print(list1)
print(len(list1))
# Remove specified index
list1.pop(1)
print(list1)
print(len(list1))
# Remove last item
list1.pop()
print(list1)
del list1
# print(list1)  # This will raise an error since list1 is deleted
# Clear the list
list2.clear()
print(list2)   

# Loop through lists
for item in list4:
    print(item)
# Loop through the index numbers
for i in range(len(list4)):
    print(i)
    print(list4[i])
# using a while loop
i = 0
while i < len(list4):
    print(list4[i])
    i += 2
# Looping Using list comprehension
print([x for x in list4 if type(x) == int])
[print(x) for x in list4 ]
[print(x) for x in list5]
# list comprehension 
list6 = [12,3,4,55,6,7,8,8,9,9]
list7 = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
new_list = []
new_list2 = []
for x in list7:
    if 'a' in x:
        new_list.append(x)
print(new_list)

for x in list6:
    if x % 2 == 0:
        new_list.append(x)
print(new_list)

for x in list6:
    if x % 2 != 0:
        new_list2.append(x)
print(new_list2)

new_list3 = [x for x in list7 if 'b' in x]
print(new_list3)

new_list4 = [x for x in list6 if x <15]
print(new_list4)

# unpack
[print(x) for x in list6 if x < 9]

# the syntax of list comprehention
# newlist = expression for item in iterable if condition == True
newlist = [x for x in range(10)]
print(newlist)
newlist2 = [x for x in range(10) if x > 5]
print(new_list2)

newlist3 = [x.upper() for x in list7]
print(newlist3)


newlist4 = [x if x != 'apple' else 'banana' for x in list7]
print(newlist4)

# sort lists
list6.sort()
print(list6)
list6.sort(reverse=True)
print(list6)
list6.reverse()
print(list6)

list7.sort(reverse=True)
print(list7)

# Customize Sort Function


# copy lists
# using copy()
mylist = list6.copy()
print(mylist)

# using list()
mylist2 = list(list7)
print(mylist2)

# using slice operator
mylist3 = list7[:]
print(mylist3)

# join lists
joinlist = list6 + list7
print(joinlist)

# another way
for x in list7:
    list6.append(x)
print(list6)

list8 = [344,4,5,4,4]
list9 = [5,9,5,3,2]
list8.extend(list9)
print(list8)

# count
print(list8.count(4))

# 🧠 List Comprehension 
# 🆚 Traditional vs List Comprehension:
# ✅ Traditional way:
numbers = [1,2,3,4,5]
squares = []

for num in numbers:
    squares.append(num ** 2)

print(squares)

# ✅ List Comprehension way:
# 🧱 Syntax (গঠন):
# [expression for item in iterable if condition]


numbers2 = [1,2,3,4,5]
squares2 = [num ** 2 for num in numbers2]
print(squares2)

# double  numbers by list comprehension

nums = [1,2,3,4,5]
doubled = [x * 2 for x in nums]
print(doubled)

# print  only even number
nums = [1,2,3,4,5,6,7]
even = [x for x in nums if x % 2 == 0]
print(even)

# print length of words
words = ['apple', 'banana', 'cherry']
lengths = [len(word) for word in words]
print(lengths)
clapitalized = [word.upper() for word in words]
print(clapitalized)



# 🔥 Challenge time! (Quiz)
print([x for x in range(10) if x % 3 == 0])

# 🧪 Practice time:
# print only odd numbers
print([x for x in range(10) if x  % 2 != 0])




