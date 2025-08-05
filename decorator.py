# 👉 @property decorator

class MyClass:

    @property
    def something(self):
        return 'Hello'
obj = MyClass()

print(obj.something)

# 🔁 Traditional way vs property way
# 🚫 Without @property:

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2

c = Circle(5)
print(c.area())

# ✅ With @property:

class Circle2:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return 3.1416 * self.radius ** 2

c = Circle2(5)
print(c.area)

# 🛠 Practical Use Case
# ✅ Auto-updated attributes (no setter):

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def full_name(self):
        return f'{self.fname} {self.lname}'

p = Person('junayed', 'nasir')
p.fname = 'hsan'
p.lname = 'ahmad'
print(p.full_name)

# 🎯 @property, @<property>.setter, @<property>.deleter
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise  ValueError("Price can't be negative!")
        self._price = value
    
    @price.deleter
    def price(self):
        print('Price deleted')

        del self._price


p = Product(100)
print(p._price)
p._price = 150
print(p._price)

# 🔐 Advanced Example (Set করা নিষেধ হলে)

class Person2:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

p = Person2('jonayed')
print(p.name)
# p.name = 'nasir'
# print(p.name)

# 🎯 Step-by-step: Getter, Setter, Deleter দিয়ে একই name property কন্ট্রোল করা

class Person3:
    def  __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Getting name.....')
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name.....')
        if len(value) < 3:
            raise ValueError('Name must be at least 3 characters! ')
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name.....')
        del self._name


p = Person3('jonayed')
print(p.name)
p.name = 'nasir'
print(p.name)
del p.name