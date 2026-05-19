# Even/Odd & Positive/Negative Checker

# Input a number and use nested if statements to check whether the number is even/odd and positive/negative.

num=int(input("enter num:"))

if num>0:
    print("positive number")
    if num%2==0:
        print("even number")
    else:
        print("odd number")
else:
    print("negative number")