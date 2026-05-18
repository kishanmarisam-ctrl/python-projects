# student marks manager #

student_name = {"kishan": 85,
                "ramesh": 90,
                "suresh": 78}


def add_student_mark(name, mark):
    student_name[name] = mark
    print(f"Added {name} with mark {mark}.")


def view_student_mark(name):
    if name in student_name:
        print(f"{name} has a mark of {student_name[name]}.")
    else:
        print(f"{name} not found.")


def view_all_students():
    if student_name:
        print("All students and their marks:")
        for name, mark in student_name.items():
            print(f"{name}: {mark}")
    else:
        print("No students found.")


def delete_student_mark(name):
    if name in student_name:
        del student_name[name]
        print(f"Deleted {name} from records.")
    else:
        print(f"{name} not found.")


while True:
    print("\nStudent Marks Manager")
    print("1. Add Student Mark")
    print("2. View Student Mark")
    print("3. View All Students")
    print("4. Delete Student Mark")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter student name: ")
        mark = float(input("Enter student mark: "))
        add_student_mark(name, mark)
    elif choice == '2':
        name = input("Enter student name: ")
        view_student_mark(name)
    elif choice == '3':
        view_all_students()
    elif choice == '4':
        name = input("Enter student name: ")
        delete_student_mark(name)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
