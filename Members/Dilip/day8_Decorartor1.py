# This learning for Decorator

#  Let assume two function foo and bar.
def foo():
    print("inside foo")

def bar():

    print("inside bar")

foo()

#Let assume we will insert the log, Enter and exit log for function, In the below case if was want to call any other function
#i need to call it again like bar entered and bar exit.
def foo():
    print("INFO: foo Entered")
    print("inside foo")
    print("INFO: foo Exit")
def bar():

    print("inside bar")

foo()

# To elminate multiple log function we can go with wrapper function call.

def foo():
    print("inside foo")
    

def bar():

    print("inside bar")

def red():

    print("enter red")

def wrapper(func):
    print("INFO: Entered")
    func()
    print("INFO: IExit")

wrapper(foo)
wrapper(bar)
wrapper(red)