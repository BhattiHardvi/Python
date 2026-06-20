# Personal Journal Manager

## Project Description
Personal Journal Manager is a Python-based console application that allows users to maintain a digital journal. Users can add entries, view all entries, search for specific entries, and delete all stored entries. Journal data is saved in a text file (`journal.txt`) for persistence.

---

## Features

- Add new journal entries
- View all saved entries
- Search entries using keywords
- Delete all journal entries
- File handling with exception management
- Menu-driven user interface

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- File Handling
- Exception Handling

---

## Class Structure

### JournalManager

#### Methods

| Method | Description |
|----------|-------------|
| `add_entry()` | Adds a new journal entry to the file |
| `view_entries()` | Displays all journal entries |
| `search_entry()` | Searches entries by keyword |
| `delete_entry()` | Deletes all journal entries |

---

## File Used

### journal.txt

This file stores all journal entries entered by the user.

Example:

```
Today I learned Python file handling.
Completed my OOP project.
Feeling productive today.
```

---

## Menu Options

```
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

---

## How to Run

1. Install Python 3.
2. Save the program as `FO.py`.
3. Open terminal or command prompt.
4. Navigate to the project folder.
5. Run the program:

```bash
python FO.py
```

---

## Example Usage

### Add Entry

```
Enter your journal entry:
Today was a great day.
Entry added successfully!
```

### Search Entry

```
Enter a keyword or date to search:
great

Matching Entries:
Today was a great day.
```

---

## Exception Handling

The program handles:

- Missing journal file
- File read/write errors
- Invalid operations

---

## Future Enhancements

- Add date and time automatically
- Delete specific entries
- Edit existing entries
- Password protection
- GUI version using Tkinter

---

## Author

Developed as a Python OOP and File Handling Project.