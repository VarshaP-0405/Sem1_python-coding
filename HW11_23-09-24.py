"""print("hi this is varvas")
print("how may i assist you today")
flag=True
while flag:
    print("1.check you broadband plan")
    print("2.check the latest bill")
    print("3.report connectivity issues")
    print("4.provide contact information for support")
    print("5.byee byeee")
    choice=int(input("what do you want to do today(1-5):"))
    if choice==1:
        print("hi i have checked your broadband plan")
        print("Plan Value: Rupees 361")
        print("Data is 50GB and the validity is 30 days")
    elif choice==2:
        print("last payment done at september-18-2024")
    elif choice==3:
        print("there is a connectivity issue prompted")
        print("check ypur connectivity properly ")
        print("network reloading")
    elif choice==4:
        print("for further information contact number is 9975664328")
        print("contact us through email:airtelplans24@gmail.com")
    else:
        print("thank you for reeaching me")
        print("every moment was precious while chatting with you")
        print("byeeeeee :-) :-) :-)")
print("how may i assist you further")"""
##2##
print("Hi and welcome to the quiz")
dict1 = {
    1: ["What is the formula for sodium chloride?", "NaCl"],
    2: ["What is the formula for calcium chloride?", "CaCl2"],
    3: ["What is the formula for sulfuric acid?", "H2SO4"]
}

flag = True
Score = 0

while flag:
    print("1. Question 1")
    print("2. Question 2")
    print("3. Question 3")
    print("4. Exit")  
    choice = int(input("Choose the question to answer (1-4): "))
    
    if choice == 1:
        print(dict1[1][0])  
        answer = input("Your answer: ")
        if answer.strip() == dict1[1][1]: 
            Score += 1
    elif choice == 2:
        print(dict1[2][0])
        answer = input("Your answer: ")
        if answer.strip() == dict1[2][1]:
            Score += 1
    elif choice == 3:
        print(dict1[3][0])
        answer = input("Your answer: ")
        if answer.strip() == dict1[3][1]:
            Score += 1
    elif choice == 4:
        flag = False  
    else:
        print("Invalid choice, please select a valid option.")

print(f"Your final score is: {Score}")

       
