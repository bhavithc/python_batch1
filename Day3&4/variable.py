# integer object then assign a value 10 to it
# ,and a is now points to integer object
# a = 10
# b = 20 # invalid
# b = 30

# print(id(a))
# print(id(b))

import sys

# def add(a, b):
#     temp = a + b
#     temp2 = temp
#     return a + b # temp = a + b


# c = add(10, 20) # add(a = 10, b = 20), c = 30


# name1 = "dilips"
# name2 = "dilips"
# name3 = "dilips"
# name4 = "dilips"

# print(id(name1))
# print(id(name2))

a = 10 # 10 - refcnt 1
b = 10 # 10 - refcnt 2 
b = 20 # 20 - refcnt1, 10 - refcnt 1
c = a + b
print(c)
# print(sys.getrefcount(10221))
