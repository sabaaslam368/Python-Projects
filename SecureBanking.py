print("========Secure Bank Transaction System=======")

correctedPIN = 123890
Balance = 10000
try:
        pin = int(input("Enter you pin: "))
       
        try:
            D_Money = int(input("Enter the deposite money: "))
           
        except ValueError:
            print("Deposite amount is negative")
        else:
             print("Collect your cash")
             UpdatedBalance=Balance + D_Money
             print(UpdatedBalance)
        try:
            W_Money=int(input("Enter the withdraw Money"))
            RemaningBalance=Balance-W_Money
            print(RemaningBalance)
        except ValueError:
            print("Insufficient Balance")

        Balance=RemaningBalance
        print(Balance)     

except ValueError:
        print("Invalid pin")
   


                 


    