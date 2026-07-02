# 🎓 Student Grade Management Program

A Python-based student grade management application developed for **CS 1101 – Programming Fundamentals (Unit 3)**. This project demonstrates the practical implementation of **for loops, while loops, break statements, continue statements, nested loops, input validation, and average grade calculation** within a real-world educational scenario.

---

## 📋 Features

* Display student names using **for loops**
* Record grades using **while loops**
* Stop grade entry using **break**
* Skip invalid grades using **continue**
* Validate user input
* Calculate class averages
* Organize students by class using **nested loops**
* Console-based interface
* Beginner-friendly Python implementation

---

## 🛠 Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python 3.x | Core programming language |
| VS Code    | Development environment   |
| Git        | Version control           |
| GitHub     | Source code hosting       |

---

## 📦 Installation

### Option 1: Clone Repository

```bash
git clone https://github.com/USERNAME/student-grade-management.git

cd student-grade-management
```

---

### Debian / Ubuntu / Linux Mint

Install Python:

```bash
sudo apt update

sudo apt install python3 python3-pip -y
```

Verify installation:

```bash
python3 --version
```

Run program:

```bash
python3 student_grade_management.py
```

---

### Fedora

Install Python:

```bash
sudo dnf install python3 -y
```

Verify installation:

```bash
python3 --version
```

Run program:

```bash
python3 student_grade_management.py
```

---

### Arch Linux / Manjaro

Install Python:

```bash
sudo pacman -S python
```

Verify installation:

```bash
python --version
```

Run program:

```bash
python student_grade_management.py
```

---

## ⬇ Download Executable

If you do not wish to install Python, download the standalone executable:

**Google Drive Download**

https://drive.google.com/file/d/YOUR_FILE_ID/view

After downloading:

### Windows

```text
Double-click StudentGradeManagement.exe
```

### Linux

```bash
chmod +x StudentGradeManagement

./StudentGradeManagement
```

---

## 🚀 Usage

Run the application:

```bash
python3 student_grade_management.py
```

The program will:

1. Display all student names.
2. Accept grade input.
3. Validate entries.
4. Skip invalid grades.
5. Allow early termination.
6. Calculate class average.
7. Display students organized by class.

---

## 💻 Sample Output

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

## 📂 Project Structure

```text
student-grade-management/
│
├── README.md
├── student_grade_management.py
├── StudentGradeManagement.exe
└── screenshots/
    └── sample-output.png
```

---

## 🎯 Learning Outcomes

This project demonstrates the ability to:

* Explain how for loops iterate over sequences.
* Discuss while loop structures.
* Apply break and continue statements.
* Create nested loop structures.
* Validate user input.
* Build a practical Python application.
* Apply programming concepts to a real-world educational scenario.

---

## 📚 Assignment Concepts Covered

| Unit 3 Concept      | Implemented |
| ------------------- | ----------- |
| For Loop            | ✅           |
| While Loop          | ✅           |
| Break Statement     | ✅           |
| Continue Statement  | ✅           |
| Nested Loop         | ✅           |
| Input Validation    | ✅           |
| Average Calculation | ✅           |

---

## 👨‍💻 Author

**Sourab Ghosh**

CS 1101 – Programming Fundamentals

University of the People

---

## 📜 License

This project is provided for educational purposes as part of a university programming assignment.
