program of even and odd by using if-else condition
user = int(input("Enter the number:- "))

if user % 2 == 0: 
    print("Number is even")
else :
    print("Number is odd")

program to find number is even and odd by another method 

num = int(input("Enter the number:- "))

print("even" if num % 2==0 else "odd")

program to print 1 to 10 even number
for num in range(1,11):
    if num % 2==0:
        print(num)

By while to print even number
num =2 
while num <=10:
    if num % 2==0:
        print(num)
    num +=1

program of odd number by while loop
num = 1
while num<=10:
    if num % 2!=0:
        print(num)
    num +=1
By for loop
for num in range(1,11):
    if num %2 !=0:
        print(num)

program of even and odd numbers 
num = int(input("Enter the number:- "))
print(f"Even number from 1 to {num} is:-")
for i in range(1,num):
    if i % 2 == 0:
        
        print(i)
