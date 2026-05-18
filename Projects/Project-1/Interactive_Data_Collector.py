print("Welcome to the Interactive Personal Data Collector!",end="\n\n")

Name=input("Please enter your name: ")
Age=int(input("Please enter your age: "))
Height=float(input("Please enter your height in meters: "))
Favourite_Number=int(input("Please enter your favourite number: "))
print(end="\n")

print("Thank you! Here is the information we Collected:",end="\n\n")

print("Name: ",Name,"( Type: ",type(Name), "Memory Address: ",id(Name),")")
print("Age: ",Age,"( Type: ",type(Age), "Memory Address: ",id(Age),")")
print("Height: ",Height,"( Type: ",type(Height), "Memory Address: ",id(Height),")")
print("Favourite Number: ",Favourite_Number,"( Type: ",type(Favourite_Number), "Memory Address: ",id(Favourite_Number),")")
print(end="\n")

current_year=2026

year_age=current_year-Age

print("Your birth year is approximately: ",year_age,"( based on your age",Age,")",end="\n\n")
print("Thank you for using the Personal Data Collector. Goodbye!")
