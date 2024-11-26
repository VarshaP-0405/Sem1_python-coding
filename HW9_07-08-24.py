"""S1=set(map(str,input().split()))
S2=set(map(str,input().split()))
c=0
for i in S2:
    if i in S1:
        c+=1
if len(S2)==c:
    print("S2 is a subset of S1")
else:
    print("S2 is  not a subset of S1")
######
tup1=tuple(map(str,input().split()))
if len(tup1)>2:
    print(tup1[2:5])
else:
    print(tup1[1:2])"""
######
"""fruits = ("apple", "banana", "cherry")
(red, yellow, pink) = fruits
print(green)
print(yellow)
print(red)
######
l1=[(2, 5), (9, ), (8, 7, 6), (4, ), (12, 4, 16, 7)]
k=int(input())
for i in l1:
    if len(i)==k:
        l1.remove(i)
print(l1)
######
tup2=tuple(map(str,input().split()))
print(tup2)
v=" ".join(tup2)
print(v)
######
list_of_tuples = [("varsha","1"), ("sai","2"),("vasu","3")]
print(list_of_tuples)
dictionary = {}
for key, value in list_of_tuples:
    dictionary.setdefault(key, []).append(value)"""
######
"""k=5
L=1
for i  in range(5):
    for dash in range(5,i,-1):
        print(" ",end="")
    for i in range(5):
        for j in range(k):
            print("*",end="")
        k=k-1
        print()
    for i in range(5):
        for j in range(L):
            print("*",end="")
        L=L+1
        print() """
######
n=int(input())
left=1
for i  in range(n,0,-1):
    for dash in range(n,i,-1):
        print("  ",end="")
    for j in range(0,i):
        print("*",end="  ")
        left+=1
    print()
for i  in range(1,n+1,1):
        for dash in range(i,n,1):
            print("  ",end="")
        for j in range(0,i):
            print("*",end="  ")
            left-=1
        print()








        

