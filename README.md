# 🎓 Student Grade Management System

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-Educational-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

A Python-based grade management application developed for **CS 1101 – Programming Fundamentals (Unit 3)** at the **University of the People**.

This project demonstrates the practical use of **for loops, while loops, break statements, continue statements, nested loops, dictionaries, input validation, and average grade calculation** through a real-world educational scenario.

---

# 📖 Overview

This application simulates a teacher managing student grades.

The program allows users to:

- Display student names
- Enter grades for each student
- Validate user input
- Skip invalid grades
- Stop data entry when needed
- Calculate the class average
- Display students organized by class

The project was created to demonstrate Unit 3 programming concepts while solving a practical classroom management problem.

---

# ✨ Features

- ✅ Display student names using **for loops**
- ✅ Enter grades for individual students
- ✅ Store grades using Python dictionaries
- ✅ Validate numeric input
- ✅ Skip invalid grades using `continue`
- ✅ Exit grade entry using `break`
- ✅ Calculate class averages
- ✅ Organize students using nested loops
- ✅ Beginner-friendly and fully commented code

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.x | Programming Language |
| Git | Version Control |
| GitHub | Repository Hosting |
| VS Code | Development Environment |

---

# 📦 Installation

## Clone the Repository

```bash
git clone https://github.com/sourabghosh108-cc1/student-grade-management-system.git

cd student-grade-management-system
```

---

## Linux Installation

### Debian / Ubuntu / Linux Mint

```bash
sudo apt update
sudo apt install python3 python3-pip -y

python3 disc3.py
```

### Fedora

```bash
sudo dnf install python3 -y

python3 disc3.py
```

### Arch Linux / Manjaro

```bash
sudo pacman -S python

python disc3.py
```

---

# 💻 Running the Program

Run:

```bash
python3 disc3.py
```

The program will:

1. Display all student names.
2. Request grades for each student.
3. Validate every grade entered.
4. Reject invalid input.
5. Store student grades.
6. Calculate the class average.
7. Display all grades.
8. Display students organized by class.

---

# ⬇ Download Executable

## Windows Executable

**Google Drive**

https://drive.google.com/file/d/1ml2zEkNEJk2w97HBNqtQrOmLeZSZOQLj/view?usp=sharing

---

# 💻 Sample Output

```text
Student List:
Alice
Ben
Chloe
David

Enter grade for Alice: 90
Grade recorded successfully.

Enter grade for Ben: 85
Grade recorded successfully.

Enter grade for Chloe: 78
Grade recorded successfully.

Enter grade for David: 92
Grade recorded successfully.

Student Grades:
Alice: 90.0
Ben: 85.0
Chloe: 78.0
David: 92.0

Class Average: 86.25

Students Organized by Class:

Class 1
Alice
Ben

Class 2
Chloe
David
```

---

# 📚 Assignment Requirements Implemented

## Question 1 – For Loop

Displays every student using a **for loop**.

```python
for student in students:
    print(student)
```

✅ Requirement Satisfied

---

## Question 2 – While Loop

Uses a **while loop** to repeatedly request valid input.

```python
while True:
```

✅ Requirement Satisfied

---

## Question 3 – Break and Continue

### Break

```python
if grade.lower() == "stop":
    break
```

### Continue

```python
if grade < 0:
    continue
```

These statements allow the teacher to stop grade entry or skip invalid grades.

✅ Requirement Satisfied

---

## Question 4 – Nested Loops

Students are organized by class using nested loops.

```python
for class_number, classroom in enumerate(classes, start=1):
    for student in classroom:
        print(student)
```

✅ Requirement Satisfied

---

# 🧠 Learning Outcomes

This project demonstrates:

- Using **for loops**
- Using **while loops**
- Controlling execution with **break**
- Skipping iterations with **continue**
- Working with **nested loops**
- Input validation
- Using dictionaries
- Calculating averages
- Building a practical Python application

---

# 📂 Project Structure

```text
student-grade-management-system/
│
├── README.md
├── disc3.py
├── StudentGradeManagement.exe
├── screenshots/
│   ├── output1.png
│   ├── output2.png
│   ├── output3.png
│   └── output4.png
└── LICENSE
```

---

# 📸 Screenshots

## Student List Display

*Insert Screenshot Here*

---

## Grade Entry and Validation

*Insert Screenshot Here*

---

## Student Grades and Average

*Insert Screenshot Here*

---

## Students Organized by Class

*Insert Screenshot Here*

---

# 👨‍💻 Author

**Sourab Ghosh**

**Course:** CS 1101 – Programming Fundamentals

**University:** University of the People

---

# 📜 License

This project is provided for educational purposes as part of a university programming assignment.

---

⭐ If you found this project useful or helpful, consider giving the repository a star!
