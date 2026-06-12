# age = int(input("enter age: "))

# if age > 18:
#     print("Adult")
# elif age >= 13:
#     print("Teenager")
# else:
#     print("Child")



age = int(input("Enter the age \n"))

if age <= 0:
    print("Invalid input received, valid input is between 1 and 100")
else:
    if age <= 18:
        if age >= 13:
            print("teenage")
        elif age < 13:
            print("child")
    else:
        print("adult")
