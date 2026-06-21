#Ternary Operator
# we cant use elif in the ternart operator
# x if condition else y
#Will write a script for even or odd number
    
a = int(input("enter the number: "))

b = True if a % 2 == 0 else False

if b:
    print(f'{a} is even')
else:
    print(f'{a} is odd')


# 