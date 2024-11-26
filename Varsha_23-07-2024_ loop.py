N=int(input())
N=str(N)
SUM=0
for i in N:
    SUM+=(int(i))
print(SUM)
#(OR)
Sum=0
num=int(input())
while num!=0:
    rem=num%10
    Sum+=rem
    num//=10
print(Sum)

N=int(input())
N=str(N)
MUL=1
for i in N:
    MUL*=(int(i))
print(MUL)
#(OR)
mul=1
num1=int(input())
while num1!=0:
    rem=num1%10
    mul*=rem
    num1//=10
print(mul)

INTEGER=int(input())
for i in range(INTEGER,0,-1):
    print(i,end="")
#(or)
print("\t")
n1=int(input())
while n1>0:
    print(n1)
    n1=n1-1
    
