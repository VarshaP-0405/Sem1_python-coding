import array as arr
L0=[]
n=int(input("enter how many values to be entered"))
for i in range(n):
 VAL0=int(input("enter values to be added in the array"))
 L0.append(VAL0)
L0.sort()
arr1=arr.array("i",L0)
print(*arr1)
#(or)
import array as arr
L0=[]
L1=[]
L2=[]
n=int(input("enter how many values to be entered"))
for i in range(n):
    VAL0=int(input("enter values to be added in the array"))
    L0.append(VAL0)

for i in L0:
    if i<0:
        L1.append(i)
    else:
        L2.append(i)
print(L1+L2)
#(or)
import array as arr
L0=[]
L1=[]
L2=[]
n=int(input("enter how many values to be entered"))
for i in range(n):
    VAL0=int(input("enter values to be added in the array"))
    L0.append(VAL0)

j=0
for i in range(0,n):
    if (a[i]<0):
        t=a[i]
        a[i]=a[j]
        a[j]=t
        j=j+1
print(a)
########
rows = 4
N=65
for i in range(1, rows + 1):
 for j in range(1, i + 1):
 print(chr(N), end=" ")
 N+=1
 print()
########
for i in range(10,20):
 if i%2==0:
 continue
 print(i)
########
x=3
while(x<=8):
 print(x*10)
 x+=2
 # using for loop
 for i in range(3,9):
     print(x*10)
     x+=2
########
import array as arr
L1=[]
n=int(input("enter how many values to be entered"))
for i in range(n):
 VAL1=int(input("enter values to be added in the array"))
 L1.append(VAL1)
2
UNI=[]
DUP=[]
for j in L1:
 if j not in UNI:
 UNI.append(j)
 else:
 DUP.append(j)
print(*DUP)











      
