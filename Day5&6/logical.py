# and, or, not

is_green = False

if not is_green:
    print("It is not green")
else:
    print("It is green")


green = False
red = False
orange = False
a = 10

if is_green and a % 2 == 0 and True and True:
# if green and red and orange:
    print("Traffic light")
else:
    print("Fancy light")


a = 12

if a < 10 and a % 2 == 0 or a == 12:
    print("its a even number")
else:
    print("Invalid value")

