print("=====================ATM Simulation===================")

ConfirmPIN = 123456
Balance = 10000
Attempt = 3

while Attempt > 0:
    PIN = int(input("Enter the PIN: "))
    
    if PIN == ConfirmPIN:
        print("Login Successful, Welcome!")
        print("1. Balance Inquiry")
        print("2. Deposite Amount")
        print("3. Withdraw Amount")
        print("4. Another Transaction")
        print("5. Fast Transaction")
        choice = int(input("Choose Option: "))

        if choice == 1:
            print("Corrected Balance: ", Balance)
        elif choice == 2:
            Amount = int(input("Enter the Number: "))
            if Amount > 0:
                Balance += Amount
                print("Updates Balance: ", Balance)
                break
            else:
                print("Invalid Balance")
                break
        elif choice == 3:
            WithdrawAmount = int(input("Enter the Withdraw Amount: "))
            if Balance >= WithdrawAmount:
                if WithdrawAmount > 0:
                    print("Collect your Cash")
                    RemaningBalance = Balance - WithdrawAmount
                    print(RemaningBalance)
                    break
                else:
                    print("Invalid Withdraw Amount")
                    break
            else:
                print("Insufficent Balance")
                break
        elif choice == 4:
            print("Perform Another Transaction")
        elif choice == 5:
            print("1. Rs. 500")
            print("2. Rs. 1000")
            print("3. Rs. 1500")
            FastChoice = int(input("Enter Fast Choice: "))
            
            if Balance >= FastChoice:
                # CHANGE: Use FastChoice instead of choice here
                if FastChoice == 1:   # Fixed: was choice==1
                    Balance -= 500
                    print("Please collect your cash")
                    Remaning_Balance = Balance - FastChoice
                    print("Your remaining Balance is : ", Remaning_Balance)
                    break
                elif FastChoice == 2:   # Fixed: was choice==2
                    Balance -= 1000
                    print("Please collect your cash")
                    Remaning_Balance = Balance - FastChoice
                    print("Your remaining Balance is : ", Remaning_Balance)
                    break
                elif FastChoice == 3:   # Fixed: was choice==3
                    Balance -= 1500
                    print("Please collect your cash")
                    Remaning_Balance = Balance - FastChoice
                    print("Your remaining Balance is : ", Remaning_Balance)
                    break
                else:
                    print("Invalid Choice")
                    break
            else:
                print("Insufficient Balance for Fast Transaction")
                break
        else:
            print("Incorrect Option")
            break
    else:
        Attempt -= 1
        if Attempt > 0:
            print("Incorrect PIN Attempt left: ", Attempt)
        else:
            print("You are Blocked")
            exit()