import sys
a=10
b=10
print(id(a))
print(id(b))


def add(a,b):
    return a+b
    
print(sys.refcount(a))

a=10
a='name'
print(a)

