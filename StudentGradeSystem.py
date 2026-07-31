print("=============Student Grade System==============")
Name = str(input("Enter your Name: "))
Marks = int(input("Enter your Marks: "))
if Marks>=90:
    print("Grade: A+")
elif Marks>=80 and Marks<=89:
    print("GRADE: A")
elif Marks>=70 and Marks<=79:
    print("Grade: B")
elif Marks>=60 and Marks<=69:
    print("Grade: C")
elif Marks>=50 and Marks<=59:
    print("Grade: D")
else:
    print("Grade: F")
print("====================End=======================")
