#Just will write some functions and use anotation and doc and name
def add(a: int, b: int) -> int:
    "Add Function"
    return a + b

#print (dir(add))
print(add.__annotations__)
print(add.__doc__)
print(add.__name__)