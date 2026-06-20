
# a = 100


# def add():
    # a = 100
    # b = 20
    # return a + b


# def print_madappa(name): # name = "Ravi Raj"
#     # name = "Ravi Raj"
#     print(name)


# def foo():
#     a = 10


# def add (a, b):
#     return a + b

# a = 10
# b = 20
# sum = add(a, b)


# print_madappa("Ravi Raj")

a = 20 # 0x10 -> 0x20
print(id(a)) # 0x10

def foo():
    global a 
    a = 10 # 0x20
    print(id(a))
    print(a)


foo()
print(a) 
print(id(a)) # 0x20
