import sys
class MyResource:

    def __init__(self):
        print("MyResource created")

    def __del__(self):
        print("Myresource Deleted")

    def __enter__(self):
        print("Resource entered")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("Resource release")

    def foo(self):
        print("foo")

# with MyResource() as resource:
#     resource.foo()


# In heritance 

class Test (MyResource):
    def __init__(self):
        super().__init__()
        print("Test init")

    def __del__(self):
        print("Test deleted")
        return super().__del__()


test = Test()
print("Hello")
test1 = test
del test
print(sys.getrefcount(test1))

# del test