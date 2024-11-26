age = int(input("Enter your age: "))  
try:
    assert age >= 18, "Participant must be at least 18 years old"
    assert age <= 60, "Participant must be no older than 60 years old"
except AssertionError as e1:
   print( f"Registration error: {e1}")
except AssertionError as e2:
   print( f"Registration error: {e2}")
else:
    print("Participant is eligible for registration.")
#QUESTION 2
try:
    N1=int(input())
    N2=int(input())
    add=N1+N2
    print(add)
except TypeError as te:
    print(te)
#QUESTION 3
BALANCE=int(input())
try:
    WITHDRAW=int(input())
    if BALANCE>WITHDRAW:
        BALANCE=BALANCE-WITHDRAW
        print("Withdrawn successfully . Your new balance is",BALANCE)
    assert WITHDRAW<0, ("Error: NegativeWithdrawalError message")
    assert BALANCE<WITHDRAW, ("Error: InsufficientFundError message")
except AssertionError as e1:
    print(e1)
except AssertionError as e2:
    print(e2)
