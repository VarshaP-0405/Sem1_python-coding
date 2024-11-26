dict1={}
dict1={"varsha":1,"sai":2,"prasadh":3}
dict1["varsha"]=1
dict1["sai"]=2
dict1["prasadh"]=5
print(dict1)
i=dict1["varsha"]
print(i)
dict2={"vasu":3,"bargavi":4}
dict1.update(dict2)
print(dict1)
del dict1["sai"]
print(dict1)
for j in dict1:
    print(j)
L=[]
for k in dict1:
    L.append(tuple(k))
print(L)
S1=set(dict1.keys())
print(S1)
KEY=(input())
if KEY in (dict1.keys()):
    print("True")
else:
    print("False")
print(len(dict1.items()))
key1=(input())
if key1 in (dict1.keys()):
    print(dict1.get(key1))
val=input()
if val in (dict1.keys()):
    dict1.pop(val)
else:
    print("key not found")
dict3=dict1
dict3.clear()
dict1.copy()
print(dict1.keys())
print(dict1.values())
print(dict1.items())

