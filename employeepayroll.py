# Parent class
class Employee:
    def __init__(self, name, employee_number):
        self.name = name
        self.employee_number = employee_number

    def calculate_pay(self):
        pass


# Child class for full-time employees
class FullTimeEmployee(Employee):
    def __init__(self, name, employee_number, monthly_salary):
        super().__init__(name, employee_number)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary


# Child class for part-time employees
class PartTimeEmployee(Employee):
    def __init__(self, name, employee_number, hours_worked, hourly_rate):
        super().__init__(name, employee_number)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        return self.hours_worked * self.hourly_rate


# Creating objects
full_time = FullTimeEmployee("Shamillah", "EMP001", 3000000)
part_time = PartTimeEmployee("Diana", "EMP002", 80, 15000)

# Display payroll information
print("Full-Time Employee")
print("Name:", full_time.name)
print("Employee Number:", full_time.employee_number)
print("Monthly Pay:", full_time.calculate_pay())

print("\nPart-Time Employee")
print("Name:", part_time.name)
print("Employee Number:", part_time.employee_number)
print("Monthly Pay:", part_time.calculate_pay())