from datetime import datetime
import time

def Datetimemenu():

    while True:

        print("\n========== Datetime and Time Operations ==========")
        print("1. Display Current Date and Time")
        print("2. Calculate Difference Between Two Dates")
        print("3. Display Formatted Date and Time")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            print("\nCurrent Date and Time:")
            print(datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

        elif choice == "2":

            try:
                date1 = input("\nEnter First Date (DD-MM-YYYY): ")
                date2 = input("Enter Second Date (DD-MM-YYYY): ")

                d1 = datetime.strptime(date1, "%d-%m-%Y")
                d2 = datetime.strptime(date2, "%d-%m-%Y")

                difference = abs((d2 - d1).days)

                print(f"\nDifference: {difference} days")

            except ValueError:
                print("Invalid date format! Please enter the date as DD-MM-YYYY.")

        elif choice == "3":

            now = datetime.now()

            print("\nFormatted Date and Time:")
            print(now.strftime("%A, %d %B %Y"))
            print(now.strftime("%d/%m/%Y"))
            print(now.strftime("%I:%M:%S %p"))

        elif choice == "4":

            seconds = int(input("\nEnter number of seconds: "))

            print("\nStopwatch Started...\n")

            for i in range(1, seconds + 1):
                mins, secs = divmod(i, 60)
                hrs, mins = divmod(mins, 60)
                print(f"{hrs:02}:{mins:02}:{secs:02}")
                time.sleep(1)

            print("Stopwatch Finished!")

        elif choice == "5":

            seconds = int(input("\nEnter countdown time (seconds): "))

            print("\nCountdown Started...\n")

            while seconds > 0:
                mins, secs = divmod(seconds, 60)
                hrs, mins = divmod(mins, 60)
                print(f"{hrs:02}:{mins:02}:{secs:02}")
                time.sleep(1)
                seconds -= 1

            print("Time's Up!")

        elif choice == "6":

            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    Datetimemenu()