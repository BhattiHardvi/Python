print("Welcome to Data Analyzer and Transformer Program\n")

arr=[]
def display_data():

    print("Main menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Function)")
    print("3. Calculate Factorial  (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")


def input_data():
    global arr
    arr=[int(i) for i in input("Enter data for a 1D array (separated by comma): \n").split(",")]

    print("\nData has been stored successfully !\n")


def data_summary():

    print("Data Summary:")

    print("- Total elements:",len(arr))
    print("- Minimum value:",min(arr))
    print("- Maximum value:",max(arr))
    print("- Sum of all value:",sum(arr))
    print("- Average value:",sum(arr)/len(arr))
    print("\n")

def fact(n):

    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

def main():

    num=int(input("Enter a number to calculate its factorial:"))
    print("\n")

    print(f"Factorial of {num} is:",fact(num))
    print("\n")



def data_threshold(arr):

 
    threshold = int(input("Enter a threshold value to filter out data above this value: \n"))

    check = lambda x: x >= threshold

    print(f"\nFiltered Data (values >= {threshold}):")

    for i in arr:
        if check(i):
            print(i, end=" ")

    print("\n")


  
def Sorting():
    if not arr:
        print("Please input data first!\n")
        return

    print("Choose sorting option:\n")
    print("1. Ascending")
    print("2. Descending")

    ch=int(input("Enter your choice: "))
    print("\n")

    if ch==1:
        arr.sort()
        print("Sorted Data in Ascending order:")
        print(*arr)
        print("\n")
    else:
        arr.sort(reverse=True)
        print("Sorted Data in Descending order:")
        print(*arr)
        print("\n")

def data_statistics():

    print("Dataset Statistics:")

    print("- Minimum value:",min(arr))
    print("- Maximum value:",max(arr))
    print("- Sum of all value:",sum(arr))
    print("- Average value:",sum(arr)/len(arr))
    print("\n")




while True:
    display_data()
    choice=int(input("Please enter your choice:"))
    print("\n")

    if choice==1:
        input_data()
    elif choice==2:
        data_summary()
    elif choice==3:
        main()
    elif choice==4:
        data_threshold(arr)
    elif choice==5:
        Sorting()
    elif choice==6:
        data_statistics()
    elif choice==7:
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break
    else:
        print("invalid choice! please enter valid choice")