# x - int 
# y - int 
# Point - x,y 

import sys

class Point:
    def __init__(self, x: int, y: int):
        print("init is called")
        self._x : int = x 
        self._y : int = y
        # open db connection

    def __del__(self):
        print("delete is called")
        # close db connection

    def __enter__(self):
        print("Enter is called ")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("Exit is called")

    def foo(self):
        print("Inside foo")


# p1 = Point(10, 20) # 1

# p2 = p1 # 2
# p3 = p2 # 3 

# print("before delete")
# del p2
# del p3
# del p1
# print("after delete")

# print(sys.getrefcount(p1) - 1) # 4

# delete

print("Before with")
with Point(10, 20) as p1:
    p1.foo()
print("After with")

p1.foo()
print(p1)


# p1 = Point(10, 20)

