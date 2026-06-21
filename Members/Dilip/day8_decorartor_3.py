# Write a code for greeting the good morning using functions

def gm_message():
    print(" Hello Good Morning ")

# calling Directly function
gm_message()

#Calling using Alias
c = gm_message
c()

############
## We will call Time module here are write the code when they message passes, Module will be thought in later classes.\
# as of now just import time.
# Once you import the time module to get the current time you need to use the command time.time() this will give current time
import time
time.time()
print(time.time())

def gm_message():
    time.sleep(5)
    print(" Hello Good Morning ")

def calculate_time(fun):   # here fun is holding function "gm_message".
    t1=time.time() # Time 1
    fun()                  #Call --> function "gm_message()".
    t2=time.time() # Time 2
    Diff = t2 - t1
    print(f" function took {Diff} Seconds ")

calculate_time(gm_message)

### Same can you write for good morning and good night


import time

def gm_message():
    time.sleep(5)
    print(" Hello Good Morning ")

def gn_message():
    time.sleep(5)
    print(" Hello Good Night ")

# Below is defiened as the wrapper function when ever needed we have called

def calculate_time(fun):   # here fun is holding function "gm_message/gn_message".
    t1=time.time() # Time 1
    fun()                  #Call --> function "gm_message()/gn_message()".
    t2=time.time() # Time 2
    Diff = t2 - t1
    print(f" function took {Diff} Seconds ")

calculate_time(gm_message)
print("-"*20)   #  This is just to differenciate between two function
calculate_time(gn_message)





