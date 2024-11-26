num=int(input())
sum1=0
string=str(num)
for i in string:
    n=(int(i))%10
    sum1+=(int(n))
    n//=10
if num%sum1==0:
    print(f"{num} is a Harshad Number")
else:
    print(f"{num} is  not a Harshad Number")
    
L=[]
sum2=0
integer=int(input("Enter no of months"))
for i in range(integer):
    num2=int(input("Enter no of books"))
    L.append(num2)
print(L)
for x in L:
    sum2+=x
print(f"The total number of books read by all the students is:{sum2}")

num3=int(input())
for i in range(1,num3+1,1):
    for j in range(i):
        print("*",end="")
    print()
