num=int(input("Enter a number:"))
if num%2==0:
    print("Even")
else:
    print("Odd")

n=int(input("Enter a number:"))
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")

math=int(input("Enter math mark:"))
phy=int(input("Enter physics mark:"))
chem=int(input("Enter chemistry mark:"))
total=math+phy+chem
percentage=(total/300)*100
print(total)
print(f"{percentage:.2f}")
if percentage>90:
    print("Eligible")
else:
    print("Not Eligible")

import string
s1=input("enter a string")
s1.strip()
if s1.isalpha():
    if s1.isupper():
        print("Upperecase")
    elif s1.islower():
        print("Lowercase")
    else:
        print("Combination of both")
    

    
