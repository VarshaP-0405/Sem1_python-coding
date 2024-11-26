L=[]
L.append(10)
L.append(45)
L.append(1)
L.append(67)
L.append(56)
print("the original list is",L)
L.sort()
print("the sorted list is",L)
L.reverse()
print("the sorted list in decending is",L)

print("2nd output")
s={10,20,30,40,90}
s1={10,90,80,77}
set2=s.intersection(s1)
print("the intersection of s and s1 is",set2)
set3=s.symmetric_difference(s1)
print("the union of s and s1 is",set3)
print(s)
n=int(input("enter a value to be removed from s"))
s.discard(n)
print(s)

print("3rd output")
t=()
L=list(t)
for i in range(5):
    n=int(input("enter a value to  be added"))
    L.append(n)
num=int(input("enter a value to  be removed"))
L.remove(num)
t=tuple(L)
print(t)

print("4th output")
string="\t\t\t\t\t hi i am varsha.THIS IS MY OUTPUT"
print(string.rindex("S"))
print(string.rfind("S"))
print(string.replace("varsha","Nithyashree"))
print(string.lstrip())

      







