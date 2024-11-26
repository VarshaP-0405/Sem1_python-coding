a=int(input("Enter a number"))
if a%3==0 and a%5==0:
    print("divisible by both")
elif a%3==0:
    print("divisible by 3")
elif a%5==0:
    print("divisible by 5")

else:
    print("not divisible by both")

item1=int(input())
item2=int(input())
item3=int(input())
total=item1+item2+item3
if total>400:
    amount=(6.75/100)*total
    tax_amount=amount+total
    tip=(10/100)*tax_amount
    totalbill= tax_amount+tip
    print(int(total))
    print(int(amount))
    print(int(tip))
    print(int(totalbill))
else:
    print(total)

import math
weight=float(input())
height=float(input())
h2=math.pow(height,2)
bmi=weight/h2
print(round(bmi,1))
if bmi<16:
    print("Severe Thinness")
elif bmi>=16 and bmi<17:
    print("Moderate Thinness")
elif bmi>=17 and bmi<18.5:
    print("Mild Thinness")
elif bmi>=18.5 and bmi<25:
    print("Normal")
elif bmi>=25 and bmi<30:
    print("Overweight")
elif bmi>=30 and bmi<35:
    print("Obese Class I")
elif bmi>=35 and bmi<40:
    print("Obese Class II")
elif bmi>40:
    print("Obese Class III")


