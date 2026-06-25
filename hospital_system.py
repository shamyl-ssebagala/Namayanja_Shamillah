# Parent class
class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id

    def clock_in(self):
        print(self.name, "has clocked in.")


# Child class: Doctor
class Doctor(Staff):
    def __init__(self, name, staff_id, specialty):
        super().__init__(name, staff_id)
        self.specialty = specialty

    def diagnose_patient(self):
        print(self.name, "is diagnosing patients.")


# Child class: Nurse
class Nurse(Staff):
    def __init__(self, name, staff_id, ward):
        super().__init__(name, staff_id)
        self.ward = ward

    def assist_patients(self):
        print(self.name, "is assisting patients in", self.ward, "ward.")


# Child class: Pharmacist
class Pharmacist(Staff):
    def __init__(self, name, staff_id, license_number):
        super().__init__(name, staff_id)
        self.license_number = license_number

    def dispense_medicine(self):
        print(self.name, "is dispensing medicine.")


# Creating objects
doctor = Doctor("Dr. Grace", "D101", "Cardiology")
nurse = Nurse("Mary", "N102", "Emergency")
pharmacist = Pharmacist("James", "P103", "LIC789")

# Demonstration
doctor.clock_in()
doctor.diagnose_patient()

nurse.clock_in()
nurse.assist_patients()

pharmacist.clock_in()
pharmacist.dispense_medicine()