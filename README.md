# 🎓 Student Grade Management System

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-Educational-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

A Python-based grade management application developed for **CS 1101 – Programming Fundamentals (Unit 3)** at the **University of the People**.

This project demonstrates the practical use of **for loops, while loops, break statements, continue statements, nested loops, dictionaries, input validation, and average grade calculation** through a real-world educational scenario.

---

# 📖 Overview

The Student Grade Management System is a Python-based application developed as part of **CS 1101 – Programming Fundamentals Unit 3**. The project demonstrates the practical implementation of **for loops, while loops, break statements, continue statements, and nested loops** while solving a real-world classroom management problem.

In this scenario, a teacher needs a program that can display student names, record grades, validate user input, calculate class averages, and organize students according to their classes. Python loop structures provide an efficient solution for handling these repetitive operations while reducing code duplication and improving program maintainability.

---

# ✨ Features

* Display student names using a **for loop**
* Record grades for individual students
* Validate user input
* Skip invalid grades using **continue**
* Stop grade entry using **break**
* Calculate class average
* Organize students by class using **nested loops**
* Store student grades efficiently
* Simple command-line interface
* Beginner-friendly implementation

---

# 🛠 Technologies Used

| Technology  | Purpose                 |
| ----------- | ----------------------- |
| Python 3    | Programming Language    |
| Git         | Version Control         |
| GitHub      | Repository Hosting      |
| VS Code     | Development Environment |
| PyInstaller | Executable Creation     |

---

# 📂 Project Structure

```text
student-grade-management-system/
│
├── disc3.py
├── disc3.exe
├── README.md
│
├── screenshots/
│   ├── output1.png
│   ├── output2.png
│   ├── output3.png
│   ├── output4.png
│   └── output5.png
│
└── LICENSE
```

---

# ⚙️ Installation Guide

## Option 1 – Clone the Repository

```bash
git clone https://github.com/sourabghosh108-cc1/student-grade-management-system.git

cd student-grade-management-system

chmod +x *
```

---

## Debian / Ubuntu / Linux Mint

```bash
sudo apt update

sudo apt install python3 -y

python3 disc3.py
```

---

## Fedora

```bash
sudo dnf install python3 -y

python3 disc3.py
```

---

## Arch Linux / Manjaro

```bash
sudo pacman -S python

python disc3.py
```

---

## Windows Executable

Run:

```text
disc3.exe
```

No Python installation is required when using the executable.

---

# 🚀 Usage

1. Launch the application.
2. View the student list.
3. Enter grades for students.
4. Input validation automatically checks entered values.
5. Invalid grades are rejected.
6. Type **stop** to terminate grade entry early.
7. View the class average.
8. View students organized by class.

---

# 💻 Sample Output

```text
==================================================
STUDENT GRADE MANAGEMENT SYSTEM
==================================================

Student List:
- Alice
- Ben
- Chloe
- David

Enter grades for each student.
Type 'stop' at any time to end grade entry.

Enter grade for Alice: 90
Grade recorded for Alice: 90.0

Enter grade for Ben: 85
Grade recorded for Ben: 85.0

Enter grade for Chloe: -5
Invalid grade. Negative grades are not allowed.

Enter grade for Chloe: 78
Grade recorded for Chloe: 78.0

Enter grade for David: 92
Grade recorded for David: 92.0

==================================================
STUDENT GRADES
==================================================

Alice: 90.0
Ben: 85.0
Chloe: 78.0
David: 92.0

==================================================
Class Average: 86.25
==================================================

==================================================
STUDENTS ORGANIZED BY CLASS
==================================================

Class 1
Alice: 90.0
Ben: 85.0

Class 2
Chloe: 78.0
David: 92.0

Program Completed Successfully.
```

---

# 📚 Assignment Questions Implementation

## Question 1 – For Loop

### Requirement

Explain how a for loop is used to print each student's name from a list.

### Code Implementation

```python
students = ["Alice", "Ben", "Chloe", "David"]

for student in students:
    print(f"Student Name: {student}")
```

### Explanation

A for loop iterates through every element in a sequence. In this project, the loop processes each student stored in the list and displays their name. This approach is efficient because additional students can be added without changing the loop structure.

---

## Question 2 – While Loop

### Requirement

Discuss how a while loop repeatedly asks the teacher to enter grades.

### Code Implementation

```python
while True:
    grade_input = input("Enter grade: ")

    try:
        grade = float(grade_input)
        break

    except ValueError:
        print("Invalid input.")
```

### Explanation

The while loop continues running until a valid grade is entered. This prevents invalid data from being stored and ensures reliable user input handling.

---

## Question 3 – Break and Continue Statements

### Requirement

Use break and continue statements to handle special situations.

### Code Implementation

```python
if grade_input.lower() == "stop":
    break

if grade < 0:
    continue
```

### Explanation

The break statement allows the teacher to stop entering grades whenever necessary.

The continue statement skips invalid entries, such as negative grades, and immediately moves to the next iteration of the loop.

---

## Question 4 – Nested Loops

### Requirement

Print student names organized by class.

### Code Implementation

```python
classes = [
    ["Alice", "Ben"],
    ["Chloe", "David"]
]

for class_number, classroom in enumerate(classes, start=1):

    print(f"\nClass {class_number}")

    for student in classroom:
        print(student)
```

### Explanation

The outer loop processes classes while the inner loop processes students belonging to each class. Nested loops are useful when working with hierarchical data structures.

---

# 🎯 Learning Outcomes

After completing this project, the following concepts were successfully demonstrated:

* Using for loops to iterate through sequences
* Using while loops to repeatedly execute tasks
* Implementing break statements for loop termination
* Implementing continue statements for skipping invalid input
* Creating nested loops for multi-level data structures
* Validating user input
* Storing and processing student data
* Calculating averages
* Building a practical Python application

---

# 📸 Screenshots

Include screenshots demonstrating:

### Screenshot 1

Displaying student names using a for loop

### Screenshot 2

Entering grades using a while loop

### Screenshot 3

Demonstrating break and continue statements

### Screenshot 4

Displaying student grades and class average

### Screenshot 5

Displaying students organized by class

---

# 👨‍💻 Author

**Sourab Ghosh**

CS 1101 – Programming Fundamentals

University of the People

---

# 🔗 Repository Link

Repository:

https://github.com/sourabghosh108-cc1/student-grade-management-system

---

# 📜 License

This project was developed for educational purposes as part of the CS 1101 Programming Fundamentals course at the University of the People.
