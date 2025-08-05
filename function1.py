import time
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


# ✅ উদাহরণ ১: *args — অনেক positional argument নেওয়া

def add_all(*args):
    total = 0
    for num in args:
        total += num
    print('Total: ', total)

add_all(1,22,33,44)


# ✅ উদাহরণ ২: **kwargs — অনেক keyword argument নেওয়া

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_info(name='jonayed', age=19, city='Dhaka')

# 🔀 একসাথে *args এবং **kwargs ব্যবহার:

def mix_example(*args, **kwargs):
    print('Positional : ', args)
    print([str(x).split(' ') for x in args])
    print('Keyword :', kwargs)

mix_example(1,2,3,45, name='hasan', age=33)


# 🔁 Function Forwarding with *args and **kwargs

def greet(name, age):
    print(f'Hello {name}, you are  {age} yers  old.')

def caller(*args):
    greet(*args)

caller('junayed', 4)


def show_info(name, city):
    print(f'{name} lives in {city}')

def caller2(**kwargs):
    show_info(**kwargs)

caller2(name='hasan', city='dhaka')


def full_info(name, age, job):
    print(f'{name} is {age} years old and works as  a {job}')

def wrapper(*args, **kwargs):
    full_info(*args, **kwargs)

wrapper('junayed', 44, job='Frontend Developer')

# 🧩 Use Case: Logging Decorator
# ✅ Decorator Function
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"🔁 Calling function: {func.__name__}")
        print(f"📦 Positional args: {args}")
        print(f"🔑 Keyword args: {kwargs}")
        result = func(*args, **kwargs)
        print(f"✅ Result: {result}")
        return result
    return wrapper

@logger
def add2(a, b):
    return a + b

add2(2,3)



def auth_required(func):
    def wrapper3(*args, **kwargs):
        if kwargs.get('user') != 'admin':
            return "⛔ Access Denied"
        return func(*args, **kwargs)
    return wrapper3

@auth_required
def delete_user(user):
    return "🗑 User deleted"

print(delete_user(user='admin'))
print(delete_user(user='admi'))


def my_decorator(func):
    def wrapper4():
        print('🌟 Start')
        func()
        print('✅ End')
        func()
    return wrapper4

@my_decorator
def say_hello():
    print('Hello')

say_hello()

# ✅ Dynamic Decorator with *args, **kwargs

def log_args(func):
    def wrapper5(*args, **kwargs):
        print(f' Args : {args}, Kwargs : {kwargs}')
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper5

@log_args
def add(x, y):
    return x + y

add(5, y=10)

# 🔁 ২. Wrapper — ফাংশনের ভিতরে আরেকটা ফাংশন

def decorator(func):
    def wrapper6(*args, **kwargs):
        print('🔁 Wrapper Start')
        result = func(*args, **kwargs)
        print('🔁 Wrapper End')
        return result
    return wrapper6

@decorator
def sum(*args, **kwargs):
    print(kwargs)
    return [x * 2 for x in args]
    



print(sum(3,4,5,6,7, name='jonayed'))

    
# 🔂 ৩. Callback — ফাংশনকে আর্গুমেন্ট হিসেবে পাঠানো হয়
def greet(name):
    return f'Hello, {name}'

def process(callback):
    return callback('junayed')

# process(greet)
print(process(greet))



def success():
    print("🎉 Successfully saved to database!")

def save_data(data, on_success):
    print(f'Saving : {data}')
    on_success()

save_data('User info, ', success)

# 🧪 Function এর ভিতর Function call করা — Callback:

def task_done():
    print("✔️ Task completed!")

def do_task(callback):
    print('Doing task....')
    callback()

do_task(success)
do_task(task_done)

# 🔥 Practice Challenge
def english(name):
    print(f'Hello, {name}')

def bangla(name):
    print(f'হ্যালো, {name}!')

def greet(name, callback):
    callback(name)

greet('jonayed', english)
greet('জুনায়েদ', bangla)

def Upper(text):
    return text.upper()

def proccess(name,func):
    return func(name)

print(proccess('jonayed',Upper))

# 🧱 ৪. Middleware — একটা ফাংশনের আগে/পরে কিছু কাজ করে দেয়
# 🧪 Simulated Middleware:
def my_middleware(func):
    def wrapper(*args, **kwargs):
        print("🔐 Checking authentication...")
        result = func(*args, **kwargs)
        print("🧹 Cleaning up response...")
        return result
    return wrapper

@my_middleware
def view_profile():
    print("👤 Showing user profile")

view_profile()

# 🎓 Practice Challenge:

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'⏱ Took {end - start:.2f} seconds')
        return result
    return wrapper

# print(time.time())

@timer
def add(*args, **kwargs):
    return f'{args} , {kwargs}'

add(33,4,5,67)

@timer
def sum(a, b):
    return  a + b

sum(3,4)