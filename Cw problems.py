import array as ar
sum1=0
c=0
max1=0
L1=[]
n=int(input("enter no of values to be appended in the array"))
for i in range(n):
    val=int(input("enter values to be in the array"))
    L1.append(val)
v=ar.array("i",L1)
for i in v:
    sum1+=i
print(sum1)
ele_search=int(input("enter the element to be searched"))
if ele_search not in v:
        print ("element not present in the array")
else:
    for x in v:

        if x==ele_search:

            c+=1
print("the no of times the element has occured is:",c)
for i in v:
    if i>max1:
        max1=i
print(max1)
    
