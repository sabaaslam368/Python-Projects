print("=============Students Record Management System=================")
Student = [
    {"Name": "Saba Aslam","Age":23,"CGPA":3.56,"Semester":"2nd"},
    {"Name": "Easha Farooq","Age":27,"CGPA":3.6,"Semester":"3nd"},
    {"Name": "Dua Jalal","Age":26,"CGPA":3.9,"Semester":"4nd"},
    {"Name": "Zara Fatima","Age":25,"CGPA":3.57,"Semester":"1nd"},
    {"Name": "Maryam Ameen","Age":24,"CGPA":3.5,"Semester":"4nd"}
]

print("1. Add Student")
print("2. View Student")
print("3. Search Student")
print("4. Update Student")
print("5. Delete Student")
print("6. Exit")

Choice = int(input("Choose option: "))
if Choice==1:
     Student[2] = {"Name": "Maryam Hanif","Age":25,"CGPA":3.4,"Semester":"4nd"}
     print(Student)
elif Choice==2:
     print(Student[0])
elif Choice==3:
     print(Student[4]["Name"])
elif Choice==4:
     Student[3]["Name"]="Rubab"
     print(Student)
elif Choice==5:
     del Student[2]
     print(Student)
elif Choice==6:
     exit
else:
     print("Invalid Choice")
