A=int(input())
B=int(input())
l=[print(B) if A>B else print(A)]
   
    
import math
prin=float(input())
rate_int=float(input())
year=float(input())
c=(100+rate_int)/100
cmpd_int=math.pow(c,year)
ci=prin*cmpd_int
ci=ci-prin
print(int(ci))



A=int(input())
B=int(input())
print(A,B)
C=0
C=A
A=B
B=C
print(A,B)


L=[]
L.append(10)
L.append(45)
L.append(1)
L.append(67)
L.append(56)
print("the original list is",L)
print("checking if 10 is in L",10 in L)

s="abcd"
if "ef" not in s:
    print("true")
else:
    print("false")
    
    

