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