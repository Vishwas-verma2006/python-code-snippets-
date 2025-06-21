program to swap two numbers with variable
a = int(input("Enter the first number:- "))
b = int(input("Enter the second number:- "))

print(f"Before swping a:- {a}")
print(f"Before swaping b :- {b}")

c=a
a=b
b=c 
print("\n")
print(f"After swaping a:- {a}")
print(f"After swaping b:- {b}")

program to swap two numbers without variable 
a =int(input("Enter the number:- "))
b =int(input("Enter the number:- "))
print("Before swaping a ",a)
print("Before swaping b ",b)
a=a-b
b=a+b 
a=b-a

print(f"\nAfter swaping a",a)
print(f"After swaping b",b)
