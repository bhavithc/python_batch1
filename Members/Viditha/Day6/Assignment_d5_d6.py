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
a=int(input("enter the number 1st"))
b=int(input("enter the number 2nd"))
c=int(input("enter the number 3rd"))
largest=0
if a>=b and a>=c:
    largest=a
elif  b>=a and b>=c:
    largest=b
else :
    largest=c
print("largest number:{largest}")    



        
