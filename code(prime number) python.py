program to find number is prime or not
num = int(input("Enter the number:- "))

prime = True

if num <= 1:
    prime = False
else:
    for i in range(2,num):
        if num % i==0:
            prime = False
            break
    	    		
if prime == True :
    print(f"{num} is prime !")
else:
    print(f"{num} is not prime !")

program to print 1 to 10 prime numbers 
print("prime numebers between 1 to 10 is:-")
for num in range(1,11):
    prime = True
    
    for i in range(2,num):
        if num % i==0:
            prime = False
            break
    if prime == True:
        print(num)

program to print 1st 10 prime numbers 
print("prime numebers between 1 to 10 is:-")
count = 0
num = 2
print("Prime numbers between 1 to 10 is:- ")
while count <10:
    prime = True
    
    for i in range(2,num):
        if num %i==0:
            prime = False
            break

    if prime == True:
        print(num)
        count +=1
    num +=1

program to print prime numbers
num = int(input("Enter the numeber:- "))        
print(f"Prime number from 1 to {num}")

for a in range(1,num):
    prime = True
    
    for i in range(2,a):
        if a % i == 0:
            prime = False
            break
   
    if prime == True:
        print(a)