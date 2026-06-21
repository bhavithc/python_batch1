def set_employee(name = "Deepak", age = 12, role = "SDE "):
    print(f"Hello \'{name}\' your age is \'{age}\' and role is \'{role}\'")



def add(a, b):
    print("inside add 1")
    return a + b

print(type(add))
temp = add

def add(a, b):
    print("inside add 2")
    return a + b


print(temp)
print(type(add))    

