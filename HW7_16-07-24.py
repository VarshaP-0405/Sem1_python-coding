balance=int(input("Enter the basic balance"))
flag="True"
while flag=="True":
    print("1.Deposit")
    print("2.Withdraw")
    print("3.View Balance")
    print("4.Exit")
    option=int(input("enter options (1 to 4)"))
    match option:
        case 1:
            deposit_money=int(input("Enter the Amount to be deposited"))
            balance=balance+deposit_money
            print("successfully deposited,balance is",balance)
            flag="True"
        case 2:
            Withdraw_money=int(input("Enter the Amount to be Withdrawn"))
            if balance>Withdraw_money:
                balance=balance-Withdraw_money
                print("successfully Withdrawn,balance is",balance)
                flag="True"
            else:
                print("amount cannot be withdrawn")
                flag="True"
        case 3:
            print("The balance is",balance)
            flag="True"
        case 4:
            quit()
            flag="False"
        case _:
            print("invalid option")
            flag="True"


flag="True"
while flag=="True":
    print("1.Starter")
    print("2.Main Course")
    print("3.Dessert")
    print("4.Exit")
    match option:
        case 1:
            print("1.Babycorn 65---->Rs.80")
            print("1.Cauliflower 65---->Rs.85")
            print("1.Tomato soup---->Rs.40")
            flag="True"
        case 2:
            print("1.Kulcha---->Rs.50")
            print("2.Noodles---->Rs.110")
            print("3.Schewan Fried Rice---->Rs.150")
            flag="True"
        case 3:
            print("1.Icecream---->Rs.40")
            print("2.Gulab Jamun---->Rs.30")
            print("3.Falooda---->Rs.50")
            flag="True"
        case 4:
            quit()
            flag="False"
        case _:
            print("The Food Item You Ordered Is Not Available")
            flag="True"

            

    
