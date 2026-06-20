class JournalManager:
    def __init__(self,filename="journal.txt"):
        self.filename=filename

    def add_entry(self):
            try:
                entry=input("Enter your journal entry:\n")

                with open(self.filename,"a") as file:
                    file.write(entry + "\n")

                print("Entry added successfully!")

            except Exception as e:
                print("Error:",e)

    def view_entries(self):
            try:
                with open(self.filename,"r") as file:
                    data=file.read()

                    if data.strip():
                        print("\nYour journal entries:")
                        print("-"*10)
                        print(data)
                    else:
                        print("No journal entries are found. Start by adding a new entry!")

            except FileNotFoundError:
                print("Error: The journal file does not exist. Please add a new entry first.")

    def search_entry(self):
            try:
                key=input("Enter a keyword or date to search:")

                with open(self.filename,"r") as file:
                    lines=file.readlines()

                    found=False
                    print("\nMatching Entries:")
                    print("-"*10)

                    for line in lines:
                        if key.lower() in line.lower():
                            print(line.strip())
                            found=True

                    if not found:
                        print(f"No entries were found for the keyword:{key}")

            except FileNotFoundError:
                print("Error: The journal file does not exist. Please add a new entry first.")

    def delete_entry(self):
            try:
            
                with open(self.filename, "w") as file:
                    pass

                print("All journal entries have been cleared.")

            except FileNotFoundError:
                print("No journal file found.")

journal = JournalManager()

while True:

    print("Welcome to Personal Journal Manager!\n")
    print("Please select an option:\n")

    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice=int(input("User Input:\n"))
    if choice==1:
        journal.add_entry()

    elif choice==2:
        journal.view_entries()

    elif choice==3:
        journal.search_entry()

    elif choice==4:
        journal.delete_entry()

    elif choice==5:
        print("Thank you for using Personal Journal Manager. Goodbye!")
        break

    else:
        print("Invalid option. Please select a valid option from the menu.")
