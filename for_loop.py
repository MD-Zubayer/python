# For Loops
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

for x in range(len(fruits)):
    print(fruits[x])

# Looping Through a String
for x in 'banana': 
    print(x)

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:


for x in fruits:
    print(x)
    if x == 'banana':
        break

# Exit the loop when x is "banana", but this time the break comes before the print:


for x in fruits:
    if x == 'banana':
        break
    print(x)

# The continue Statement
for x in fruits:
    if x == 'banana':
        continue
    print(x)

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# end value
for x in range(6):
    print(x)
# start & end value
for x in range(2, 6):
    print(x)

# start & end & steep value
for x in range(2, 10, 3):
    print(x)

# Else in For Loop

for x in range(6):
    print(x)
else:
    print('Finally finished')

# Note: The else block will NOT be executed if the loop is stopped by a break statement.

for x in range(6):
    if x == 3: break
    print(x)
else:
    print('Finally finished!')

# Nested Loops
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']
price = [22,33,44]
for x in adj:
    for y in fruits:
        print(x,y)

for x in adj:
    for y in fruits:
        for z in price:
            print(x,y,z)