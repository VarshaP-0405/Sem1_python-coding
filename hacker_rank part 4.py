#Online shopping
F_P=int(input())
F_DIS=int(input())
F_SC=int(input())
Sn_P=int(input())
Sn_DIS=int(input())
Sn_SC=int(input())
AM_P=int(input())
AM_DIS=int(input())
AM_SC=int(input())
F_DISC=(F_DIS/100)*F_P
Sn_DISC=(Sn_DIS/100)*Sn_P
AM_DISC=(AM_DIS/100)*AM_P
F_AMT=((F_P-F_DISC))+F_SC
Sn_AMT=((Sn_P-Sn_DISC))+Sn_SC
AM_AMT=((AM_P-AM_DISC))+AM_SC
print(f"In Flipkart: Rs.{int(F_AMT)}")
print(f"In Snapdeal: Rs.{int(Sn_AMT)}")
print(f"In Amazon: Rs.{int(AM_AMT)}")
if F_AMT<Sn_AMT and F_AMT<AM_AMT:
    print("Choose Flipkart")
elif Sn_AMT<F_AMT and Sn_AMT<AM_AMT:
    print("Choose Snapdeal")
elif AM_AMT<F_AMT and AM_AMT<Sn_AMT:
    print("Choose Amazon")
else:
    print("Choose Flipkart")
#Hotel Tariff Calculator
month=int(input())
perday_rent=int(input())
nodays=int(input())
if month>=1 and month<=12:
    if month in [4,5,6,11,12]:
        perday_rent=((20/100)*perday_rent)+perday_rent
        l=perday_rent*nodays
        print(int(l))
    else:
        l=perday_rent*nodays
        print(int(l))
else:
    print("Invalid Input")
    
#Gift for Birthday
year=int(input())

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
#Trendy number
n=int(input())
num=str(n)
s=(n//10)%10
sec_div=int(s%3)
if len(num)==3 :
    if sec_div==0 :
        print("Trendy Number")
    else:
        print("Not a Trendy Number")
else:
    print("Invalid Number")










    
