# Parent class
class User:
    def __init__(self, username):
        self.username = username

    def login(self):
        print(self.username, "has logged in.")


# Child class
class Student(User):
    def __init__(self, username, course):
        super().__init__(username)
        self.course = course

    def view_course(self):
        print(self.username, "is studying", self.course)


# Grandchild class
class TeachingAssistant(Student):
    def __init__(self, username, course, responsibility):
        super().__init__(username, course)
        self.responsibility = responsibility

    def assist_teaching(self):
        print(self.username, "is responsible for", self.responsibility)


# Creating object
ta = TeachingAssistant(
    "Shamillah",
    "Software Engineering",
    "Marking Assignments"
)

# Accessing inherited methods
ta.login()
ta.view_course()
ta.assist_teaching()