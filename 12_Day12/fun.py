# def sum(a, b, c):
#     print(f"a = {a}, b = {b}, c = {c}")
#     return a + b + c

# print(sum(10, b = 20, c = 30))


# def sum2(*pargs, **kwrgs):
#     print(pargs, kwrgs)

# pargs = (10, 20, 30)

# sum2(10, 20, 30, a = 40, b = 50, c = 40)

import logging
from functools import wraps

logging.basicConfig(
    filename = "ravi.log",
    level = logging.DEBUG,
    format = "%(asctime)s %(levelname)s %(threadName)s %(taskName)s :%(name)s:%(message)s"
)

def log(fun):
    @wraps(fun)
    def wrapper(*pargs, **kwrgs):
        logging.debug(f"{fun.__name__} entered")
        retvalue = fun(*pargs, **kwrgs)
        logging.debug(f"{fun.__name__} exit")
        return retvalue
    return wrapper

@log
def foo():
    print("inside foo")

@log
def sum(a, b):
    print(f"a = {a}, b = {b}")
    return a + b


@log
def bar(a = 100):
    print(a)

@log
def foo():
    print("inside foo")

# sum(b = 10, a = 20)
# foo()
# bar()


print(foo.__name__)

