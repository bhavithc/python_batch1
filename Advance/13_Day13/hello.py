class Employee:
    def __init__(self):
        print("Ctor called")
        print(f"self: {hex(id(self))}")
        self.name = "Deepak"
        self.age = 30

    # def __eq__(self, e):
    #     print("eq is called ")

    def __str__(self):
        print("Str is called")
        return f"{self.name} is {self.age} old"

    def __repr__(self):
        print("reptr is called")
        return f"Name: {self.name}, age: {self.age}"

    def print(self):
        print(f"self: {hex(id(self))}")
        print(f"Hello {self.name}")

    def foo(self):
        print("Foo")


# e1.name
# e1.age
e1 = Employee() # Employee.__init__(e1)
print(f"e1: {hex(id(e1))}")
e1.print() # Employee.print(e1)
# Employee.foo(e1) # Employee.foo(e1)
e1.foo() # Employee.foo(e1)

print(e1)
print(repr(e1))




# e2 = Employee()
# print(f"e2: {hex(id(e1))}")

# e1 = e2

# if e1 == e2:
#     print("equal")

# e1.print()


