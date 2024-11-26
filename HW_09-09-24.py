"""#1
N=int(input())
C=False
l=[2,3,5,7]
for i in l:
    if N%i:
        C=True
    else:
        C=False
if C==True:
    print("Prime Number")
else:
    print(" Not Prime Number")
#2
Num=int(input())
fac=1
while Num>0:
    fac*=Num
    Num-=1
print(fac)
#3
num=int(input())
N1=0
N2=1
count=0
L=[]
if num<0:
    print("Enter positive number")
elif num==1:
    print("The Fibonniacci series is",N1)
else:
    while count<num:
        L.append(N1)
        N3=N1+N2
        N1=N2
        N2=N3
        count+=1
print("The Fibonniacci series is",*L)
#4
number=int(input())
if number%11==0:
    print("The number is divisible by 11")
else:
    print("The number is not divisible by 11")
#5
num1=int(input())
l=[]
for i in range(1,n+1):
    if n%1==0:
        l.append(i)
print("the factors of the number",num1,"are",*l)"""
#Armstrong Number
num2=int(input())
arm_num=num2
first=num2//100
second=(num2//10)%10
last=num2%10
arm=(first**3)+(second**3)+(last**3)
if arm==arm_num:
    print("This number is armstrong number")
else:
    print("This number is not an armstrong number")
#Odd or Even
val=int(input())
if val%2==0:
    print("This number is Even number")
else:
    print("This number is Odd number")
