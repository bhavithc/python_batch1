import time 

def log(function):
    def wrapper():
        print(f"{function.__name__} enter")
        function()
        print(f"{function.__name__} exit")
    return wrapper


def calculate_time(function): # fun = good_morning
    def wrapper():    
        t1 = time.time() # time 1
        function() # call -> good_morning()
        t2 = time.time() # time 2 
        diff = t2 - t1
        diff = int(diff)
        print(f"function took {diff} seconds")
    return wrapper


"""
Decorator Dilip
"""
def dilip_decorator(fun_name):
    def dilip_wrapper():
        fun_name()
    return dilip_wrapper

@dilip_decorator
def other_function():
    pass

other_function()


@log
def foo():
    print("inside foo")

# c = log(foo)
# c()

foo()


# @dilip_decorator
# def bar():
#     print("inside bar")
#     time.sleep(1)


# bar()