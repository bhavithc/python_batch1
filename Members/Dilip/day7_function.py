#FUnction various type of code and analysis

# Code1
x = 10

def foo():
    x = 20
    print("Hello")

foo()
print(x)

#Code 2
x = 10

def foo():
    global x
    x = 20
    print("Hello")

foo()
print(x)

# Code 3
x = 10
print(id(x))
def foo():
    global x
    x = 20
    print(id(x))
    print("Hello")

foo()
print(id(x))
print(x)

# Write a code to parameter

def add(a, b):
    return a + b

sum = add(10, 20)
print(sum)

# assignment why the below code is still returing flot value even after integer is defined.

def add(a: int, b:int) -> int:

    print(type(a))
    print(type(b))

    return a + b
sum = add(10.2, 20.3)
print(sum)

#In Python, type hints like a: int, b: int, and -> int are annotations only — 
#They do not enforce types at runtime.
# We passed add(10.2, 20.3) - These are float values, so Python accepts them and assigns:
#a = 10.2   # float
#b = 20.3   # float
#The annotations:
#a: int
#b: int
#-> int
#Python itself does not convert or reject values.

def add(a: int, b: int) -> int:
    print(type(a))
    print(type(b))
    return int(a) + int(b)

sum = add(10.2, 20.3)
print(sum)