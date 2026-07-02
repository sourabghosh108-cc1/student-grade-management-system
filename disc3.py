# Student Grade Management Program

students = ["Alice", "Ben", "Chloe", "David"]

# Question 1: Display student names using a for loop
print("Student List:")
for student in students:
    print(f"- {student}")

# Question 2 and Question 3: Enter grades using a while loop
grades = []

while True:
    grade = input("\nEnter a grade, type 'next' to finish grades, or 'stop' to quit: ")

    if grade.lower() == "stop":
        print("Grade entry stopped by the teacher.")
        break

    if grade.lower() == "next":
        print("Moving to the next section.")
        break

    try:
        grade = float(grade)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if grade < 0:
        print("Invalid grade. Negative grades are not allowed.")
        continue

    grades.append(grade)
    print(f"Grade recorded: {grade}")

# Calculate average if grades were entered
if grades:
    average = sum(grades) / len(grades)
    print(f"\nClass Average: {average:.2f}")

# Question 4: Organize students by class using nested loops
classes = [["Alice", "Ben"], ["Chloe", "David"]]

print("\nStudents Organized by Class:")
for class_number, classroom in enumerate(classes, start=1):
    print(f"\nClass {class_number}")

    for student in classroom:
        print(f"Student: {student}")

input("\nPress Enter to exit...")
