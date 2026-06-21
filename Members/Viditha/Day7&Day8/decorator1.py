def print_even(Num):
    for i in range(0, Num):
        if i % 2 == 0:
            print(i)


def print_odd(Num):
    for i in range(0, Num):
        if i % 2 != 0:
            print(i)

def foo(nr):
    print("inside foo")
    print(f"nr is {nr}")

def log_and_execute(c, value): # c = print_even, value = 10
    print("enter")
    print(type(c))
    print(type(value))
    c(value) # print_even(10)
    print("exit")

# log_and_execute_alias = log_and_execute
# log_and_execute_alias(10)

# print_even(10)
# print_odd(10)

log_and_execute(print_even, 10)

def pet_animal(a):
    print(f"pet animal {a}")

def wild_animal(b):
    print(f"wild animal {b}")

def func_exce(c,value):
    print(f"inside the functionloop {c}")
    print(type(value))  

    print(f"calling function here {c(value)}") # here pet_animal() dosn't have return statement so it returns NOne .

func_exce(pet_animal,"dog")    

