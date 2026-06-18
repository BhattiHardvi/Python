# Employee Management System (Python OOP)

## Overview
This is a console-based Employee Management System developed using Python Object-Oriented Programming (OOP) concepts.

The project demonstrates:
- Classes and Objects
- Inheritance
- Encapsulation
- Method Overriding
- Constructors
- Menu-Driven Programming

## Classes

### Employee
Base class containing:
- Employee ID
- Name
- Age
- Salary

Methods:
- `get_empid()`
- `get_salary()`
- `display()`

### Manager
Derived from Employee.

Additional Attribute:
- Department

Overrides:
- `display()`

### Developer
Derived from Employee.

Additional Attribute:
- Programming Language

Overrides:
- `display()`

## Features

1. Create Employee
2. Create Manager
3. Create Developer
4. Display Details
5. Exit Program

## Concepts Used

- Encapsulation (`_emp_id`, `_salary`)
- Inheritance (`Manager`, `Developer`)
- Polymorphism (Method Overriding)
- Constructors (`__init__`)
- Menu-driven User Interaction

## Sample Output

```
Choose a operation:
1. Create a Employee
2. Create an Manager
3. Create a Developer
4. Show Details
5. Exit

Enter your choice: 1

Enter employee id: 101
Enter Name: John
Enter Age: 25
Enter Salary: 50000

Employee created!!
Employee created with ID:101,name:John,age:25,salary:50000.
```

## How to Run

1. Install Python 3.
2. Save the code as `OOP_project.py`.
3. Open Terminal or Command Prompt.
4. Run:

```bash
python OOP_project.py
```
