L=[12,34,56,67]
print("the original list is:",L)
n=int(input("number to be added:"))
L.append(n)
print("after adding",n,":",L)
num=int(input("enter number to be removed from the above list:"))
L.remove(num)
print("after removing",num,":",L)

AccountName=input("enter name")
AccountNumber=int(input("enter number"))
AccountBalance=float(input("enter balance"))
print("Account Name:",AccountName)
print("Account Number:",AccountNumber)
print(f"Balance:{AccountBalance:.2f}")



age=int(input("enter your age"))
if age>24:
    print("eligible to write bank exam")
else:
    print("not eligible to write bank exam")


V1=int(input("Enter value 1 "))
V2=int(input("Enter value 2 "))
V3=int(input("Enter value 3 "))
V4=int(input("Enter value 4 "))
V5=int(input("Enter value 5 "))
L=[V1,V2,V3,V4,V5]
print("The original list is:",L)
L.pop(2)
DATA=int(input("Enter a value"))
L.insert(2,DATA)
print("The changed list is:",L)


             
