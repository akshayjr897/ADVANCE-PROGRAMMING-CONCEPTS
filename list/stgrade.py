names = []
grades = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    grade = int(input("Enter grade: "))
    names.append(name)
    grades.append(grade)

print("Students:", names)
print("Grades:", grades)

name = input("Enter new student name: ")
grade = int(input("Enter new grade: "))
names.append(name)
grades.append(grade)

print("Updated:", names, grades)

name = input("Enter student name to update: ")
if name in names:
    i = names.index(name)
    grades[i] = int(input("Enter new grade: "))

print("Updated grades:", grades)

name = input("Enter student name to remove: ")
if name in names:
    i = names.index(name)
    names.pop(i)
    grades.pop(i)

print("Students:", names)
print("Grades:", grades)

if grades:
    print("Average:", sum(grades) / len(grades))
    print("Highest grade:", max(grades))
    print("Lowest grade:", min(grades))