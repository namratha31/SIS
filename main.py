import json
import os

DATA_FILE = "students.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_student():
    students = load_data()

    student = {
        "name": input("Student Name: "),
        "usn": input("USN: "),
        "father_name": input("Father Name: "),
        "mother_name": input("Mother Name: "),
        "date_of_joining": input("Date of Joining (DD-MM-YYYY): "),
        "year_of_graduation": input("Year of Graduation: "),
        "fees_paid": input("Fees Paid (Yes/No): "),
        "attendance": input("Attendance (%): "),
        "marks": input("Marks: ")
    }

    students.append(student)
    save_data(students)
    print("✅ Student added successfully")


def view_students():
    students = load_data()
    if not students:
        print("❌ No students found")
        return

    for i, student in enumerate(students, start=1):
        print(f"\nStudent {i}")
        for key, value in student.items():
            print(f"{key.replace('_', ' ').title()}: {value}")


def main():
    while True:
        print("\n--- Student Information System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Bye 👋")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
