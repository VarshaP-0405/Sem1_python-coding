import random
def USER1(F):
    while F:
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        user_input = input("Enter a value (1-3): ")
        user1 = int(user_input)
        if user1 not in [1, 2, 3]:
            print("Invalid choice. Please enter a number between 1 and 3.")
            continue
        F = False
        BOT = random.randrange(1, 4)
        print(f"BOT chose: {BOT}")

        if (user1 == 1 and BOT == 3) or (user1 == 2 and BOT == 1) or (user1 == 3 and BOT == 2):
            print("YOU WIN")
        elif user1 == BOT:
            print("MATCH DRAW")
        else:
            print("BOT WINS")
print("WANT TO PLAY AGAIN? (Y/N)")
CH = input("ENTER Y OR N: ").strip().upper()
while CH == "Y":
    USER1(True)
    print("WANT TO PLAY AGAIN? (Y/N)")
    CH = input("ENTER Y OR N: ").strip().upper()
