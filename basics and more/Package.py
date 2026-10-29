

def student_details():
    print("\nSTUDENT INFORMATION")

    name = input("Enter student Name: ")
    class_name = input("Enter student Class: ")
    mobile = input("Enter student Mobile Number: ")

    print("\nName:", name)
    print("Class:", class_name)
    print("Mobile Number:", mobile)


def exam_details():
    print("\nEXAMINATION INFORMATION")

    marks = []

    for i in range(1, 7):
        mark = float(input("Enter marks for Semester " + str(i) + ": "))
        marks.append(mark)

    average = sum(marks) / len(marks)

    print("\nSEMESTER MARKS")

    for i in range(6):
        print("Semester", i + 1, ":", marks[i])

    print("\nCumulative Average:", round(average, 2))

    if average >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")


print("akshay")
print("vishuu")
print("Sneha")

student_details()
exam_details()