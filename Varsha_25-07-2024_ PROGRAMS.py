import math
n=int(input())
L=[]
for i in range(0,n+1):
    sqr=math.pow(i,2)
    L.append(sqr)
if n in L:
    print(f"{n} is a Perfect Square")
else:
    print(f"{n} is not a Perfect Square")

n1==1
n2=4
num=int(input())
for i in range(1,n,1):
 i=str(i)



r=int(input())
col=int(input())
for i in range(0,r):
    for j in range (0,col):
        if i==0 or i==r-1 or j==0 or j==col-1:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()
    
        
        
