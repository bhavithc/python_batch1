name=input("what is your name?")
print(name)
 # first way
print("What is your name")
name = input()

print("What is your age")
age = input()
print(name, age)

 # second way
name = input("What is your name?")
age = input("What is your age ")
print(name, age)


a = int(input("Please enter first number: \n")) 
b = int(input("Please enter second number: \n")) 

print("sum of {} and {} is {}".format(a, b, a + b))
