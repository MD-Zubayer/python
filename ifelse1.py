a = 33
b = 33
if b > a:
    print('b is greater then a')
elif a ==b:
    print('a and b are equle')

a = 200
b = 33
if b > a:
    print('b is greater then a')
elif a == b:
    print('a & b are equle')
else:
    print("a is greater then b")


# Short Hand if
if a > b: print('a is preater then b')

a = 2
b = 330
print('A') if a > b else print('B')

x = 3
y = 10 
if x < y: print('x is smaller then y')
print('X') if x < y else print('Y')

a = 44
b =44
print('A') if a > b else print('=') if a == b else print('B')

# and keyword

a = 200
b = 33
c = 500
if a> b and c > b:
    print('Both conditions are True')

if a > b or a > c:
    print('At least one of the conditions is True')    

if not a < b:
    print('a is not smaller then b')

x = 41
if x > 10:
    print('Above ten,')
    if x > 20:
        print('and also above 20!')
    else:
        print('But not above 20.')

# the pass statement
if a > b:
    pass