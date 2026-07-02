# 🎓 Student Grade Management Program

A Python-based student grade management application developed for **CS 1101 – Programming Fundamentals (Unit 3)**. This project demonstrates the practical use of **for loops, while loops, break statements, continue statements, nested loops, input validation, and average grade calculation** within a real-world educational scenario.

---

# 📖 Overview

The goal of this project is to help a teacher manage student grades efficiently. The program can:

* Display student names.
* Record student grades.
* Validate user input.
* Skip invalid entries.
* Allow the teacher to stop grade entry at any time.
* Calculate the class average.
* Organize students according to their classes.

The project was developed as part of the Unit 3 discussion assignment on Python loops and loop-control statements.

---

# ✨ Features

* Student name display using **for loops**
* Grade entry system using **while loops**
* Grade validation
* Error handling for invalid inputs
* Early program termination using **break**
* Invalid input skipping using **continue**
* Class average calculation
* Student organization by class using **nested loops**
* Beginner-friendly Python code

---

# 🛠 Technologies Used

| Technology | Purpose                 |
| ---------- | ----------------------- |
| Python 3.x | Programming Language    |
| Git        | Version Control         |
| GitHub     | Repository Hosting      |
| VS Code    | Development Environment |

---

# 📦 Installation

## Option 1: Clone the Repository

```bash
git clone https://github.com/sourabghosh108-cc1/student-grade-management-system

cd student-grade-management
```

---

## Debian / Ubuntu / Linux Mint

Install Python:

```bash
sudo apt update

sudo apt install python3 python3-pip -y
```

Verify installation:

```bash
python3 --version
```

Run the application:

```bash
python3 disc3.py
```

---

## Fedora

Install Python:

```bash
sudo dnf install python3 -y
```

Verify installation:

```bash
python3 --version
```

Run the application:

```bash
python3 disc3.py
```

---

## Arch Linux / Manjaro

Install Python:

```bash
sudo pacman -S python
```

Verify installation:

```bash
python --version
```

Run the application:

```bash
python disc3.py
```

---

# ⬇ Download Executable

If you do not want to install Python, download the standalone executable version.

**Google Drive Download**

https://drive.google.com/file/d/1ml2zEkNEJk2w97HBNqtQrOmLeZSZOQLj/view?usp=sharing

### Windows

```text
Double-click disc3.exe
```


---

# 🚀 Usage

Run the program:

```bash
python3 disc3.py
```

The application will:

1. Display all student names.
2. Accept grade entries.
3. Validate user input.
4. Skip invalid grades.
5. Allow the teacher to stop grade entry.
6. Calculate the class average.
7. Display students organized by class.

---

# 💻 Sample Output

```text
Student List:
- Alice
- Ben
- Chloe
- David

Enter a grade, type 'next' to finish grades, or 'stop' to quit:
90

Grade recorded: 90.0

Enter a grade:
-5

Invalid grade. Negative grades are not allowed.

Enter a grade:
abc

Please enter a valid number.

Enter a grade:
85

Grade recorded: 85.0

Enter a grade:
next

Class Average: 87.50

Students Organized by Class:

Class 1
Student: Alice
Student: Ben

Class 2
Student: Chloe
Student: David
```

---

# 🎯 Learning Outcomes

This project demonstrates the ability to:

* Explain how for loops iterate through sequences.
* Discuss while loop structures.
* Apply break statements effectively.
* Apply continue statements effectively.
* Create nested loop structures.
* Validate user input.
* Calculate averages using Python.
* Develop a practical real-world application.

---

# 📚 Assignment Requirements & Implementation

This project was developed to solve the **Managing Student Grades** scenario from the Unit 3 Discussion Assignment.

---

## Question 1 – For Loop

### Requirement

Print each student's name from a list.

### Implementation

The program uses a **for loop** to iterate through the student list and display each student's name.

```python
students = ["Alice", "Ben", "Chloe", "David"]

for student in students:
    print(f"Student Name: {student}")
```

### Concept Demonstrated

* For Loop
* List Iteration
* Sequence Processing

---

## Question 2 – While Loop

### Requirement

Repeatedly ask the teacher to enter grades until they type `"done"`.

### Implementation

The program uses a **while loop** to continuously collect grade information until the teacher decides to stop.

```python
grade = ""

while grade.lower() != "done":
    grade = input("Enter a grade or type 'done' to finish: ")

    if grade.lower() != "done":
        print(f"Grade recorded: {grade}")
```

### Concept Demonstrated

* While Loop
* Conditional Repetition
* User-Controlled Input

---

## Question 3 – Break and Continue

### Requirement

Use:

* `break` to stop entering grades completely.
* `continue` to skip invalid grades.

### Implementation

The program uses a robust validation system that prevents invalid data from being processed.

```python
while True:
    grade = input("Enter a grade or type 'stop' to end: ")

    if grade.lower() == "stop":
        print("Grade entry stopped.")
        break

    try:
        grade = float(grade)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if grade < 0:
        print("Invalid grade.")
        continue

    print(f"Grade accepted: {grade}")
```

### Concept Demonstrated

* Break Statement
* Continue Statement
* Input Validation
* Error Handling

---

## Question 4 – Nested Loops

### Requirement

Print all student names organized by class.

### Implementation

The program uses a nested loop where:

* The outer loop processes classes.
* The inner loop processes students within each class.

```python
classes = [["Alice", "Ben"], ["Chloe", "David"]]

for class_number, classroom in enumerate(classes, start=1):
    print(f"\nClass {class_number}")

    for student in classroom:
        print(f"Student: {student}")
```

### Concept Demonstrated

* Nested Loops
* Multi-Level Iteration
* Hierarchical Data Processing

---

# 📂 Project Structure

```text
student-grade-management/
│
├── README.md
├── student_grade_management.py
├── StudentGradeManagement.exe
├── LICENSE
└── screenshots/
    └── sample-output.png
```

---

# 👨‍💻 Author

**Sourab Ghosh**

CS 1101 – Programming Fundamentals

University of the People

---

# 📜 License

This project is provided for educational purposes as part of a university programming assignment.

---

# 🔗 Repository

GitHub Repository:

https://github.com/sourabghosh108-cc1/student-grade-management-system
