try:
    import string
    n=input()
    sub=input()
    x=n.index(sub)
except ValueError :
    print("Substring was not found")
#Question 2
try:
    sum1=0
    count=0
    grades=[]
    n=int(input())
    for i in range(n):
        val=int(input())
        grades.append(val)
    for x in grades:
        sum1+=x
        count+=1
    average=sum1/count
    print(average)
except ZeroDivisionError as ze:
    print("list cannot be empty")
#Question 3
try:
    value_1=int(input())
    grade=[]
    ret_val=int(input())
    for y in range(value_1):
        num1=int(input())
        grade.append(num1)
    print(grade[ret_val])
except IndexError as ie:
    print("index errror")
        

    
