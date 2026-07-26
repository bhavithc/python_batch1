
#  x if condition else y


a = int(input("enter the number: "))

# b = False 
# if a % 2 == 0:
#     b = True
# else:
#     b = False


b = False if a % 2 == 0 else True

if b:
    print(f'{a} is an even')
else:
    print(f'{a} is an odd')


# age = int(input("enter age: "))

# if age > 18:
#     print("Adult")
# elif age >= 13:
#     print("Teenager")
# else:
#     print("Child")



age = int(input("enter age: "))

print("Adult") if age > 18 else print("Child")




