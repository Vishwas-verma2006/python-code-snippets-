1ts one 
for i in range(1,6):
    
    print("* "*i)

2nd method 
for i in range(1,6):
    for j in range(1,i+1):
        print("* ",end='')
    print()