print("--- Python OOP Project: Employee Management System ---")

class Employee:
    def __init__(self,emp_id,name,age,salary):
        self._emp_id=emp_id
        self.name=name
        self.age=age
        self._salary=salary

        print("Employee created!!")

    def setter(self,emp_id,salary):
        self._emp_id=emp_id
        self._salary=salary

    def get_empid(self):
        return self._emp_id  
    
    def get_salary(self):
        return self._salary
    
    def display(self):
        print("\n\nEmployee Details")
        print("Employee id:",self._emp_id)
        print("Name:",self.name)
        print("Age:",self.age)
        print("Salary:",self._salary)


class Manager(Employee):
    def __init__(self,emp_id,name,age,salary,department):
        super().__init__(emp_id,name,age,salary)
        self.department=department

    def display(self):
        print("\n\nManager Details")
        print("Manager id:",self._emp_id)
        print("Name:",self.name)
        print("Age:",self.age)
        print("Salary:",self._salary)
        print("Department:",self.department)

class Developer(Employee):
    def __init__(self,emp_id,name,age,salary,p_language):
        super().__init__(emp_id,name,age,salary)
        self.p_language=p_language

    def display(self):
        print("\n\nDeveloper Details")
        print("Developer id:",self._emp_id)
        print("Name:",self.name)
        print("Age:",self.age)
        print("Salary:",self._salary)
        print("Programming Language:",self.p_language)
         
eobj=None
mobj=None
dobj=None

while True:

    print("Choose a operation:")
    print("1. Create a Employee")
    print("2. Create an Manager")
    print("3. Create a Developer")
    print("4. Show Details")
    print("5. Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        emp_id=int(input("\nEnter employee id:"))
        name=input("Enter Name:")
        age=int(input("Enter Age:"))
        salary=int(input("Enter Salary:"))

        eobj=Employee(emp_id,name,age,salary)

        print(f"\nEmployee created with ID:{eobj.get_empid()},name:{eobj.name},age:{eobj.age},salary:{eobj.get_salary()}.")
        print("\n---Choose another operation---")

    elif choice==2:
        emp_id=int(input("\nEnter Manager id:"))
        name=input("Enter Name:")
        age=int(input("Enter Age:"))
        salary=int(input("Enter Salary:"))
        department=input("Enter department:")

        mobj=Manager(emp_id,name,age,salary,department)

        print(f"\nManager created with ID:{mobj.get_empid()},name:{mobj.name},age:{mobj.age},salary:{mobj.get_salary()} and department:{mobj.department}")
        print("\n---Choose another operation---")

    elif choice==3:
        emp_id=int(input("\nEnter Developer id:"))
        name=input("Enter Name:")
        age=int(input("Enter Age:"))
        salary=int(input("Enter Salary:"))
        p_language=input("Enter programming language:")

        dobj=Developer(emp_id,name,age,salary,p_language)        

        print(f"\nDeveloper created with ID:{dobj.get_empid()},name:{dobj.name},age:{dobj.age},salary:{dobj.get_salary()} and programming language:{dobj.p_language}")
        print("\n---Choose another operation---")

    elif choice==4:

        print("\n Choose the details to show:")
        print("1. Employee")
        print("2. Manager")
        print("3. Developer\n")

        ch=int(input("Enter your choice:"))

        if ch==1:
            if eobj:
                eobj.display()
            else:
                print("\n Employee detail not found")

        elif ch==2:
            if mobj:
                mobj.display()
            else:
                print("\n Manager detail not found")

        elif ch==3:
            if dobj:
                dobj.display()
            else:
                print("\n Developer detail not found")

        else:
            print("\n Invalid choice!!!!")

    elif choice==5:
        print("\nExiting the system. All Resources have been freed. ")
        print("\nGoodbye!\n")
        break

    else:
        print("Invalid choice!!!")