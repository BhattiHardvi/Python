import datetime
import math
import random
import uuid

def dirmenu():

    print("\nExplore Module Attributes:")

    mod=input("Enter module name to explore:").lower()

    if mod=="datetime":
        print("\nAvailable Attributes in datetime module:")
        print(dir(datetime))

    elif mod=="math":
        print("\nAvailable Attributes in math module:")
        print(dir(math))

    elif mod=="random":
        print("\nAvailable Attributes in random module:")
        print(dir(random))

    elif mod=="uuid":
        print("\nAvailable Attributes in uuid module:")
        print(dir(uuid))


    else:
        print("Module not found!")

if __name__ == "__main__":
    dirmenu()