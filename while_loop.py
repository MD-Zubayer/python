i = 1
while i < 6:
    print(i)
    i += 1

# The break Statement
i = 1
while i < 7:
    print(i)
    if i == 3:
        break
    i += 1


# The continue Statement

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

# The else Statement

i = 1 
while i < 6:
    print(i)
    i += 1
else:
    print('i is no loger less then 6')
