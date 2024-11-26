"""n = int(input())

arr=[]
for i in range(n):
 VAL = list(map(int, input().split()))
 arr.append(VAL)
rows = len(arr)#3
cols = len(arr[0])#3
for col in range(cols):#0,1,2
    if col % 2 == 0:#0
        for row in range(rows):#0,1,2
            print(arr[row][col], end=" ")
    else:#1
        for row in range(rows-1, -1, -1):#2,1,0
            print(arr[row][col], end=" ")
#######"""
n = int(input())
arr=[]
for i in range(n):
 VAL = list(map(int, input().split()))
 arr.append(VAL)#[1 2 3 4 5 6 7 8 9]
rows = len(arr)#3
print(rows)
cols = len(arr[0])#3
for start in range(rows + cols - 1):#(0,1,2,3,4)
    if start < cols:#(2<3)
        r = 0
        c = start#0#1#2
    else:
        r = start - cols + 1#
        c = cols - 1
    
    while r < rows and c >= 0:#0<3 and 0>=0# 0<3 and 1>=0#0<3 and 2>=0
        print(arr[r][c], end=" ")#[0][0]#[0][1]#[0][2]#
        r+=1#1
        c-=1#-1
        
