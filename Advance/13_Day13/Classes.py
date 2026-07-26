
class Employee:
    def __init__(s, name, age):
        print("Ctor called")
        print(id(s))
        s.name = name
        s.age = age 

    def foo(s):
        print(s.name)

e1 = Employee("Bhavith", 20)
e2 = Employee("Supreeth", 30)

print(hex(id(e1)))
print(hex(id(e2)))
print(e1.foo)
print(e2.foo)
print(Employee.__dict__)

Employee.foo(e2)


# print(f"name: {e.name}, age: {e.age}")
