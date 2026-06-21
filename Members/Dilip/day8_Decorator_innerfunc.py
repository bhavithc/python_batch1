# Here we will used the function inside function and decoarte the previous scernaio

def entry_exit(dilip):

    def wrapper():
        print("WARN: Entered")
        dilip()
        print("WARN : EXIT")
              
    return wrapper

@entry_exit
def foo():
    print("inside foo")

foo()



