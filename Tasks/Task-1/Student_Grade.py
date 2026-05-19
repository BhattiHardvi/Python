# Student Grade Checker

# Take student name and marks using input(). Use if-elif-else to display grade (A, B, C, Fail).
#  Print datatype and memory address using type() and id().

name=input("enter name:")
marks=int(input("enter marks:"))

if marks>=90:
    print("A")
elif marks>=75:
    print("B")
elif marks>=55:
    print("C")
else:
    print("Fail")

print("\n")
print("datatype of name:",type(name))
print("memory address:",id(name))
print("\n")

print("datatype of marks:",type(marks))
print("memory address:",id(marks))

