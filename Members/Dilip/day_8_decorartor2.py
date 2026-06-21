# Lets write the code for even numbers with in the provided range.
def print_even(max_no_of_items):
    for i in range(0, max_no_of_items):
        if i % 2 == 0:
            print(i)

print_even(20)



# Lets write the code for even and odd numbers with in the provided range.

def print_even(max_no_of_items):
    for i in range(0, max_no_of_items):
        if i % 2 == 0:
            print(i)

def print_odd(max_no_of_items):
    for i in range(0, max_no_of_items):
        if i % 2 == 0:
            print(i)



print_even(10)
print("-"*20)
print_odd(10)

#########################################################cls#############

# Lets write the code for even and odd numbers with in the provided range and also provide the logs like enter and exit for functions
# Need to use the decorator to call the logs.

def print_even(max_no_of_items):
    for i in range(0, max_no_of_items):
        if i % 2 == 0:
            print(i)

def print_odd(max_no_of_items):
    for i in range(0, max_no_of_items):
        if i % 2 == 0:
            print(i)

#  we are creating the wrapper function to call the log recorder when ever needed.

def log(fun, Param):   # Fun = print_even/print_odd , param = 20
    print("Enter the Function")
    fun(Param)      # print_even(10) : Here parameter also to be passed  inside function paramater is passed
    print("Exit the Function")

log(print_even, 20)  # Here we are not calling the function we are passing the function and also we need paramaters to be passed for range so we have taken anothe value param"
log(print_odd, 20)   # Here we are not calling the function we are passing the function and also we need paramaters to be passed for range so we have taken anothe value param"
