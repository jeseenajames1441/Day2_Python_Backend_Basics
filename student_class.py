class Student:
    def __init__(self, name, age, student_class):
        self.name = name
        self.age = age
        self.student_class = student_class

    def show_details(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Class:", self.student_class)

s1 = Student("Mariya", 22, "B com")
s1.show_details()

s2 = Student("Anju", 22, "BBA")
s2.show_details()

s3 = Student("Jobin", 22, "BCA")
s3.show_details()