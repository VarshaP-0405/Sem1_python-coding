#Time Sheet
SUN=int(input())
MON=int(input())
TUE=int(input())
WED=int(input())
THU=int(input())
FRI=int(input())
SAT=int(input())
TOT=MON+TUE+WED+THU+FRI
if MON>8:
    EXTRA_M=MON-8
    SAL_M=(MON*100)+(EXTRA_M*15)
else:
    SAL_M=MON*100
if TUE>8:
    EXTRA_TU=TUE-8
    SAL_TU=(TUE*100)+(EXTRA_TU*15)
else:
    SAL_TU=TUE*100
if WED>8:
    EXTRA_W=WED-8
    SAL_WE=(WED*100)+(EXTRA_WE*15)
else:
    SAL_WE=WED*100
if THU>8:
    EXTRA_TH=THU-8
    SAL_THU=(THU*100)+(EXTRA_TH*15)
else:
    SAL_THU=THU*100
if FRI>8:
    EXTRA_FR=FRI-8
    SAL_FRI=(FRI*100)+(EXTRA_FR*15)
else:
    SAL_FRI=FRI*100
SAL_SAT=0
if SAT>0:
    EXTRA_SA=(SAT*100)
    SAL_SAT=int((25/100)*EXTRA_SA)+EXTRA_SA
else:
    SAL_SAT=0
SAL_SUN=0
if SUN>0:
    EXTRA_SU=SUN*100
    SAL_SUN=int((50/100)*EXTRA_SU)+EXTRA_SU
else:
    SAL_SUN=0
WEEK=0
if TOT>40:
    WEEK=int((TOT-40)*25)
TOTAL=SAL_M+SAL_TU+SAL_WE+SAL_THU+SAL_FRI+SAL_SAT+SAL_SUN+WEEK
print(TOTAL)
#Number of Days
year=int(input())
month=int(input())
if 1900<=year<=9999:
    if 1<=month<=12:
        if month in [1,3,5,7,8,10,12]:
            print("31 Days")
        elif month==2:
            if (year%4==0 and year%100!=0 or year%400==0): 
                print("29 Days")
            else:
                print("28 Days")
        else:
            print("30 Days")
else:
    print(0)
#Scholarship
    age=int(input())
year=int(input())
income=int(input())
arrear=int(input())
scolarship=float(input())
attendance=float(input())
if year>=2021:
    if arrear<=2:
        if 18<=age<=21 and year>2021 and income<=200000 and arrear<2 and scolarship>=60 and attendance>=80:
            print("Eligible")
    else:
        if scolarship>=80 and attendance>=90 and(200000<=income<250000):
            print("Partially Eligible")
        else:
            print("Not Eligible")
else:
    print("Not Eligible")
#Mango tree
ROWS=int(input())
COLU=int(input())
TREE_NO=int(input())
if TREE_NO<=COLU:
    print("Yes")
elif TREE_NO%COLU==1:
    print("Yes")
elif TREE_NO%COLU==0:
    print("Yes")
else:
    print("No")
#Cricket
import math
tot_balls=int(input())
tot_runs=int(input())
no_runs=int(input())
no_balls=int(input())
TOT_OVERS=tot_balls//6
OVER_WHOLE=no_balls//6
OVERS_DEC=no_balls%6
TOTAL_OVERS=(OVER_WHOLE)+(OVERS_DEC/10)
CURR_RUN_RATE=no_runs/TOTAL_OVERS
TOT_RUN_RATE=tot_runs/TOT_OVERS
print(f"{TOT_OVERS}")
print(f"{TOTAL_OVERS:.1f}")
print(f"{CURR_RUN_RATE:.1f}")
print(f"{TOT_RUN_RATE:.1f}")
if CURR_RUN_RATE>=TOT_RUN_RATE:
    print("Eligible to Win")
else:
    print("Not Eligible to Win")
