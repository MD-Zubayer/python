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
set5 = {3,4,5,6,7,8}
for x in set5:
    print(x)

# Join sets
# using union() & upsate()
set6 = {'apple', 'banana'}
print(set6.union(set5))
print(set5 | set6)

# join mutiple sets
set7 = {9,10,1,11,22,33,44,55,66}
set8 = {'cherry','mango'}
print(set5.union(set6,set7,set8))
print(set5|set6|set7|set8)
# join a set and tuple
t = (1,2,3,33,44,55)
print(set7.union(t))
z = set7.union(t)
print(type(z))

