print("Welcome to Week 1, Day 2!")

students = []

try:
    student_count = int(input("Enter number of students: "))

    for i in range(student_count):

        print("\nStudent", i + 1)

        name = input("Enter student name: ")

        # Validate marks
        while True:
            try:
                marks = float(input("Enter marks (0-100): "))

                if 0 <= marks <= 100:
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except Exception as e:
                print("Invalid marks. Please enter a number.")

        # Calculate grade
        if marks >= 90:
            grade = "A"

        elif marks >= 80:
            grade = "B"

        elif marks >= 70:
            grade = "C"

        elif marks >= 60:
            grade = "D"

        else:
            grade = "F"

        # Store student information
        student = {
            "name": name,
            "marks": marks,
            "grade": grade
        }

        students.append(student)

except Exception as e:
    print("Error:", e)


# Display all students
print("\n----- STUDENT RESULTS -----")

for student in students:
    print(
        "Name:", student["name"],
        "| Marks:", student["marks"],
        "| Grade:", student["grade"]
    )