# global variabel
x = 100
def fun():
    print(x)
fun()
def fun2():
    x = 99
    print(x)
fun2()
print(x)

# change the globle variable
def fun3():
    global x
    x = 96
    print(x)

fun3()
print(x)

def fun6():
    a = x
    a += 55
    print(a)
fun6()
# local variable
def fun4():
    a = 40
    print(a)
fun4()
#print(a)  # This will raise an error because 'a' is not defined outside of fun4

# ননলোকাল বা নন-গ্লোবাল ভ্যারিয়েবল (Enclosing/Nonlocal Scope)
# যদি nested (ইনসাইড ইনসাইড) ফাংশন থাকে, তাহলে বাইরের ফাংশনের ভ্যারিয়েবলই “enclosing” বা “nonlocal” হয়ে যায়। এসব ভ্যারিয়েবলকে ভিতরের ফাংশন থেকে পরিবর্তন করতে চাইলে nonlocal কীওয়ার্ড দিতে হয়:
def outer():
    a = 10
    def inner():
        nonlocal a
        a += 5
        print("inner a:",a)
    inner()
    print("outer a:",a)

outer()


# the type of variable assinment

# multiple assignment
a, b, c = 1, 2, 3

x = y = z = 100

# type checking

a = 5
b = 4.6
c = "hello"
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>

# type checking with isinstance
print(isinstance(a, int))
print(isinstance(b, float))
print(isinstance(c, int))

# type conversion/casting
d = '34'
x = float(a)
y = int(b)
n = int(d)
z = float(d)
j = str(a)
print(x, y, z, n, j)  # 5.0 4 34
print(type(j))


# variable deletion
s = 20
m = 30
print(s)
del s
# print(s)

#নেমস্পেস ও নাম ছায়াছবি (Name Shadowing)
#যদি গ্লোবাল নেমস্পেসে x = 5 থাকে, আর ফাংশনের ভিতরে আবার x = 10 লিখে ফেলি, তাহলে ফাংশনের ভিতরে ঐ গ্লোবাল x আর দেখা যাবে না— ফাংশনের লোকাল x সেই নাম ছায়াছবি (shadow) করে ফেলবে:

z = 5

def fun5():
    z = 10
    print(z)

fun5()
print(z)

# variable Reinitialization
# immutable variable such as int, float, str, tuple can be reinitialized
s =  "hello"
s = s + " world"
print(s)  # hello world
print(id(s))  # id will change because a new string is created

# mutable variable such as list, dict, set can be reinitialized


my_list = [1, 2, 3]
my_list.append(4) # chenged first list

# Good name conventions
total_price = 100
user_age = 30

# Advanced concepts

# গ্লোবাল কনস্ট্যান্ট
# কোডবেসে এমন কিছু ভ্যালু থাকে যা সব জায়গায় অপরিবর্তিত (e.g. API URL, MAX_LIMIT)। এগুলো সাধারণত বড় হাতের অক্ষরে লিখে ফাইলের শীর্ষে রাখা হয়:

API_URL = "https://api.example.com/v1"
MAX_RETRIES = 3


# Type Hinting

age: int = 40
name: str = 'Rahim'
shorce: list[int] = [3,5,6]
