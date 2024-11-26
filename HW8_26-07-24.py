import math
num=30
NUM=int(input())
L=[]
L1=[]
n1=0
n2=1
count=0
if num==1:
    L.append(n1)
else:
    while count < num:
        L.append(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1
for x in L:
    if x%2==0:
        L1.append(x)
count1=0
print(L1[(NUM)])


L3=[]
numofplots=int(input())
area=list(map(int,input().split()))
L3=area 
L2=[]
for y in range(1,107):
    sqr=math.pow(y,2)
    L2.append(sqr)
for u in L2:
    for v in L3:
        if u==v:
            count1+=1
print(count1)
