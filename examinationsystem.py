# Parent class
class Learner:
    def __init__(self, name, reg_number):
        self.name = name
        self.reg_number = reg_number

    def calculate_final_grade(self):
        pass


# Child class Undergraduate
class Undergraduate(Learner):
    def __init__(self, name, reg_number, marks):
        super().__init__(name, reg_number)
        self.marks = marks

    def calculate_final_grade(self):
        return self.marks


# Child class Postgraduate
class Postgraduate(Learner):
    def __init__(self, name, reg_number, coursework_score, research_score):
        super().__init__(name, reg_number)
        self.coursework_score = coursework_score
        self.research_score = research_score

    def calculate_final_grade(self):
        return (self.coursework_score * 0.4) + (self.research_score * 0.6)


# Creating objects
undergrad = Undergraduate("Sarah", "UG101", 85)
postgrad = Postgraduate("John", "PG201", 80, 90)

# Displaying results
print("Undergraduate Student")
print("Name:", undergrad.name)
print("Registration Number:", undergrad.reg_number)
print("Final Grade:", undergrad.calculate_final_grade())

print()

print("Postgraduate Student")
print("Name:", postgrad.name)
print("Registration Number:", postgrad.reg_number)
print("Final Grade:", postgrad.calculate_final_grade())