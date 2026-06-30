from MyPackage.datetime_menu import Datetimemenu
from MyPackage.math import mathmenu
from MyPackage.random_menu import randommenu
from MyPackage.uuid_menu import uuidmenu
from MyPackage.file import filemenu
from MyPackage.dir import dirmenu

while True:

    print("\n===============================")
    print("Welcome to Multi-Utility Toolkit")
    print("===============================")
    print("\nChoose an option:")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print("================================")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        Datetimemenu()
 
    elif choice == "2":
        mathmenu()

    elif choice == "3":
        randommenu()

    elif choice == "4":
        uuidmenu()

    elif choice == "5":
        filemenu()

    elif choice == "6":
        dirmenu()

    elif choice == "7":
        print("\n================================")
        print("Thank you for using the Multi-Utility Toolkit!")
        print("================================\n")
        break

    else:
        print("Invalid choice!")