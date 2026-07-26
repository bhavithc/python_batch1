def log(function):
    def wrapper():
        print(f"Enter {function.__name__}")
        function()
        print(f"Exit {function.__name__}")

    return wrapper


@log
def hello():
    print("Hello world")

# wrap = log(hello)
# wrap()

# hello()

print(hello)