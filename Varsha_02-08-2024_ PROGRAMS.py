n=int(input())
NUM=n
rev_num=0
while n>0:
    last_dig=n%10
    rev_num=rev_num*10+last_dig
    n=n//10
if NUM==rev_num:
    print("number is a palindrome")
else:
    print("number is  not a palindrome")
#####
import math
n=int(input("Enter the number of terms:"))
x=int(input("Enter the value of x:"))
sum1=1
for i in range(2,n+1):
    sum1=sum1+((x**i)/math.factorial(i))
print("The sum of series is",round(sum1,2))
######
N=int(input())
MUL=1
while N>0:
    last_dig=N%10
    MUL*=last_dig
    N=N//10
print(MUL)
#######
var=int(input())
mul=1
for i in range(var,0,-1):
    mul*=i
print(mul)
#######
n1=int(input())
if n1%2==0 or n1%3==0 or n1%5==0 or n1%7==0:
    print("not a prime number")
else:
    print("prime number")
######
for i in range(5,9):
    print(i)
######
for i in "Python":
    print(i,end="")
######
for i in "Python":
    print(i,'?$')
#######
x=8
while x<=20:
    print(x**2)
    x+=3
#######
rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
######
for i in range(100,500):
    if i%11==0 and i%2!=0:
        print(i)
















