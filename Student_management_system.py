# Student Marks Management System

def add_student(students):
    """
    Adds a student's name and marks to the list.
    """
    name = input("Enter the student's name: ")
    marks = float(input(f"Enter the marks for {name}: "))
    students.append({"name": name, "marks": marks})
    print(f"{name} added successfully!\n")


def view_students(students):
    """
    Displays the list of students with their marks.
    """
    if not students:
        print("No students found.\n")
        return

    print("\nName           | Marks")
    print("-----------------------")
    for student in students:
        print(f"{student['name']:15} | {student['marks']:.2f}")
    print()


def calculate_statistics(students):
    """
    Calculates and displays average, highest, and lowest marks.
    """
    if not students:
        print("No students found to calculate statistics.\n")
        return

    total = sum(student["marks"] for student in students)
    highest = max(students, key=lambda x: x["marks"])
    lowest = min(students, key=lambda x: x["marks"])
    average = total / len(students)

    print(f"\nStatistics:")
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Marks: {highest['marks']:.2f} ({highest['name']})")
    print(f"Lowest Marks: {lowest['marks']:.2f} ({lowest['name']})\n")


def save_to_file(students):
    """
    Saves the students and their marks to a file for persistence.
    """
    file_path = "students.txt"
    with open(file_path, "w") as file:
        for student in students:
            file.write(f"{student['name']},{student['marks']}\n")
    print(f"Students' data saved to '{file_path}'\n")


def load_from_file():
    """
    Loads students and their marks from a file if it exists.
    """
    try:
        students = []
        with open("students.txt", "r") as file:
            for line in file:
                name, marks = line.strip().split(",")
                students.append({"name": name, "marks": float(marks)})
        return students
    except FileNotFoundError:
        return []


def main():
    """
    Main menu for the Student Marks Management System.
    """
    students = load_from_file()
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Calculate Statistics")
        print("4. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            calculate_statistics(students)
        elif choice == "4":
            save_to_file(students)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
