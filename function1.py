
# Creating a Function
def my_fun():
    print('hello from a function')

# Calling a Function
my_fun()

# Arguments
def my_fun2(fname):
    print(fname + " " + 'Refsnes')

my_fun2('hasan')
my_fun2('hublu')
my_fun2('abdullah')
# ✅ মনে রাখার সহজ উপায়:
# Parameter = Function কে "কি চায়" সেটা।
# Argument = Function কে "কি দেয়" সেটা।

def my_fun3(fname, lname):
    print(fname + ' ' + lname)

my_fun3('Emil', 'Refsnes')
# erro
# my_fun3('emil')

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:


def my_fun4(*kids):
    print('The youngest child is' + ' '+ kids[1])

my_fun4('hasan', 'ahsan', 'husain')

# Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def my_fun5(child3, child2, child1):
    print('The youngest child is ' + child3)

my_fun5(child1= 'ahmad', child2= 'arham', child3= 'ahsan')

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:

def my_fun6(**kids):
    print('His last name ' + kids['lname'])

my_fun6(fname = 'Md', lname = 'abdullah', user_name = 'Md abdullah')

# Default Parameter Value
def my_fun7(country = 'bangladesh'):
    print('I am from ' + country)

my_fun7('india')
my_fun7()

# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def my_func(food):
    for x in food:
        print(x)

fruits = ['apple',  'banana', 'cherry']
my_func(fruits)

def my_func2(food):
    print(food)
fruits = ['apple', 'banana', 'cherry']
my_func2(fruits)

# Return Values
def my_func3(x):
    return 5 * x

print(my_func3(6))

# The pass Statement
def myFun():
    pass
def myFunc(x):
    print(x)
myFunc(x = 3)

# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:

def my_func4(x, /):
    print(x)

my_func4(4)

# Error
# my_func4(x = 4)

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:

def my_func5(*, x):
    print(x)

my_func5(x = 4)
# Error
# my_func5(66)

# Combine Positional-Only and Keyword-Only
def my_func6(a, b, /, *, c, d):
    print(a + b + c + d)

my_func6(3,4, c =4, d = 5)

# Recursion

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print('Recursion Example Results: ')
tri_recursion(6)

# lambda function
x = lambda a, b : a * b
print(x(2,3))

y = lambda a, b : a + b
print(y(3,6))

x = lambda a, b, c : a + b + c
print(x(4,6,7))
print(x(a=4, b=4, c= 5))

z = lambda *a : a + a
print(z(4,6,7,7,7,7,7))

y = lambda a, /, *, b : a * b
print(y(4, b=7))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def my_func(n):
    return lambda a : a + n

my_doubler = my_func(9)
print(my_doubler(56))

