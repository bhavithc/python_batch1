# import dilip, ravi

from dilip import calc

# print("Init is imported")

# from .calc import add

# print(dilip.calc.add(10, 20))
# print(dilip.version)

def add(a, b):
    print("My add function")
    return a + b + 10


print(add(10, 20))

import dis

dis.dis(add)