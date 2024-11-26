rows, cols = map(int, input().split())
matrix1 = []
matrix2 = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix1.append(row)
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix2.append(row)
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)
for row in result:
    print(" ".join(map(str, row)))
######
n=int(input()) 
arr=[]
arr1=arr[:][:]
num = len(arr)
for i in range(n):
    L=list(map(int,input().split()))
    arr.append(L)
for i in range(n):
    for j in range(i + 1, n):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
for i in range(n):
    arr[i].reverse()
for row in arr:
    print(" ".join(map(str, row)))
######
m=int(input())
n=int(input()) 
arr=[]
for i in range(m):
    L=list(map(int,input().split()))
    arr.append(L)
MA_VAL=[]
for i in range(n):
    max_value=arr[0][i] 
    for j in range(1,m):
        if arr[j][i]>max_value:
            max_value = arr[j][i]
    MA_VAL.append(max_value)
print(max(MA_VAL))
######
n=int(input()) 
arr=[]
c=0
for i in range(n):
    L=list(map(int,input().split()))
    arr.append(L)
for j in range(n):
    for k in range(n):
        if arr[i][j]==arr[j][i]:
            c+=1
        else:
            c=0
if c>0:
    print("Symmetric matrix")
else:
    print("Not a Symmetric matrix")
        

    
