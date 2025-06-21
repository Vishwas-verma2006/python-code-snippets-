a = ["vishwas","Verma","sandesh","Neha",123,12.63,False] 
print(a[::-1])

By reverse() function of list 
a = ["vishwas","Verma","sandesh","Neha",123,12.63,False] 
a.reverse()
print(a)

program list comperhension 
# same name of data with same name list 
name = ["Vishwas","nikhil","nandni","Krish","Krishna","rishi"]
v = [word for word in name if word.startswith("V")]
n = [word for word in name if word.startswith("n")]
K = [word for word in name if word.startswith("K")]
r = [word for word in name if word.startswith("r")]

print("name list = ",name)
print("v list = ",v)
print("n list = ",n)
print("K list = ",K)
print("r list = ",r)

program to divide the name thruogh other variable
name = ["Vishwas","Sandesh","Neha","Rakseh"]
n1,n2,n3,n4=name
print(name)
print(n1)
print(n2)
print(n3)
print(n4)