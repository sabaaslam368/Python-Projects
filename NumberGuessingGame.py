SecretNum = 23
Attempt = 0

while True:
    num = int(input("Enter the number: "))
    Attempt+=1
    if num==SecretNum:
        print("Congratulation! you guess correct number")
        print("Attempt: ",Attempt)
        break
    elif num>SecretNum:
        print("Too High")
    else:
        print("Too Low")