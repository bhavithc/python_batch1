class MyException(Exception):
    def __init__(self, *args):
        self.__name = args
        super().__init__(*args)
    def __repr__(self):
        return self.__name
        return super().__repr__()

try:
    # age = int(input("Age:"))
    raise MyException("Bhavith C")
except ValueError:
    print("Not a number")
except ZeroDivisionError:
    print("Div by zero")
except Exception as e:
    print(f"Exception {e}")
else:
    print("No exception")
finally:
    print("Always runs")
