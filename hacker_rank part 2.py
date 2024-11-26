#area:
length=int(input())
breadth=int(input())
peri=(length+breadth)
perimeter=2*peri
area=length*breadth
print("The required length is",perimeter,"m")
print("The required area of carpet is",area,"sqm")
#newspaper:
a=int(input())
b=int(input())
c=int(input())
co=(a*b)
cost=co-(a*c)
cost1=cost-100
print(cost1)
#harry potter:
import string
n=input()
n=n.strip()
n=n.strip(string.punctuation)
print(int(n[0])+int(n[-1]))
#team seperation:
n=int(input())
n1=int(input())
num=n//n1
remainder=n%n1
print("The number of friends in each team is",num,"and left out is",remainder)
#intrest:
prin=float(input())
rate_int=float(input())
year=float(input())
intrest=(prin*rate_int*year)/100
amount=prin+intrest
discount=(2.0/100)*intrest
finalsettlement=amount-discount
print(f"{intrest:.2f}")
print(f"{amount:.2f}")
print(f"{discount:.2f}")
print(f"{finalsettlement:.2f}")

