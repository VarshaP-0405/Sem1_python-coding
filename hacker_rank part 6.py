#Multiplication Table
N=int(input())
M=int(input())
print(F"Enter n")
print(F"Enter m")
print(F"The multiplication table of {N} is")
C=1
for i in range(M):
    MN=N*C
    print(f"{C}*{N}={MN}")
    C=C+1
    
#Print Prime Numbers in a range
upper=int(input())        
for num in range(1, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num,end="\t")
#Amoeba Multiplication
num=int(input())
n1=0
n2=1
count=0
sum1=0
if num==1:
    print(n1)
else:
    while count<num:
        sum1=n1
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1
print(sum1)
#Number Series
import math
N=int(input())
for i in range(1,N+1):
    if i%2==0:
        seq=(i**2)-2
        print(seq,end="\t")
    else:
        seq=(i**2)-1
        print(seq,end="\t")
#Hollow square pattern
n=int(input())
for i in range(n):
    for x in range(n):
        if i==0 or i==(n-1) or x==0 or x==(n-1):
                print("*",end="")
        else:
            print(" ",end="")
    print()
#reasure Finder
import math
a=int(input())
b=int(input())
c=int(input())
if a>b and a<c or a<b and a>c:
    sec=a
elif b>a and b<c or b<a and b>c:
    sec=b
else:
    sec=c

print("The treasure is in the box which has the number",sec)
gcd=math.gcd(math.gcd(a,c),b)
print("The code to open the box is",gcd)
#Collatz problem
n=int(input())
count=0
while n>=1:
    if n==1:
        print(n)
        break
    if n%2==0:
        print(n)
        n=n//2
        count+=1
    else:
        print(n)
        n=(3*n)+1
        count+=1
print(count)
#Strong Number
import math
NUM=int(input())#145
SUM=0
N=NUM
while NUM>0: 
    NUM1=NUM%10#5 
    FAC=math.factorial(NUM1)#120
    SUM+=FAC#120
    NUM//=10
if N==SUM:
    print("Yes")
else:
    print("No")
#Inverted right-angled triangle
N=int(input())
for i in range(N,0,-1):
    for j in range(i):
        print("*",end="")
    print()
#Sum of digit till single digit
number = int(input())
total_sum = 0
step = 1
condition = True
while condition:
    while number:
        total_sum += number%10
        number //= 10
    number = total_sum
    total_sum = 0
    step += 1
    condition = number > 9
print(number)
#Kaprekar number
K=int(input())
if K<1:
    print("Not a Kaprekar Number")
else:
    SQR=K**2
    string=str(SQR)
    n=len(str(K))
    RIGHT_DIG=int(string[-n:])
    LEFT_DIG=int(string[:-n])
    if (RIGHT_DIG+LEFT_DIG)==K:
        print("Kaprekar Number")
    else:
        print("Not a Kaprekar Number")

                












        
