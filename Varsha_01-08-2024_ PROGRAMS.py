"""n1=int(input())
l1=[]
for i in range(n1):
	val=input("enter values for l1")
	l1.append(val)
n2=int(input())
l2=[]
for j in range(n2):
	val1=int(input("enter values for l2"))
	l2.append(val1)
for i in range(min(len(l1),len(l2))):
        print(l1[i],l2[i])
#Question 2       
N=int(input())
val=list(map(int,input().split(" ")))
print("Minimum element=",min(val))"""

import array as arr
L0=[]
n=int(input("enter how many values to be entered"))
for i in range(n):
    VAL0=int(input("enter values to be added in the array"))
    L0.append(VAL0)   
arr1=arr.array("i",L0)
print("before sorting array 1",arr1)
L1=[]
n1=int(input("enter how many values to be entered"))
for i in range(n1):
    VAL1=int(input("enter values to be added in the array"))
    L1.append(VAL1)   
arr2=arr.array("i",L1)
print("before sorting array 2",arr2)
L0.sort(reverse=True)
L1.sort(reverse=True)
arr1=arr.array("i",L0)
arr2=arr.array("i",L1)
print("after sorting array 1",arr1)
print("after sorting array 2 ",arr2)
l3=[]
l3.extend(L0)
l3.extend(L1)
A3=arr.array("i",l3)
print(A3)
l3=L0+L1
print(l3)
A3=arr1.concat(arr2)
print(A3)







