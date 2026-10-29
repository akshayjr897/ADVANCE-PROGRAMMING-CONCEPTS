
class InvalidMarksException(Exception):
    pass


class StudentNotFoundException(Exception):
    pass


students = {
    101: {
        "name": "Shahuraj",
        "DAA": 85,
        "CC": 78,
        "Python": 92,
        "Java": 88
    }
}


try:
    id = int(input("Enter Student Id Name : "))

    if id not in students:
        raise StudentNotFoundException("Student not found")

    student = students[id]

    print("Name:", student["name"])

    for subject in ["DAA", "CC", "Python", "Java"]:
        try:
            marks = int(input("Enter " + subject + " marks: "))

            if marks < 0 or marks > 100:
                raise InvalidMarksException("Marks must be between 0 and 100")

            student[subject] = marks

        except ValueError:
            print("Please enter numbers only")

        except InvalidMarksException as e:
            print(e)

    total = (
        student["DAA"] +
        student["CC"] +
        student["Python"] +
        student["Java"]
    )

    percentage = total / 4

    print("\n----- RESULT -----")
    print("Name:", student["name"])
    print("DAA:", student["DAA"])
    print("CC:", student["CC"])
    print("Python:", student["Python"])
    print("Java:", student["Java"])
    print("Total:", total)
    print("Percentage:", percentage)

except ValueError:
    print("Invalid Student ID")

except StudentNotFoundException as e:
    print(e)

finally:
    print("Program completed")