def Add(d, key, lis):
    d[key] = lis
    return d

def Remove(d, key):
    if key in d:
        del d[key]
        return True
    else:
        return False

def Update(d, key, l):
    if key in d:
        d[key] = l
        return True
    else:
        return False

def Search(d, key):
    if key in d:
        return d[key]
    else:
        return False

dic = {}
while True:
    print("\nMAIN MENU")
    print("1. Add")
    print("2. Display")
    print("3. Remove")
    print("4. Update")
    print("5. Search")
    print("6. Exit")
    
    choice1 = int(input("Enter the Choice: "))
    
    if choice1 == 1:
        l = []  
        Id = int(input("Enter the student id: "))
        Name = input("Enter the name: ")
        Grade = input("Enter the student grade: ")
        Major = input("Enter the student's major: ")
        l.append(Name)
        l.append(Grade)
        l.append(Major)
        dic = Add(dic, Id, l)
        print("The dictionary after adding values is:", dic)
        
    elif choice1 == 2:
        print(dic)
        
    elif choice1 == 3:
        Id = int(input("Enter the student id to be removed: "))
        if Remove(dic, Id):
            print("The dictionary after removing values is:", dic)
        else:
            print("ID not found")
            
    elif choice1 == 4:
        Id_up = int(input("Enter the student id to update: "))
        Name_up = input("Enter the name to update: ")
        Grade_up = input("Enter the student grade to update: ")
        Major_up = input("Enter the student's major to update: ")
        l = [Name_up, Grade_up, Major_up]  
        if Update(dic, Id_up, l):
            print("The dictionary after updating values is:", dic)
        else:
            print("ID not found")
            
    elif choice1 == 5:
        Id = int(input("Enter the id to search in the dictionary for: "))
        result = Search(dic, Id)
        if result:
            print(result)
        else:
            print("ID not found")
            
    elif choice1 == 6:
        break
    
    else:
        print("Invalid choice, please try again.")
