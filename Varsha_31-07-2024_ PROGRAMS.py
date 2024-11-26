"""import array as arr
L0=[]
n=int(input("enter how many values to be entered"))
for i in range(n):
    VAL0=int(input("enter values to be added in the array"))
    L0.append(VAL0)   
arr1=arr.array("i",L0)
print(arr1[5])
print('Beofre loop',arr1)
for i in range(len(arr1)-1,-1,-1):
    print(arr1[i])
arr1.insert(13,1600)
arr1.insert(14,1700)
print(arr1)
#Second Question
import array as arr
L1=[]
for i in range(10):
    n=int(input("enter values to be appended in the list"))
    L1.append(n)
arr2=arr.array("i",L1)
print(arr2)
new=int(input("enter a new score"))
arr2[3]=new
print(arr2)
print(max(arr2))
print(min(arr2))"""
#Third Question
import array as arr
arr3=arr.array("d",[10.99, 5.49, 20.00, 7.95, 12.75])
print(arr3)
print(sum(arr3))
arr3.remove(arr3[1])
print(arr3)
new_item_price=float(input("new items price"))
arr3.insert(int(len(arr3))+1,new_item_price)
print(arr3)



