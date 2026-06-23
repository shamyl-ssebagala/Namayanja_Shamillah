class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"User Profile: {self.first_name} {self.last_name}, "
              f"Age: {self.age}, Email: {self.email}, Location: {self.location}")

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome back!")


user1 = User("Shamyla", "Ssebagala", 25, "shamy@gmail.com", "Kampala")
user2 = User("Gael", "Musoke", 30, "gael@gmail.com", "Masaka")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()
