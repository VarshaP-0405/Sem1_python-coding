#Trapezium Pattern
n=int(input())
left=1
right=(n*n)+1
for i  in range(n,0,-1):
    for dash in range(n,i,-1):
        print("--",end="")
    for j in range(1,i+1):
        print(left,end="*")
        left+=1
    for k in range(1,i+1):
        print(right,end="")
        if k<i:
            print("*",end="")
        right+=1
    print()
    right=right-(i-1)*2-1
#Same or Not
size1 = int(input())
size2 = int(input())
if size1 != size2:
    print("Not Same")
else:
    array1 = []
    for X in range(size1):
        array1.append(int(input()))
    array2 = []
    for Y in range(size2):
        array2.append(int(input()))
    sum1 = sum(array1)
    sum2 = sum(array2)
    if sum1 == sum2:
        print("Same")
    else:
        print("Not Same")
#Count distinct elements
N=int(input())
L1=[]
for i in range(N):
    L1.append(int(input()))
print(f"There are {len(set(L1))} distinct element in the array.")
#Compatible array
size1 = int(input())
l1=[]
for i in range(size1):
    val=int(input())
    l1.append(val)
size2 = int(input())
l2=[]
for j in range(size2):
    val1=int(input())
    l2.append(val1)
if size1==size2:
    for i in range(size1):
        if l1[i]>=l2[i]:
            c=True
        else:
            c=False
    if c:
        print("Compatible")
    else:
        print("Incompatible")
else:
    print("Incompatible")
#Sum of even numbers and odd numbers
size1 = int(input())
l1=[]
eve_sum=0
odd_sum=0
for i in range(size1):
    val=int(input())
    l1.append(val)
for i in l1:
    if i%2==0:
        eve_sum+=i
    else:
        odd_sum+=i
print(f"The sum of the even numbers in the array is {eve_sum}")
print(f"The sum of the odd numbers in the array is {odd_sum}")
#Ascending order
size1 = int(input())
l1=[]
for i in range(size1):
    val=int(input())
    l1.append(val)

print("The Sorted array is:")
l1.sort()
for i in l1:
    print(i)












    








