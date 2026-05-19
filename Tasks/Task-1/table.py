# Multiplication Table Generator
# Take a number from the user and print its multiplication table using for loop and range() function.

num=int(input("enter num:"))

for i in range(1,11):
    print(num,"*",i,"=",num*i)