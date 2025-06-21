program to read the data from the file
f = open("num.txt","r")
data = f.read()
print(data)
f.close()
    
program to write in a file 
st = input("Enter :- ")
fi = open("num.txt","w")
Write = fi.write(st)
print(f"You Write '{st}'")
print("Write sucessfully !")
fi.close()

# append() Mode to add the data on the file 
st = input("Enter any string:- ")
f = open("num file.txt","a") # to add some data on last on the file 
wr = f.write(st)
print("data has written sucesssfylly !")
f.close()

# with statemnt (donot need to write close() function in code)  
with open("num file.txt") as f:
    print(f.read())

# readlines()
f = open("num file.txt")
line = f.readlines()
print(line,type(line))
f.close()

#readline()
f =open("num file.txt")
l1 = f.readline() # the starting line will be print
print(l1)

l2 = f.readline() 
print(l2,type(l2))

l3 = f.readline() 
print(l3)

l4 = f.readline() 
print(l4)

l5 = f.readline()
print(l5)

f.close()

# readline() with loop 
f = open("num file.txt")
line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()


    
# program to edit the data of file 
# this will work when some data is in the file 
with open("example.txt","r") as f:
    lines = f.readlines()
    print('That is data!\n')
    for i , line in enumerate(lines,start = 1):
        print(f"{i}. {line.strip()}")
        
    edit = int(input("Enter the line that you want to edit:- "))-1
    
    if 0 <= edit < len(lines):
        new_data = input("Enter the new data:- ")
        lines[edit] = new_data + '\n'
    else :
        print("invalid number of line !")
        
with open("example.txt","w") as f:
    f.writelines(lines)



#program of edit file if you want to add data on the file and after edit to it so use this 
with open("example.txt","w") as f:
    st = input("Enter the data:- ")
    f.write(st)
    
with open("example.txt","a") as f:
    while True :
        st = input("Enter the data or exit:- ")
        if st.lower() == "exit":
            break
        else:
            f.write('\n'+st)

with open("example.txt","r") as f:
    lines = f.readlines()
    print('That is data!\n')
    for i , line in enumerate(lines,start = 1):
        print(f"{i}. {line.strip()}")
        
    edit = int(input("Enter the line that you want to edit:- "))-1
    
    if 0 <= edit < len(lines):
        new_data = input("Enter the new data:- ")
        lines[edit] = new_data + '\n'
    else :
        print("invalid number of line !")
        
with open("example.txt","w") as f:
    f.writelines(lines)


        
#program of edit file with loop and also fill the data 
with open("example.txt","w") as f:
    st = input("Enter the data:- ")
    f.write(st)
    
with open("example.txt","a") as f:
    while True :
        st = input("Enter the data or exit:- ")
        if st.lower() == "exit":
            break
        else:
            f.write('\n'+st)

with open("example.txt","r") as f:
    lines = f.readlines()
    print('That is data!\n')
    for i , line in enumerate(lines,start = 1):
        print(f"{i}. {line.strip()}")
    
    while True:
        edit = input("Enter the line that you want to edit or 'done':- ")
        if edit.lower() == "done":
            break
        
        try:
            edit = int(edit)-1
            if 0 <= edit < len(lines):
                new_data = input(f"Enter the new data for line number {edit +1}:- ")
                lines[edit] = new_data + '\n'
            else :
                print("invalid number of line !")
        
        except ValueError:
            print("Please enter the valod number of line or done !")
            
            
with open("example.txt","w") as f:
    f.writelines(lines)
    print("\nData has been edit !")
    
    
    