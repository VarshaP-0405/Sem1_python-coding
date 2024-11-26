###1###
def Display(L):
    print("The Books in the list are")  
    for i in L:
        print(i)
    
def Add(N,L):
    L.append(N)
    print("The book is added in the list")
   
def Remove(N,L):
    L.remove(N)
    print("The book is removed from the list")
    
LIST=[ ]
print("1.Add")
print("2.Remove")
print("3.Display")
print("4.Exit")
flag=True
while flag:
    choice=int(input("enter a choice (1-4):"))
    if choice==1:
        n=input("enter a book name to add")
        Add(n,LIST)
        flag=True
    elif choice==2:
        n=input("enter a book name to remove")
        Remove(n,LIST)
        flag=True
    elif choice==3:
        Display(LIST)
    elif choice==4:
        flag=False
        quit()
    else:
        print("enter a valid number")
        flag=True
###2###
def Display(L):
    print("The Products in the list are:")
    for product in L:
        print(f"Name: {product[0]}, Quantity: {product[1]}")
    
def Add(N, Q, L):
    L.append([N, Q])
    print("The Product is added to the list.")

def Remove(L2,L):
    if L2 in L:
        L.remove(L2)
        print("The Product is removed from the list.")
    else:
        print("The Product was not found in the list.")
LIST = []
print("1. Add")
print("2. Remove")
print("3. Display")
print("4. Exit")
while True:
    try:
        choice = int(input("Enter a choice (1-4): "))
        if choice == 1:
            n = input("Enter a product name to add: ")
            q = input("Enter a product quantity to add: ")
            Add(n, q, LIST)
        elif choice == 2:
            n = input("Enter a product name to remove: ")
            q = input("Enter a product quantity to remove: ")
            L2=[n,q]
            Remove(L2,LIST)
        elif choice == 3:
            Display(LIST)
        elif choice == 4:
            print("Exiting the program.")
            quit()
        else:
            print("Enter a valid number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a number.")











    
        
