# code to compare the age using operator

## 18 and above - adult
## < 18 then Child
## > 13 Teen

#age = 10

#if age > 13:
   # print("teenage")
#elif age > 18:
 #  print("adult")
#else:
#    print("child")

#age = 18
#if age <= 13:
   # print("teenage")
#elif age == 18:
    #print("adult")
#else:
   # print("child")

#age = int(input("Enter the age: \n"))
#if age >= 18:
 #  print("adult")
#elif age >= 13:
 #   print("teenage")
#else:
 #  print("child")


# Defensive program what if age is less than 0 or -1 

age = int(input("Enter the age: \n"))   

if age <= 0:
   print("Invalid input received, Valid input is betweeen 1 to 100")
else:
    if age >= 18:
       print("adult")
    elif age >= 13:
        print("teenage")
    else:
        print("child")

