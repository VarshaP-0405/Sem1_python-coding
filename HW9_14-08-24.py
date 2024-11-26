"""n=int(input())
arr=[]
SUM1=0
for i in range(n):
    L=list(map(int,input().split()))
    arr.append(L)
for i in arr:
    for j in i:
        SUM1+=j
print(SUM1)"""
    
n=int(input())
arr=[]
for i in range(n):
    L=list(map(int,input().split()))
    arr.append(L)
element_to_find = int(input("Enter the element to be found: "))
found = False
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == element_to_find:
            print(f"Found at position ({i},{j})")
            found = True
            break
    if found:
        break
if not found:
    print("Not found")

"""n=int(input())
arr=[]
for i in range(n):
    L=list(map(int,input().split()))
    arr.append(L)
for i in range(n):
    for x in range(n):
        print(arr[i][x],end=" ")
    print()
print("Transpose matrix is:")
for i in range(len(arr[0])):
    for j in range(len(arr)):
        print(arr[j][i],end=" ")
    print()


n=int(input())
arr=[]
for i in range(n):
    L=list(map(int,input().split()))
    arr.append(L)
print("Theater Seating Chart:")
for row in arr:
    for seat in row:
        if seat == 0:
            print("O", end=" ")
        else:
            print("X", end=" ")
    print()"""

        
