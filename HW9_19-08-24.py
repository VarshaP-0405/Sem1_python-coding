"""n = int(input())
m = int(input())
arr = []
l1=[]
d=1
v=0
c=0
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
print("Average grades for each student:")
for row in arr:
    row_sums = sum(row)/len(row)
    print(f"student{d}:{row_sums:.2f}")
    d+=1
print("Highest grade in each subject:")
col_max = [max(arr[i][j] for i in range(n)) for j in range(m)]
print("Math:",col_max[0])
print("Science:",col_max[1])
print("English:",col_max[2])
for i in range(n):
    for j in range(m):
        v+=arr[i][j]
        c+=1
print(f"Overall class average:{(v/c):.2f}")"""
######
n = int(input())
m = int(input())
arr = []
l1=[]
d=1
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
print("Total Quantities of each product")
for row in arr:
    row_sums = sum(row)
    print(f"Product{d}:",row_sums)
    l1.append(row_sums)
    d+=1
product=int(input("enter values 1-4"))
mas=l1[product-1]
for i  in range(n):
    for j in range(m):
        if mas==arr[product][0]:
            mas="A"
        elif mas==arr[product][1]:
            mas="B"
        elif mas=arr[product][2]:
            mas="C"
        else:
            mas="D"
print("Section with the highest quantity for Product",product,":Section",mas)
print("Product with the lowest quantity:Product",l1.index(min(l1)))

















      
