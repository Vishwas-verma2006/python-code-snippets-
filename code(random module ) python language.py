program of randon password genrator 

import random 

char = "asdffghjklopiuytrewqzxcvbnm123@"
lenght = int(input("Enter the lenght of password:- "))
password = ""
for i in range(0,lenght):
    password += random.choice(char)
    
print(password)

program of random joke genrator 

import random 

jokes = ["Why is a football stadium always cold? It has lots of fans!",
        "What did one math book say to the other? 'I've got so many problems.",
        "What do you call two bananas on the floor? Slippers.",
        "What do kids play when their mom is using the phone? Bored games.",
        " What's the smartest insect? A spelling bee!",
        "How does the ocean say hi? It waves!"]

h = random.choice(jokes)
print(h)


program of password genrator with your name 
import random 
chars = "123456789"   # you can use this also - "qwertyuioplkjhgfdsazxcvbnm!#$%0987654321"
lenght = int(input("Enter the lenght of your password:- "))
password = "Vishwas@"

for i in range(0,lenght):
    password += random.choice(chars)
    
print(password) 

