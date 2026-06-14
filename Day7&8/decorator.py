def print_even(max_nr_of_items):
    for i in range(0, max_nr_of_items):
        if i % 2 == 0:
            print(i)


def print_odd(max_nr_of_items):
    for i in range(0, max_nr_of_items):
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


