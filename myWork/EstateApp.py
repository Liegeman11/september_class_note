# name_email=input[("Enter your name: "), input('Enter your email address: ')]
# print('Passwords do not match! Try again.')
        # return
        
registered_clients = {}

def profile():
    print("""\n=== About Us ===
Liegeland Real Estate is a trusted and innovative company dedicated to providing secure, transparent, and sustainable property solutions...
Our Divisions:
1. Liegeland Properties
2. Liegeland Development
3. Liegeland Investment
...
""")


def sign_up():
    print("\n=== Sign Up ===")
    name = input("Enter your full name: ")
    while True:
        email = input("Enter your email address: ").lower().strip()
        if "@" in email and email.endswith(".com"):
            print("✅ Valid email... continue the registration")
            break
        else:
            print("⚠️ Invalid email... try again")
    address = input("Enter your Address: ")
    state = input("Enter your state of origin: ")
    lga = input("Enter your local government area: ")
    country = input("Enter your country: ")
    occupation = input("Enter your occupation: ")
    nin = input("Enter your NIN No.: ")
    while True:
        password = input("Enter password: ")
        confirmed_password = input("Confirm password: ")
        if password == confirmed_password:
            break
        else:
            print("⚠️ Passwords do not match! Try again.")
    registered_clients[email] = {
        "Name": name,
        "Email": email,
        "Address": address,
        "State": state,
        "LGA": lga,
        "Country": country,
        "Occupation": occupation,
        "NIN": nin,
        "Password": password
    }
    print("✅ Registration successful!")

def sign_in():
    print("\n=== Sign In ===")
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    if email in registered_clients and registered_clients[email]["Password"] == password:
        print(f"✅ Welcome back, {registered_clients[email]['Name']}!")
    else:
        print("❌ Invalid email or password.")

def landing_page():
    while True:
        print("""\n=== Welcome to Liegeland Real Estate Company ===
Motto: Land of promise, Built on loyalty, Guided by Pride
1. Company Profile
2. Sign In
3. Sign Up
4. Exit
""")
        choice = input("Enter your Option: ").strip()

        if choice == "1":
            profile()
        elif choice == "2":
            sign_in()
        elif choice == "3":
            sign_up()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid selection! Please enter 1-4.")

landing_page()



# registered_clients = {} 

# def profile():
#     print("""                               About Us
# Liegeland Real Estate is a trusted and innovative real estate company dedicated to providing secure, transparent, and sustainable property solutions...
# Our Divisions:
# 1. Liegeland Properties
# 2. Liegeland Development
# 3. Liegeland Investment
# ...
# """)

# def sign_up():
#     print("=== Sign Up ===")
#     Name = input('Enter your full name: ')
#     Email = input('Enter your email: ')
#     while True:
#         email = input("Enter your email address: ").lower().strip()
#         if "@" in email and email.endswith(".com"):
#             print("✅ Valid email... continue the registration")
#             break
#         else:
#             print("⚠️ Invalid email... try again")
#         if Email in registered_clients:
#             print(f'{Email} already exists. Please choose another one.')
#             return
#     Address = input('Enter your Address: ')
#     State_of_origin = input('Enter your state of origin: ')
#     LGA = input('Enter your local government area: ')
#     Country = input('Enter your country: ')
#     Occupation = input('Enter your occupation: ')
#     identification = input('Enter your NIN No.: ')
#     password = input('Enter password: ')
#     confirmed_password = input("Confirm your password: ")
#     while True:
#         if password != confirmed_password:
#             print('the password do not match! confirmed the password again and make sure they are the same.')
#         break
#     registered_clients[Email] = {
#         'Name': Name,
#         'Address': Address,
#         'State_of_origin': State_of_origin,
#         'LGA': LGA,
#         'Country': Country,
#         'Occupation': Occupation,
#         'NIN': identification,
#         'Password': password
#     }
#     print('Registration successful!')

# def sign_in():
#     print("=== Sign In ===")
#     Email = input('Enter your Email: ')
#     Password = input('Enter your password: ')
    
#     if Email in registered_clients and registered_clients[Email]['Password'] == Password:
#         print(f'Welcome back, {registered_clients[Email]["Name"]}!')
#     else:
#         print('Invalid Email or password.')

# def landing_page():
#     while True:
#         print("""\nWelcome to Liegeland Real Estate Company
# Motto: Land of promise, Built on loyalty, Guided by Pride
# 1. Company Profile
# 2. Sign In
# 3. Sign Up
# 4. Exit""")
        
#         User_option = input("Enter your Option: ").strip()
#         if User_option == '1':
#             profile()
#         elif User_option == "2":
#             sign_in()
#         elif User_option == "3":
#             sign_up()
#         elif User_option == '4':
#             print("Exiting... Goodbye!")
#             break
#         else:
#             print('Invalid selection! Please enter a valid option (1-4)')
# landing_page()




import json

# ===============================
# Data Storage
# ===============================
registered_clients = {}
properties = {}

# ===============================
# Persistence Functions
# ===============================
def save_data():
    with open("clients.json", "w") as f:
        json.dump(registered_clients, f, indent=4)
    with open("properties.json", "w") as f:
        json.dump(properties, f, indent=4)

def load_data():
    global registered_clients, properties
    try:
        with open("clients.json", "r") as f:
            registered_clients = json.load(f)
    except FileNotFoundError:
        registered_clients = {}

    try:
        with open("properties.json", "r") as f:
            properties = json.load(f)
    except FileNotFoundError:
        properties = {}

# ===============================
# Company Profile
# ===============================
def profile():
    print("""\n                               About Us
    Liegeland Real Estate is a trusted and innovative real estate company dedicated to providing secure, transparent, and sustainable property solution. 
    We specialize in land sales, housing development, property investment, rentals, and facility management, serving individuals, families, business, and investors worldwide.

    Our goal is to make real estate ownership and investment accessible to everyone, while ensuring maximum value and trust in every transaction.

                        Our Divisions
    1. Liegeland Properties
    2. Liegeland Development
    3. Liegeland Investment
    4. Liegeland Facility Management
    5. Liegeland Mortgage & Finance
    6. Liegeland Global (Diaspora Services)
    7. Liegeland Agro-Realty
    8. Liegeland Interior & Smart Homes
    9. Liegeland Legal & Consultancy
    10. Liegeland Rentals & Leasing  
    """)
email=input9
if '@' in email and email.endswith('.com'):
    print('valid email. you can continue with your registration')
# ===============================
# User Registration
# ===============================
def sign_up():
    Name = input('Enter your full name: ')
    while True:
        email = input('Enter your email: ')
        if email in registered_clients:
            print(f'{email} already exists, please choose another one.')
            continue
        if '@' in email and email.endswith('.com'):
            print('Valid email... continue the registration')
            break
        else:
            print('Invalid email, enter the right email address')

    Address = input('Enter your Address: ')
    State_of_origin = input('Enter your state of origin: ')
    lga = input('Enter your local government area: ')
    Occupation = input('Enter your occupation: ')
    Country = input('Enter your country: ')
    identification = input('Enter your NIN No.: ')

    while True:
        password = input('Enter password: ')
        confirmed_password = input("Confirm your password again: ")
        if password == confirmed_password:
            break
        else:
            print('Passwords do not match! Try again.')

    registered_clients[email] = {
        'Name': Name,
        'Email': email,
        'Address': Address,
        'State_of_origin': State_of_origin,
        'lga': lga,
        'Occupation': Occupation,
        'Country': Country,
        'identification': identification,
        'Password': password
    }
    save_data()
    print(f'Registration successful! Welcome, {Name}')

# ===============================
# User Login
# ===============================
def sign_in():
    attempts = 3
    while attempts > 0:
        email = input("Enter your email: ")
        password = input('Enter your password: ')
        if email in registered_clients and registered_clients[email]['Password'] == password:
            print(f"Welcome back, {registered_clients[email]['Name']}!")
            return email  # Return logged-in user email
        else:
            attempts -= 1
            if attempts > 0:
                print(f'Invalid email or password. You have {attempts} attempt(s) left.')
            else:
                print("Sorry, you have been locked out due to multiple failed attempts.")
    return None

# ===============================
# Property Management
# ===============================
def add_property():
    property_id = str(len(properties) + 1)
    title = input("Enter property title: ")
    location = input("Enter property location: ")
    price = input("Enter property price: ")
    status = "Available"

    properties[property_id] = {
        "Title": title,
        "Location": location,
        "Price": price,
        "Status": status
    }
    save_data()
    print("Property added successfully!")

def view_properties():
    if not properties:
        print("No properties available at the moment.")
        return
    print("\nAvailable Properties:")
    for pid, details in properties.items():
        print(f"ID: {pid} | Title: {details['Title']} | Location: {details['Location']} | Price: {details['Price']} | Status: {details['Status']}")

# ===============================
# Landing Page
# ===============================
def landing_page():
    load_data()
    while True:
        print("""\n           Welcome to Liegeland Real Estate Company
                    Motto: Land of promise, Built on loyalty, Guided by Pride
                1. Company Profile
                2. Register (Sign Up)
                3. Login (Sign In)
                4. View Properties
                5. Add Property (Admin Only)
                6. Exit    """)
        User_option = input("Enter your Option: ").strip()

        if User_option == '1':
            profile()
        elif User_option == "2":
            sign_up()
        elif User_option == "3":
            sign_in()
        elif User_option == "4":
            view_properties()
        elif User_option == "5":
            add_property()
        elif User_option == '6':
            print("Exiting system... Goodbye!")
            break
        else:
            print('Invalid selection! Please enter a valid option (1-6)')

# ===============================
# Run Program
# ===============================
landing_page()

