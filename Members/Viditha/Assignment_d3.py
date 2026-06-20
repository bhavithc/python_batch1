#1
print("What is your name")
name=input()

name=input("What is your name \n")

#2
age = input("what is your age\n")

#3
name = input("Enter your name: \n")

print(f"Hello, {name} Welcome to Python.")

#4
km = float(input("Enter distance in kilometers: "))

miles = km * 0.621371

print("Distance in miles:{}".format(miles) )

#5
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print(f"Area ={area}")
print(f"Perimeter ={perimeter}")

#6
no1 = int(input("Enter first number: "))
no2 = int(input("Enter second number: "))

print("Sum =", no1 + no2)
print("Difference =", no1 - no2)
print("Product =", no1 * no2)

if no2 != 0:
    print("Quotient =", no1 / no2)
else:
    print("Division by zero is not allowed")

#7
bill = int(input("Enter bill amount: "))
tip_percent = int(input("Enter tip percentage: "))

tip_amount = bill * tip_percent / 100
total_amount = bill + tip_amount

print("Tip Amount =", tip_amount)
print("Total Amount to Pay =", total_amount)