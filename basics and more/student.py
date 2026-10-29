import json

students = []
grades = []

try:
    with open("students.json", "r") as file:
        data = json.load(file)
        students = data["students"]
        grades = data["grades"]
except FileNotFoundError:
    pass

def save_data():
    data = {
        "students": students,
        "grades": grades
    }
    with open("students.json", "w") as file:
        json.dump(data, file)

def add_student(name, grade):
    students.append(name)
    grades.append(grade)
    save_data()

def update_grade(name, new_grade):
    if name in students:
        index = students.index(name)
        grades[index] = new_grade
        save_data()
    else:
        print("Student not found.")

def remove_student(name):
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        save_data()
    else:
        print("Student not found.")

def calculate_average():
    if grades:
        print("Average Grade:", sum(grades) / len(grades))
    else:
        print("No grades available.")

def display_extremes():
    if grades:
        print("Highest Grade:", max(grades))
        print("Lowest Grade:", min(grades))
    else:
        print("No grades available.")

def display_students():
    if students:
        for i in range(len(students)):
            print(students[i], ":", grades[i])
    else:
        print("No students available.")

while True:
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Calculate Average")
    print("5. Display Highest and Lowest")
    print("6. Display Students")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = float(input("Enter grade: "))
        add_student(name, grade)

    elif choice == "2":
        name = input("Enter student name: ")
        grade = float(input("Enter new grade: "))
        update_grade(name, grade)

    elif choice == "3":
        name = input("Enter student name: ")
        remove_student(name)

    elif choice == "4":
        calculate_average()

    elif choice == "5":
        display_extremes()

    elif choice == "6":
        display_students()

    elif choice == "7":
        break

    else:
        print("Invalid choice.")