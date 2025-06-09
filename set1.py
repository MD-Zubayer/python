# unordered, unchangeable, duplicates not allow

set1 = {2.34,5,6,7,8,9}
print(set1)
set2 = {1,2,3,4,'apple', 'banana', True, False}
print(set2)
set3 = {False, True, 0,1}
print(set3)
print(len(set3))
set4 = set((2,2,3,4,5,6))
print(set4)

txt = '''There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''
split_word = txt.split(' ') 
set_split = set(split_word)
print(set_split)

# Access items
for x in set4:
    print(x)
print(3 in set4)
print(4 not in set4)

# add set items
# using add()
set4.add(9)
print(set4)

# using update()
set3.update(set4)
print(set3)
# if the item remove dose not exits, will raise an error
set3.remove(True)
print(set3)

# if the item remove dose not exits, will Not raise an error
set3.discard(2)
print(set3)
set3.pop()
print(set3)
print(set3.clear())
del set3
 

# Loop sets
set5 = {3,4,5,6,7,8,9, 10,11}
for x in set5:
    print(x)

# Join sets
# using union() & upsate()
set6 = {'apple', 'banana'}
print(set6.union(set5))
print(set5 | set6)

# join mutiple sets
set7 = {9,10,1,11,22,33,44,55,66}
set8 = {'cherry','mango', 'apple'}
print(set5.union(set6,set7,set8))
print(set5|set6|set7|set8)
# join a set and tuple
t = (1,2,3,33,44,55)
print(set7.union(t))
z = set7.union(t)
print(type(z))
n = set6.union({'mobail', 'laptop'})
print(n)
# Update
# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.
set6.update(set7)
print(set6)
# 
# Intersection
# Keep ONLY the duplicates
# 
# The intersection() method will return a new set, that only contains the items that are present in both sets.
# 
# Example
# Join set1 and set2, but keep only the duplicates:
print(set7.intersection(t))
# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.
x = set7 & set5
print(x)

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set
set6.intersection_update(set8)
print(set6)

# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

# You can use the - operator instead of the difference() method, and you will get the same result.
# Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.
set3 = set1 - set2
print(set3)

# The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set
set1.difference_update(set2)
print(set1)

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
# Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.
set4 = set1 ^ set2
print(set4)

# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

set1.symmetric_difference_update(set2)
print(set1)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1 ^= set2
print(set1)

set3 = set2.copy()
print(set3)
set3.add('kiwi')
print(set3)
set3.clear()
print(set3)