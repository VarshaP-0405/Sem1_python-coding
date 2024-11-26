import math
#Question 1
num=int(input())
num=str(num)
for i in range(len(num)-1,-1,-1):
    print(num[i],end="")
#Question 2
print("\t")
num1=int(input())
L=len(str(num1))
print(L)
number=0
while L==3:
    first=num1//100
    sec=(num1//10)%10
    third=num1%10
    n1=(math.pow(first,L))
    n2=(math.pow(sec,L))
    n3=(math.pow(third,L))
    number=n1+n2+n3
if number==num1:
    print("AMSTRONG NUMBER")
else:
    print("NOT AN AMSTRONG NUMBER")
                                
