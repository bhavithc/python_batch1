class SeniorCitizenException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return "I am more than 60"

s = SeniorCitizenException()
print(s)

while True:
    try: 
        age = int(input("Please enter your age? ")) # ValueError
        # age / 0 # Div by zero
        if age < 18:
            print("Teen age")
        # elif age >= 18:
        #     print("You are adult")
        elif age >= 60:
            raise SeniorCitizenException()
        else:
            print("Unknown")
    except ValueError as v:
        print(f"Invalid value entered please try again ! -> {v}")
    except ZeroDivisionError as z:
        print(f"Divide by zero is not allowed something went wrong -> {z}")
    except SeniorCitizenException as s:
        print(f"SeniorCitizenException exception occurred -> {s}")
    except Exception as ex:
        print(f"Exception occurred ! --> {ex}")
    else: # when no exception this block will get executed
        print("No exception")
    finally: # irrespetive of exception occurred or not this block will get executed
        print("This will execute any way")