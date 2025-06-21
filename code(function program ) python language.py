#taking input from user through argument
def name(name1,name2):
    print(f"Helo! {name1},{name2}")

name(input("Enter the name:- ") , input("Enter the name:- "))

example of keyword argument
def name(name1,name2):
    print("Heloo! ",name1,name2)
    
name(name1="Vishwas",name2="Verma")

example of poistional argument
def name(name1,name2):
    print("Hi!",name1,name2)
    
name("Vishwas","Sandesh")

example of default argument
1st 
def name(name1="Vishwas"):
    print("Hi!",name1)
    
name()

2nd 
def name(name1="Vishwas"):
    print("Hi!",name1)
    
name("Sandesh")

example of variable lenth argument 
1stdef test(**arg):
    print(type(arg)) 
    print(len(arg))
    print(arg)
    
test(name1="Vishwas",name2="sandehs",name3="Neha")

2nd 
def test(*arg):
    print(type(arg)) 
    print(len(arg))
    print(arg)
    
test("Vishwas","sandehs","Neha") 

#short program of command line 
from sys import argv 
print(argv)
print(type(argv))

program of calculator by fnctions
def calculator(a,b):
    print("\nAddition:- ",a+b)
    print("Substtraction:- ",a-b)
    print("Multiplication:- ",a*b)
    print("Division:- ",a/b)
    
calculator(a=int(input("Enter the number:-")),b=int(input("Enter the number:- ")))