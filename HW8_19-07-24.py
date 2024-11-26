#Question 1
START=int(input("enter start range:"))
END=int(input("enter end range:"))
print("Odd numbers:",end=" ")
for i in range(START,END+1):
    if i%2==1:
       print(i,end=" ")
print("\n")
print("Even numbers:",end=" ")
for n in range(START,END+1):
    if n%2==0:
        print(n,end=" ")

#Question 2
print("\n")
str1=input("Enter a string")
str1=str1.upper()
for i in range(len(str1)-1,-1,-1):
    print(str1[i],end="")

#Question 3
print("\n")
num=int(input("enter number of times to repeat"))
L=[]
success=0
loss=0
for i in range(num+1):
    n=int(input("enter a number:"))
    List=L.append(n)
print("Number of successful sales:",end=" ")
for x in L:
    if x>=0:
       success+=1
print(success)
print()
print("Number of returns or losses:",end=" ")
for m in L:
    if m<0:
        loss+=1
print(loss)
print()
          
