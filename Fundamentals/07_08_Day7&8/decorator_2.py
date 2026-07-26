import time

def finish_breakfast():
    print("having breakfast....")
    time.sleep(5)
    print("breakfast finished !")

def good_morning():
    print("Good morning")
    finish_breakfast()
    time.sleep(3)
    print("nap done")

def good_night():
    print("Good night")
    time.sleep(1)

# calling directly
# greet_good_morning()

# called using alias 
# c = greet_good_morning
# c()
def calculate_time(function): # fun = good_morning
    print(type(function))
    t1 = time.time() # time 1
    function() # call -> good_morning()
    t2 = time.time() # time 2 
    diff = t2 - t1
    diff = int(diff)
    print(f"function took {diff} seconds")


calculate_time(good_morning)
# print("--" * 20)
# calculate_time(good_night)
