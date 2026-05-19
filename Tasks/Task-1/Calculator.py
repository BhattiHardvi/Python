# Simple Calculator

# Accept two numbers and an operator from the user.
#  Use match-case to perform addition, subtraction, multiplication, or division.

n1=int(input("enter num1:"))
n2=int(input("enter num2:"))

choice=int(input("enter a choice:"))

match choice:
    case 1:
        print("addition of two numbers:",n1+n2)
    case 2:
        print("subtraction of two numbers:",n1-n2)
    case 3:
        print("multiplication of two numbers:",n1*n2)
    case 4:
        print("division of two number:",n1/n2)
    case _:
        print("invalid")
