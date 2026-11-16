# Student Grades Management System

student_grades = {}

def give(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a grade of {grade}")

def update(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s marks are updated to {grade}")
    else:
        print(f"{name} is not found!")

def delete(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found!")

def display_details():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No students found!")

def main():
    while True:
        print("\nStudent Grades")
        print("1. Add student details")
        print("2. Update details")
        print("3. Delete details")
        print("4. View details")
        print("5. EXIT")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter student name: ")
            grade = int(input("Enter student grades: "))
            give(name, grade)

        elif choice == 2:
            name = input("Enter student name: ")
            grade = int(input("Enter student grades: "))
            update(name, grade)

        elif choice == 3:
            name = input("Enter student name: ")
            delete(name)

        elif choice == 4:
            display_details()

        elif choice == 5:
            print("THANK YOU")
            break

        else:
            print("Invalid choice!")

# Start the program
main()