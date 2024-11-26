"""n=int(input())
list1=list(map(int,input().split()))
val=int(input())
c=0
for i in list1:
    if i==val:
        c+=1
print(c)
if c>(n/2):
    print(val,"is a majority element")
else:
     print(val,"is not a majority element")"""
######
n1=int(input())
list2=list(map(int,input().split()))#3 4 2 6
max1=max(list2)#6
sec_max=0
if len(list2)<2:
    print("There i no second largest element") 
for i in list2:#3#4#2#6
    if  i<max1 and i>sec_max:#3<6 and 3>0#4<6 and 4>3#2<6 and 2>4
        sec_max=i#3#4
print('Second max value is:',sec_max)#4
######
"""number = int(input())
to_replace = input()
replace_with = input()
number_str = str(number)
modified_number_str = number_str.replace(to_replace, replace_with)
modified_number = int(modified_number_str)
print(f"Modified number = {modified_number}")
######
user_name=input()
password=input()
correct_username={"VARU":"v@123","SAI":"s@123","VASU":"v@234"}
if user_name not in correct_username:
    print("Invalid username")
elif  user_name in correct_username and password != correct_username[user_name]:
    print("Print Incorrect password")
else:
    print("Successfully logged in")"""




     
