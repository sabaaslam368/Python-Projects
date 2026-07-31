print("=====================ATM Simulation===================")
ConfirmPIN = 123456
Balance = 10000

PIN = int(input("Enter the PIN: "))
if PIN == ConfirmPIN:
    print("Login Successful, Welcome!")
    print("1. Balance Inquiry")
    print("2. Deposite Amount")
    print("3. Withdraw Amount")
    choice = int(input("Choose Option: "))

    if choice==1:
      print("Corrected Balance: ", Balance)
    elif choice==2:
      Amount = int(input("Enter the Number: "))
      Balance+=Amount
      print(Balance)
    elif choice==3:
      WithdrawAmount = int(input("Enter the Withdraw Amount: "))
      if Balance>=WithdrawAmount:
        print("Collect your Cash")
        RemaningBalance = Balance-WithdrawAmount
        print(RemaningBalance)
      else: 
        print("Insufficent Balance")

    else:
      print("Incorrect Option")

else: 
    print("Invalid PIN")
