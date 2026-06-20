x = 10

# def foo():
#     global x
#     x = 20
#     print(id(x)) #20

# print(id(x)) # 10
# print(x)
# foo()



def one():
    print("one")
    global x
    x = 100
    y = 1000


    def two():
        print("two")
        global x
        x = 200
        global y
        y = 2001
        print(f"two: deepak: y {id(y)}")

    two()
    print(y)

one()
global y
y = 100
print(y)
print(f"outside: deepak: y {id(y)}")
# print(x)

# global y
# print(y)
