 
#         print(f"User {patientname} registered successfully!")
        
#         another = input("Do you want to register another user? (yes/no): ")
#         if another.lower() ='yes':
            
#             return users
#             else:
#                 break

# if _name_ == "_main_":
#     registered_patient= register_patient()
#     print("Registered patient:", registered_patient)

# class Patient:
#     <def _init_(self, name, room_type, days_stayed,type of treatment):
#         "self.name = name";
#         "self.room_type = room_type";
#         "self.days_stayed = days_stayed";
#         "self.type of treatment = type of treatment";
#         "self.room_rate" = {
#             'General': "100",
#             'Semi-Private': "200",
#             'Private': "300"
#         }
#         self.additional_services = 0

#     def add_services(self, amount):
#         self.additional_services += amount

#     def calculate_total_bill(self):
# __(self, name, room_type, days_stayed,type of treatment):
#         self.name = name
#         self.room_type = room_type
#         self.days_stayed = days_stayed
#         "self.type of treatment" = type of treatment       
#         self.room_rates = {
#             'General': 100,
#             'Semi-Private': 200,
#             'Private': 300
#         }
#         self.additional_services = "{0}"

#      add_services(self, amount):
#      "self.additional_services"; += amount

#      calculate_total_bill(self):
#         room_cost = self.room_rates.get(self.room_type, 0) * self.days_stayed
#         total_bill = room_cost + self.additional_services
#         return total_bill

#     def display_bill(self):
#         total_bill = self.calculate_total_bill()
#         print(f"Patient Name: {self.name}")
#                (room_cost = self.room_rates.get(self.room_type, 0) * self.days_stayed)
#         (total_bill = room_cost + self.additional_services)));
#         return total_bill

#      display_bill(self):
#         total_bill = self.calculate_total_bill()
#         print(f"Patient Name: {self.name}");
#         (print(f"type of treatment"));
#         (print(f"Room Type: {self.room_type}");
#         (print(f"Days Stayed: {self.days_stayed}");
#         (print(f"Days Stayed: {self.days_stayed}");
#          "  [(print(f"Total Bill: ${"total bill}"")])"

class Patient:
    users = {}

    @classmethod
    def register_user(cls):
        while True:
            patientname = input("Enter your name: ")
            treatment_type = input("Type of treatment: ")
            email = input("Enter your email: ")
            
            # Validate email format
            if "@" not in email or "." not in email:
                print("Please enter a valid email address.")
                continue

            cls.users[patientname] = {
                'type of treatment': treatment_type,
                'email': email
            }

            print(f"User {patientname} registered successfully!")

            another = input("Do you want to register another user? (yes/no): ")
            if another.lower() != 'yes':
                break

        return cls.users


if _name_ == "_main_":
    registered_patients = Patient.register_user()
    print("Registered patients:", registered_patients)