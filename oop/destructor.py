class Student:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")

s1 = Student()
del s1