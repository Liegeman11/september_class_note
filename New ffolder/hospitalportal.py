# class Patient:
#     users = {}

#     @staticmethod
#     def register_user():
#         while True:
#             username = input("Enter your name: ")
#             if not username:
#                 print("Name cannot be empty.")
#                 continue
            
#             treatment = input("Type of treatment: ")
#             if not treatment:
#                 print("Treatment cannot be empty.")
#                 continue
            
#             email = input("Enter your email: ")
#             if "@" not in email or "." not in email:
#                 print("Please enter a valid email address.")
#                 continue
            
#             Patient.users[username] = {
#                 'treatment': treatment,
#                 'email': email
#             }

#             print(f"User {username} registered successfully!")
#             another = input("Do you want to register another user? (yes/no): ").lower()
#             if another != 'yes':
#                 break

# class PatientBill:
#     room_rates = {
#         'General': 100,
#         'Semi-Private': 200,
#         'Private': 300
#     }

#     def __init__(self, name, room_type, days_stayed, treatment):
#         self.name = name
#         self.room_type = room_type
#         self.days_stayed = days_stayed
#         self.treatment = treatment
#         self.additional_services = 0

#     def add_services(self, amount):
#         """Add extra service cost"""
#         self.additional_services += amount

#     def calculate_total_bill(self):
#         """Calculate the total bill based on room type, days stayed, and additional services"""
#         room_cost = self.room_rates.get(self.room_type, 0) * self.days_stayed
#         total_bill = room_cost + self.additional_services
#         return total_bill

#     def display_bill(self):
#         """Display the total bill for the patient"""
#         total_bill = self.calculate_total_bill()
#         print(f"Patient Name: {self.name}")
#         print(f"Type of Treatment: {self.treatment}")
#         print(f"Room Type: {self.room_type}")
#         print(f"Days Stayed: {self.days_stayed}")
#         print(f"Additional Services: ${self.additional_services}")
#         print(f"Total Bill: ${total_bill:.2f}")

# if __name__ == "__main__":
#     Patient.register_user()
#     print("Registered patients:", Patient.users)


class Patient:
    users = {}

    def register_user():
        while True:
            username = input("Enter your name: ")
            if not username:
                print("Name cannot be empty.")
                continue
            
            treatment = input("Type of treatment: ")
            if not treatment:
                print("Treatment cannot be empty.")
                continue
            
            email = input("Enter your email: ")
            if "@" not in email or "." not in email:
                print("Please enter a valid email address.")
                continue
            
            Patient.users[username] = {
                'treatment': treatment,
                'email': email
            }

            print(f"User {username} registered successfully!")
            another = input("Do you want to register another user? (yes/no): ").lower()
            if another != 'yes':
                break

class PatientBill:
    room_rates = {
        'General': 100,
        'Semi-Private': 200,
        'Private': 300
    }

    def __init__(self, name, room_type, days_stayed, treatment):
        self.name = name
        self.room_type = room_type
        self.days_stayed = days_stayed
        self.treatment = treatment
        self.additional_services = 0

    def add_services(self, amount):
        """Add extra service cost"""
        self.additional_services += amount

    def calculate_total_bill(self):
        """Calculate the total bill based on room type, days stayed, and additional services"""
        room_cost = self.room_rates.get(self.room_type, 0) * self.days_stayed
        total_bill = room_cost + self.additional_services
        return total_bill

    def display_bill(self):
        """Display the total bill for the patient"""
        total_bill = self.calculate_total_bill()
        print(f"Patient Name: {self.name} Type of Treatment: {self.treatment} Room Type: {self.room_type}Days Stayed: {self.days_stayed} Additional Services: ${self.additional_services} Total Bill: ${total_bill:.2f}")

if __name__ == "__main__":
    Patient.register_user()
    print("Registered patients:", Patient.users)
    
    for username, details in Patient.users.items():
        room_type = input(f"Enter room type for {username} (General/Semi-Private/Private): ")
        days_stayed = int(input(f"Enter number of days stayed for {username}: "))
        bill = PatientBill(username, room_type, days_stayed, details['treatment'])
        bill.display_bill()
    display_bill = PatientBill





