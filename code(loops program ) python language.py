program to print natural number by [continue]
for num in range(1,11):
    if num == 7:
        continue
    else :
        print(num)

By [break]
for num in range(1,11):
    if num == 6:
        break
    else :
        print(num)
 
program to print 1-5 revers counting 
1st
for num in range(5,0,-1):
    print(num)
print('BOOM\nClyamore !')

2nd 
num = 5
while num > 0:
    print(num)
    num-=1 
print("BOOM\nClyamore !")

program to print natural numbers by while loop
num = 1
print("Natural numbers:-")
while num<=10:
    print(num)
    num += 1

program to print natural numbers by for loop 
print("natural nubers:- ")
for num in range(1,11):
    print(num)
    num +=1

program to print table by using for loop
user = int(input("Enter the number:- "))
print("This is table of ",user)
for num in range(1,11):
    print(user * num)
    
program to unlock phone by using while loop
password = "Vishwas"
upassword = input("Enter the password:- ")
while password != upassword:
    upassword = input("Enter the password:- ")
else :
    print("Phone unlock !\nWelcome") 

program to print whole number
print("Whole number:-")

for _ in range(0,101):
    print(_) 

program to print number from taking user input
a = int(input("Enter the number from which you print the numbers:-")) #starting number
b= int(input("Enter the number the last number:-")) #Ending number

while a<=b:
    print(a)
    a +=1 