print("===========Calculator==============")
Number1 = int(input("Enter First Number: "))
Number2 = int(input("Enter Second Number: "))

print("Addition: ", Number1+Number2)
print("Subtraction: ", Number1-Number2)
print("Multiplication: ", Number1*Number2)

if Number2!=0:
 print("Division: ", Number1/Number2)
 print("Floor Division: ", Number1//Number2)
 print("Modulas: ", Number1%Number2)

else:
 print("Division:  Number1 is divided by zero")
 print("Floor Division: Number1 is not divided by zero")
 print("Modulas: Number is not divided by zero")

print("Power:   ", Number1**Number2)