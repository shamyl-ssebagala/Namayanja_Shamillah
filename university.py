# Base class
class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}")


# Subclass Student
class Student(Person):
    def __init__(self, name, id_number, major):
        super().__init__(name, id_number)
        self.major = major

    def display_details(self):
        super().display_details()
        print(f"Major: {self.major}")


# Subclass Lecturer
class Lecturer(Person):
    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")


# Creating objects
student1 = Student("Shamillah", "STU101", "Software Engineering")
lecturer1 = Lecturer("Dr. Kato", "LEC201", "Computer Science")

# Display details
print("Student Details")
student1.display_details()

print("\nLecturer Details")
lecturer1.display_details()
