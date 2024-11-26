#3 Psychos
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
midx=(x1+x2)/2
midy=(y1+y2)/2
print(f"Arun's house is located at({midx},{midy})")
#Hop n Hop
import math
x1=int(input())
y1=int(input())
x2=3
y2=4
square_x=math.pow((x2-x1),2)
square_y=math.pow((y2-y1),2)
dist=int(math.sqrt(square_x+square_y))
print(dist)
#Dollars & Cents
D1=int(input())
C1=int(input())
D3=int(input())
C2=int(input())
C1_D2=C1//100
C2_D4=C2//100
SUM_CENT=(C1+C2)
if SUM_CENT>100:
    SUM1=D1+D3+1
    SUM2=(C1+C2)-100
else:
    SUM1=D1+D3
    SUM2=(C1+C2)
print(SUM1)
print(SUM2)
#Treasure Hunter
total_coin=int(input())
Ben_Share=int(input())
Black_Share=int(input())
Ben_coin=int((Ben_Share/100)*total_coin)
AMOUNT_REMAINING=total_coin-Ben_coin
Black_coin=int((Black_Share/100)*AMOUNT_REMAINING)
REMAINING=total_coin-(Ben_coin+Black_coin)
others_coin=REMAINING//3
print(Ben_coin)
print(Black_coin)
print(others_coin)
#Reverse a 3-digit number
n=int(input())
third=n%10
second=(n//10)%10
first=n//100
Rev_of_digits=third*100+second*10+first
print(Rev_of_digits)
#Tic Tac Toe
n=int(input())
if n>=1 and n<=9:
    l=[-1,-1]
    l[1]=-1
    if n in [1,2,3]:
        l[0]=0
        if n==1:
            l[1]=0
        if n==2:
            l[1]=1
        if n==3:
            l[1]=2
    if n in [4,5,6]:
        l[0]=1
        if n==4:
            l[1]=0
        if n==5:
            l[1]=1
        if n==6:
            l[1]=2
    if n in [7,8,9]:
        l[0]=2
        if n==7:
            l[1]=0
        if n==8:
            l[1]=1
        if n==9:
            l[1]=2 
print(l[0],l[1])
# ANOTHER METHOD:
n=int(input())
if 1<=n<=9:
    n=n-1
    r=n//3
    c=n%3
print(f"{r} {c}")
#Checking Alphabets
char=input()
char.strip()
if char.isalpha():
    if char in ["a","e","i","o","u"]:
        print("Vowel")
    elif char in ["A","E","I","O","U"]:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")
#Electricity Bill
unit=int(input())
if unit<=200:
    cost=unit*0.5
elif unit>200 and unit<=400:
    cost=(unit*0.65)+100
elif unit>400 and unit<=600:
    cost=(unit*0.80)+200
else:
    cost=(unit*1.25)+425
cost=int(cost)
print(f"Rs.{cost}")
