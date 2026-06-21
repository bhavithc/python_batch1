#logical operatror discussion and behaviour

is_green = True

if not is_green:
    print("it is not green")
else:
    print("it is green")    



green = True
red = False
orange = True

if green and red and orange:

    print("Traffic light")

else:

    print("Fancy Light") 


if green or red or orange:

    print("Traffic light")

else:

    print("Fancy Light") 


a = int(input("enter the number: "))

if a < 10 and a % 2 == 0:
     print("It is number less than 10 and also even")
else:
    print("Invalid value")
