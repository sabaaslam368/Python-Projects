print("==================Employee Database System====================")

print("1. Add Employee")
print("2. View Employee")
print("3. Search Employee")
print("4. Exit")


import csv
import os

choice = int(input("Choose option: "))
if choice==1:
    if not os.path.exists("EmployeeData.csv"):
        with open("EmployeeData.csv","w",newline="" ) as file:
             Writer = csv.writer(file)

             Writer.writerow(["Employee ID","Name","Department","Salary"])
             Writer.writerow(["01","Saba Aslam","Computer Science", 5000000])
             Writer.writerow(["02","Dua Jalal","IT",5500000])
    else:
        print("File is already exist")        
       
elif choice==2:
    with open("EmployeeData.csv","r") as file:
         reader = csv.reader(file)
         for row in reader:
            print(row)
            
elif choice==3:
    search_name = input("Enter Employee name: ")

    with open("EmployeeData.csv", "r") as file:
         reader = csv.DictReader(file)
         print(reader)

         for row in reader:
            if row["Name"].lower() == search_name.lower():
             print("Employee ID:", row["Employee ID"])
             print("Name:", row["Name"])
             print("Department:", row["Department"])
             print("Salary:", row["Salary"])
elif choice==4:

    exit()
else:
    print("Invalid Choice")

