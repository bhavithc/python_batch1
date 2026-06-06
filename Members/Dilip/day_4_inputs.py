# CODE for getting the vaule via input

print("Please enter the first number")
a =input() # 10
print("Please enter the second number")
b = input() # 20

print("sum of {} and {} is {}".format(a, b, a+b))

##output "sum of 10 and 29 is 1029"

## Converting into an integer

print("Please enter the first number")
a =int(input()) # 10
print("Please enter the second number")
b = int(input()) # 20

print("sum of {} and {} is {}".format(a, b, a+b))

## other way passing the vaule to integer assiginment

print("Please enter the first number")
a =input() # 10
x=int(a)
print("Please enter the second number")
b = input() # 20
y=int(b)

print("sum of {} and {} is {}".format(x, y, y+x))

### another simplied way in signle line converting to integer

a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))

print("sum of {} and {} is {}".format(a, b, a+b))

a = int(input("Please enter the first number: \n"))
b = int(input("Please enter the second number: \n"))

print("sum of {} and {} is {}".format(a, b, a+b))