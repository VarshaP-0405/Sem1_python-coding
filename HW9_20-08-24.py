"""DICT={"VARSHA":[9,8,7],"VASUDHA":[8,9,8],"BARGAVI":[8,6,7]}
DICT["PRASADH"]=[7,7,6]
print("dictionary after adding value PRASADH is",DICT)
SUM=0
COUNT=0
STU_NAME=input()
if STU_NAME in DICT:
    for i in DICT.get(STU_NAME):
        SUM+=i
        COUNT+=1
else:
    print("Student Name Not Found")
AVG_STU=SUM/COUNT
print(AVG_STU)
if STU_NAME in DICT:
    del DICT[STU_NAME]
else:
    print("Student Name Not Found")
print("dictionary after removing the student")
print(DICT)"""
######
TUP=()
VAL=int(input("enter a single element"))
LIS=list(TUP)
LIS.append(VAL)
TUP=tuple(LIS)
print(TUP)
LIS=list(TUP)
LIS.append(34)
LIS.append(67)
TUP=tuple(LIS)
print(TUP*3)
ELE=int(input("enter the element to find index of:"))
print(TUP.index(ELE))
ST=str(TUP)
print(ST)
LIS=list(TUP)
MAXIMUM=max(LIS)
MINIMUM=min(LIS)
print("MAXIMUM IS",MAXIMUM,"MINIMUM IS ",MINIMUM)
GIV_ELE=int(input("enter the element whose count of occurence is to be found"))
COUNT=0
for i in TUP:
    if i==GIV_ELE:
        COUNT+=1
print("the occourence of the given element is:",COUNT)
TUP1=(1,2,(3,4),5,6,(7,8,9))
print(TUP1[2])
print(TUP1[2][1])
LIS=list(TUP)
LIS.pop(5)
TUP=tuple(LIS)
print("tuple after deletion of one element is:",TUP)











