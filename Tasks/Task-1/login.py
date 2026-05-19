# Menu Driven Login System

# Create a menu with options like Admin, Student, and Guest using match-case. 
# Perform different actions based on user selection using conditional statements.

choice=input("enter string :")

match choice:
    case "admin":
        password=input("enter password:")

        if password=="hardvi123":
            print("Welcome admin")
        else:
            print("Wrong password")
    case "student":
        marks=int(input("enter the marks:"))

        if marks>=35: 
            print("pass")
        else:
            print("fail") 
    case "guest":
        age=int(input("enter your age:"))

        if age>=18:
            print("valid age !!! now you can login")
        else:
            print("invalid age!!! login fail")
    case _:
        print("invalid!!!!!!!!!")
        
          