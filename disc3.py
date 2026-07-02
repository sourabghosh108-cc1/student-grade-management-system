
# Question 1: Student List
students = ["Alice", "Ben", "Chloe", "David"]

print("=" * 50)
print("STUDENT GRADE MANAGEMENT SYSTEM")
print("=" * 50)

print("\nStudent List:")
for student in students:
    print(f"- {student}")

# Question 2 & Question 3:
# Enter grades using a while loop
# Use break and continue for control

grades = {}

print("\nEnter grades for each student.")
print("Type 'stop' at any time to end grade entry.")

for student in students:

    while True:

        grade_input = input(f"Enter grade for {student}: ")

        # Break Statement
        if grade_input.lower() == "stop":
            print("\nGrade entry stopped by the teacher.")
            break

        try:
            grade = float(grade_input)

        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
            continue

        # Continue Statement
        if grade < 0:
            print("Invalid grade. Negative grades are not allowed.")
            continue

        grades[student] = grade
        print(f"Grade recorded for {student}: {grade}")

        break

    if grade_input.lower() == "stop":
        break

# Display Recorded Grades
if grades:

    print("\n" + "=" * 50)
    print("STUDENT GRADES")
    print("=" * 50)

    for student, grade in grades.items():
        print(f"{student}: {grade}")

    average = sum(grades.values()) / len(grades)

    print("\n" + "=" * 50)
    print(f"Class Average: {average:.2f}")
    print("=" * 50)

else:
    print("\nNo grades were entered.")

# Question 4: Nested Loops

classes = [
    ["Alice", "Ben"],
    ["Chloe", "David"]
]

print("\n" + "=" * 50)
print("STUDENTS ORGANIZED BY CLASS")
print("=" * 50)

for class_number, classroom in enumerate(classes, start=1):

    print(f"\nClass {class_number}")

    for student in classroom:
        if student in grades:
            print(f"{student}: {grades[student]}")
        else:
            print(f"{student}: No Grade Recorded")

print("\nProgram Completed Successfully.")
input("\nPress Enter to exit...")

