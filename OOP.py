# Python Classes and Objects
# Create a Class
class MyClass:
    x = 5

# Create Object
p1 = MyClass()
print(p1.x)
print(p1)
print(MyClass())
print(MyClass)

# The __init__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = Person('hsan', 34)
print(p2.name)
print(p2.age)
print(p2)


class Person2:
    def __init__(self, *, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def __str__(self):
        return f" the first name: {self.first_name} and the last name: {self.last_name}"
    
p3 = Person2(fname= 'ahmad', lname= 'shikdar')
print(p3)

# Object Methods

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print(f'Hello! my name is {self.name} and my age is {self.age}')

s1 = Student('mahdi', 44)
s1.hello()

# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:

class student:
    def __init__(sl, name, age):
        sl.name = name
        sl.age = age

    def pr(abc):
        print(f'Hello my name is {abc.name}')

s2 = student('ahsan', 33)
s2.pr()

# Modify Object Properties
s2.name = 'tanjil'
s2.pr()
# Delete Object Properties
del s2.age
# Delete Objects
del s2
# print(s2)

# The pass Statement

class person:
    pass

# Python Inheritance
# Create a Parent Class

class simple_person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(f'First Name: {self.fname} Last Name: {self.lname}')
x = simple_person('abdullah', 'ahmad')
x.print_name()

# Create a Child Class

class std(simple_person):
    pass
y = std('Md', 'jonayed')
y.print_name()

# যখন একটি চাইল্ড ক্লাস (সাবক্লাস) তার প্যারেন্ট ক্লাস (বেস ক্লাস) থেকে ইনহেরিট করে, তখন আপনি চাইল্ড ক্লাসে নিজের __init__() মেথড যোগ করতে পারেন। কিন্তু, __init__() যোগ করলে প্যারেন্ট ক্লাসের __init__() অটোমেটিক কল হয় না!
# ১. super() ব্যবহার না করলে (প্যারেন্টের __init__() ওভাররাইড হয়)
#  add the __init__() function to the child class
class std2(simple_person):
    def __init__(self, first, last, age):
        self.age = age

z = std2('MD', "AHSAN", 55)

# error
# z.print_name()
# print(z.age)

# error
# print(z.fname)
# print(z.lname)


# super() দিয়ে প্যারেন্টের __init__() কল করা (সঠিক উপায়)
class std3(simple_person):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name)
        # self.first_name = first_name
        # self.last_name = last_name
        # self.age = age

s3 = std3('MD', 'AHsan', 44)
s3.print_name()

# old way
class std4(simple_person):
    def __init__(self, fname, lname):
        simple_person.__init__(self, fname, lname)
        self.age = 45
s5 = std4('Mohammd', 'mohsin')
s5.print_name()
print(s5.age)


# 📦 উদাহরণ ১: Parent class এর __init__() call করা

class Parent:
    def __init__(self):
        print('Parent constructor')

class child(Parent):
    def __init__(self):
        super().__init__()
        print('Child constructor')

obj = child()

# 🧪 উদাহরণ ২: Method overriding + super()
class Animal:
    def speak(self):
        print('Animal speaks')

class Dog(Animal):
    def speak(self):
        super().speak()
        print('Dog barks')

d = Dog()
d.speak()

class A:
    def show(self):
        print('A')

class B(A):
    def show(self):
        print('B')
        super().show()

class C(B):
    def show(self):
        print('C')
        super().show()

obj = C()
obj.show()
print(C.__mro__)
# help(C)

# 🧱 Practical Use Case: Parent class এ repeated code avoid করা

class Form:
    @property
    def save(self):
        print('Validating data....')
        print('Saving to database....')

class ContactForm(Form):
    @property
    def save(self):
        print('ContactForm custom save')
        super().save

form = ContactForm()
form.save

# 🧪 Step 1: Callback in Class (Function as argument)
def greet(name):
    print(f'Hello , {name}')

class Gretter:
    def run_callback(self,name, func):
        self.name = name
        func(name)

g = Gretter()
g.run_callback('junayed', greet)

# 🎁 Step 2: Decorator in Class
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Somthing before  method runs')
        result = func(*args, **kwargs)
        print('somthing after method runs')
        return result
    return wrapper

class MyClass:

    @my_decorator
    def show(self):
        print('Inside the method')

obj = MyClass()
obj.show()

# 🔁 Step 3: Wrapper Manually Inside Class Method

class MyClass2:
    def original(self):
        print('original method')

    def wrapper(self):
        print('Before  original')
        self.original()
        print('After original')

obj2 = MyClass2()
obj2.original()
obj2.wrapper()


# 🧰 Step 4: Middleware Like Behavior (Before/After Execution)
# class Middleware:
#     def process(self, func):
#         def wrapper(*args, **kwargs):
#             print('Middleware: Before function')
#             result = func(*args, **kwargs)
#             print('Middleware: After function')
#             return result
#         return wrapper

# class MyService:
#     def __init__(self):
#         self.middleware = Middleware()

#     def run(self):
#         print('Main function runnig')

#     def execute(self):
#         wrapped = self.middleware.process(self.run)
#         wrapped()

# m = MyService()
# m.execute()

class Middleware:
    def process(self, func):
        def wrapper(*args, **kwargs):
            print('Middleware: Befor function')
            result = func(*args, **kwargs)
            print('Middleware: After function')
            return  result
        return wrapper

class Service:
    def __init__(self):
        self.middleware = Middleware()

    def run(self):
        print('Main function runnig')

    def execute(self):
        wrappered = self.middleware.process(self.run)
        wrappered()

m2 = Service()
m2.execute()