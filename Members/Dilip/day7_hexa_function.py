#Hexa address print

def foo():
    print("inside foo")

print(hex(id(foo)))
print(foo)
print(id(foo))

# assigning funcation to a variable and need an o/p for type of a and ID of a and hex a value of a and call funcation?

def foo():
    print("inside foo")

a = foo
print(type(a))
print(id(a))
print(hex(id(a)))
a()

# We can assign a function to a variable and call a function using a assigned variable a example a = foo for calling a()

def foo():
    print("inside foo")
    return 10
a = foo()
print(type(a))

def foo():
    print("inside foo")
    return
a = foo()
print(type(a))

def foo():
    print("inside foo")
    return True
a = foo()
print(type(a))

def foo():
    pass
a = foo()
print(type(a))
