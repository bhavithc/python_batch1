# Inner Funcation

#Code1
def foo():
    print("inside foo")
    def bar():
        print("Inside Bar")
    bar()
foo()        

#Code2 bit complex
x = 10
def foo():
    print("inside foo")
    x = 20
    print(x)


    def bar():
        print("Inside Bar")

    bar()
print(x)    
foo()  

#Code 2

x = 10
def foo():
    print("inside foo")
    global x
    x = 20
    print(x)


    def bar():
        print("Inside Bar")

    bar()
print(x)    
foo()
print(x)

# Code 3
def foo():
    print("inside foo")
    global x
    x = 20
    print(x)


    def bar():
        print("Inside Bar")
        x = 30
        print(x)
    bar()

print(x)    
foo()
print(x)

#code 4
def foo():
    print("inside foo")
    global x
    x = 20
    print(x)

    y = 30
    def bar():
        print("Inside Bar")
        nonlocal y
        y = 100
        print(y)
    bar()

print(x)    
foo()
print(x)

# Code 5

x = 10

def one():
    print("one")
    global x
    x = 100
    y = 1000


    def two():
        print("two")
        global x
        x = 200
        nonlocal y
        y = 2000
        
    two()
    print(y)

one()
print(x)


