def log(function):
    def wrapper():
        print(f"enter inside {function.__name__}")
        function()
        print(f"Exsit {function.__name__}")
    return wrapper    
@log
def hello():
    print("inside the hello")


print(hello)            