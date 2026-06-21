#1
number=int(input("Enter the number in the range 1-100 \n"))
for i in range(1,number+1):
    if i%3==0 and i%5==0 :
        print(f"FizzBuzz {i}") 
    elif i%3==0:
        print(f"Fizz  {i}")
    elif i%5==0: 
         print(f"Buzz  {i}")
    else:
        print(i)  


#3
#num=int(input("Please enter the number \n"))

for no in range(2,101):
   prime=True
   for i in range(2,no):
       if no%2==0:
        prime=False
        break
if prime:
    print(no)

   

#4
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)

#5
num=[]
for i in range(0,3):
    num=int(input("enter the 3 numbers"))
    print(num)



        
