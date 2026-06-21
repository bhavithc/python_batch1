# Write a decorator code using log function wrapper
import time

def log(function):
    def wrapper():
        print(f"{function.__name__} entered")
        function()
        print(f"{function.__name__} exit")
    return wrapper


def finish_breakfast():
    print("Having breakfast")
    time.sleep(5)
    print("Breakfast finished")

@log
def Good_morning():
    print("Good Morning")
    finish_breakfast()
    time.sleep(3)
    print("Nap Done")

@log
def Good_night():
    print("Good night")
    time.sleep(3)


Good_morning()
print("-"*20)   #  This is just to differenciate between two function
Good_night()


####### Log function basic understanding using phython syntatical sugar @log

def log(function):
    def wrapper():
        print(f"{function.__name__} entered")
        function()
        print(f"{function.__name__} exit")
    return wrapper

@log
def foo():
    print("inside foo")

# c = log(foo)
# c()

foo()


# Now we will calculate time using wrapper and log function

import time
def log(function):
    def wrapper():
        print(f"{function.__name__} entered")
        function()
        print(f"{function.__name__} exit")
    return wrapper

def calculate_time(function):   # here fun is holding function "gm_message/gn_message".
    def wrapper():
        t1=time.time() # Time 1
        function()                  #Call --> function "gm_message()/gn_message()".
        t2=time.time() # Time 2
        diff = t2 - t1
        diff = int(diff)
        print(f" function took {diff} Seconds ")
    return wrapper


@calculate_time
def bar():
    print("inside bar")
    time.sleep(1)

bar()