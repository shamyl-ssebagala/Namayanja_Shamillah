# Base class
class Vehicle:
    def __init__(self, registration_number, rental_price_per_day):
        self.registration_number = registration_number
        self.rental_price_per_day = rental_price_per_day

    def calculate_rental_cost(self, days):
        return self.rental_price_per_day * days

    def display_info(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Rental Price Per Day: UGX {self.rental_price_per_day}")


# Subclass Car
class Car(Vehicle):
    def __init__(self, registration_number, rental_price_per_day, seating_capacity):
        super().__init__(registration_number, rental_price_per_day)
        self.seating_capacity = seating_capacity

    def display_info(self):
        print("Car Information")
        print(f"Registration Number: {self.registration_number}")
        print(f"Rental Price Per Day: UGX {self.rental_price_per_day}")
        print(f"Seating Capacity: {self.seating_capacity}")


# Subclass Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, registration_number, rental_price_per_day, engine_capacity):
        super().__init__(registration_number, rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        print("Motorcycle Information")
        print(f"Registration Number: {self.registration_number}")
        print(f"Rental Price Per Day: UGX {self.rental_price_per_day}")
        print(f"Engine Capacity: {self.engine_capacity} cc")


# Creating objects
car1 = Car("UBA123A", 100000, 5)
bike1 = Motorcycle("UBD456B", 50000, 150)

# Display information
car1.display_info()
print("Rental Cost for 3 Days:", car1.calculate_rental_cost(3))

print()

bike1.display_info()
print("Rental Cost for 3 Days:", bike1.calculate_rental_cost(3))