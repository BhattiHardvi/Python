import random
import string

def randommenu():

    while True:

        print("\n========== Random Data Generation ==========")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            num = random.randint(1, 100)
            print("\nRandom Number:", num)

        elif choice == "2":

            random_list = [random.randint(1, 1000) for _ in range(5)]
            print("\nRandom List:", random_list)

        elif choice == "3":

            characters = string.ascii_letters + string.digits + "@#$%&!*"

            password = ""

            for _ in range(8):
                password += random.choice(characters)

            print("\nGenerated Password:", password)

        elif choice == "4":

            otp = random.randint(100000, 999999)
            print("\nGenerated OTP:", otp)

        elif choice == "5":

            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    randommenu()