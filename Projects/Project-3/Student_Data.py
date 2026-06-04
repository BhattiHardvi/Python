print("Welcome to the Student Data Organizer!\n")
students=[]

while True:
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice=int(input("Enter your choice: "))
    if(choice==1):

        print("Enter student detaitls:")
        stid=int(input("Student ID: "))
        name=input("Name: ")
        age=int(input("Age: "))
        grade=input("Grade: ")
        dob=input("Date of Birth (YYYY-MM-DD): ")        
        subjects=input("Subjects (comma-separated): ").split(",")
    
        st={
            "stid": stid,
            "name": name,
            "age": age,
            "grade": grade,
            "dob": dob,
            "subjects": [s.strip() for s in subjects]
        }
        students.append(st)
        print("\nStudent added successfully!\n")

    elif(choice==2):
        print("\n---Display All Students---\n")

        if len(students)==0:
            print("No Details found!!!")
        else:
            for info in students:
                print(
                    f"Student ID: {info['stid']} | "
                    f"Name: {info['name']} | "
                    f"Age: {info['age']} | "
                    f"Grade: {info['grade']} | "
                    f"Subjects: {', '.join(info['subjects'])}"
    )
                print("\n")

    elif(choice==3):
        stid=int(input("Enter student ID to update: "))
        for st in students:
            if st["stid"]==stid:
                st['name']=input("New Name: ")
                st['age']=int(input("New Age: "))
                st['grade']=input("New Grade: ")
                st['dob']=input("New DOB (YYYY-MM-DD): ")
                st['subjects']=input("New Subjects: ").split(",")

                print("\nStudent information updated successfully!\n")
                break
            else:
                print("Student not found.")

    elif(choice==4):
        stid=int(input("Enter student ID to delete: "))

        for st in students:
            if st["stid"]==stid:
                students.remove(st)
                print("\nStudent Deleted Successfully!\n")
                break
            else:
                print("Student not found.")

    elif(choice==5):
        print("\n---Subjects Offered---\n")

        sub_set=set()

        for st in students:
            sub_set.update(st["subjects"])

        for subject in sub_set:
            print(subject)

        print("\n")

    elif(choice==6):
        print("Thank you for using this Student Data Organizer!")
        break

    else:
        print("Invalid choice!!!!")