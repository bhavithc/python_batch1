#Introduction to Scopes and Function
# In pyhthon how to write a function we need ti say def - here def means define
# and we need to give any name for the function example add
# and this is the () parameter of the function.
#example: def add ()

def add (a , b):
    return a + b

def printname(name):
    print(name)

print(add(10, 20))
printname("Ravi Raj")



a = 10
print(id(a))

def foo():
    global a
    a = 20
    print(id(a))
    print(a)

foo()
print(id(a))
print(a)
