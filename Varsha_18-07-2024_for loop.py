#QUESTION 1
c=0
print(f"the multiples of 4 are:")
for i in range(8):
    fac=4*c
    print(fac,end=" ")
    c=c+1
print()

#QUESTION 2
row=int(input("enter no of rows"))
col=int(input("enter no of columns"))
for i in range(row):
    for j in range(col):
        print("*",end=" ")
    print()   
#QUESTION 3
Scores=[85,90,-5,76,92,-1,88,79,55]
for i in Scores:
    if i==-1:
        print("Encountered missing data.stopping processing")
        break
    elif i<-1:
        print(f"invalid score {i} encountered.skipping")
        continue
    else:
        print("Score:",i)
    
