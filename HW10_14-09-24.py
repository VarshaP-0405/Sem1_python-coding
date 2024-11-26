##1##
import random
def roll_dice():
    while True:
        print("1. ROLL")
        print("2. QUIT")
        user = input("ENTER A NUMBER (1-2): ").strip()
        if user == "1":
            print("You rolled:", random.randint(1, 6))  
        elif user == "2":
            print("Exiting the game...")
            break
        else:
            print("Invalid input. Please enter 1 or 2.")

while True:
    print("WANT TO ROLL AGAIN? (Y/N)")
    ch = input("ENTER Y OR N: ").strip().upper()
    if ch == "Y":
        roll_dice()
    elif ch == "N":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter Y or N.")
##2##
import random
def pick(L):
    while True:
        print("1. PICK")
        print("2. QUIT")
        user = input("ENTER A NUMBER (1-2): ").strip()
        if user == "1":
            print("YOU PICKED:", random.choice(L))  
        elif user == "2":
            print("Exiting the choices...")
            break
        else:
            print("Invalid input. Please enter 1 or 2.")
l=[]
while True:
    print("WANT TO CHOOSE AGAIN? (Y/N)")
    ch = input("ENTER Y OR N: ").strip().upper()
    if ch == "Y":
        print("pick to choose a restaurant")
        N=int(input("no of values to append in the list"))
        for i in range(N):
            val=input()
            l.append(val)
        pick(l)
    elif ch == "N":
        print("BYE!!! Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter Y or N.")
##3##
def val_chk(val):
    if val.isalpha() or val.isdigit() or "_" in val:
        if val[0].isalpha():
            if 5<=len(val)<=15:
                print("This username is valid")
            else:
                print("The username length must be between 5 and 15 characters")
        else:
            print("The username must start with a letter")
    else:
        print("The username must contain only letters,numbers or underscore")
user_name=input("input the username")
val_chk(user_name)
















