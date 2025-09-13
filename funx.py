# def landing_page():
#     print("""
#                         1.Login
#                         2.register
#                         3.make enquiry
#                         4.exit
#         """)
#     user=input('select option>>>> ')
#     if user == '1':
#         print('welcome')
#     elif user == '2':
#         print('welcome!!! you can now register ')
#     elif user == '3':
#         print('what do you want? ')
#     elif user == '4':
#         exit()
# landing_page()

# 3. Feedback
# client={}
# import json

# def save_data():
#     with open("clients.json", "w") as f:
#         json.dump(registered_clients, f)

# def load_data():
#     global registered_clients
#     try:
#         with open("clients.json", "r") as f:
#             registered_clients = json.load(f)
#     except FileNotFoundError:
#         registered_clients = {}
# registered_clients ={}
# def profile():
#     print("""                               About Us
#             Liegeland Real Estate is a trusted and innovative real estate company dedicated to providing secure, transparent, and sustainable property solution. We specialize in land sales, housing development, property investment, rentals, and facility management, serving individuals, families, business, and investors worldwide.
#             Our goals is to make real estate ownership and investment accessible to everyone, while ensuring maximum value and trust in every transaction.\n
#                         Our Division\n
#             1. Liegeland properties
#             2. Liegland Development
#             3. Liegeland Investment
#             4. Liegeland Facility Management
#             5. Liegeland Mortgage & Finance
#             6. Liegeland Global(Diaspora Services)
#             7. Liegeland Agro-Realty
#             8. Liegeland Interior & Smart & Homes
#             9. Liegeland Legal & Consultancy
#             10. liegeland Rentals & Leasing  
    
#     """)
# def sign_up():
#     Name=input('Enter your full name: ')
#     while True:
#         email=input('Enter your email: ')
#         if email in registered_clients:
#             print(f'{email}  already exits, Please choose another one.')
#         if '@' in email and email.endswith('.com'):
#             print('Valid email... continue the registration')
#             break
#         else:
#             print('Invalid email, enter the right email address')
            
#     Address=input('Enter your Address: ')
#     State_of_origin=input('Enter your state of origin: ')
#     lga=input('Enter your local government area: ')
#     Occupation=input('Enter your occupation: ')
#     Country=input('Enter your country: ')
#     identification=input('Enter your NIN No.: ')
#     while True:
#         password= input('Enter password: ')
#         confirmed_password=input("Confirmed your password again: ")
#         if password == confirmed_password:
#             break
#         else:
#             print('the password do not match! confirmed the password again.')
#     registered_clients[email]= {'Name': Name,
#                                 'Email': email,
#                                 'Address': Address,
#                                 'State_of_origin': State_of_origin,
#                                 'lga':lga,
#                                 'Occupation':Occupation,
#                                 'Country':Country,
#                                 'identification':identification,
#                                 'Password':password
#                                 }
#     save_data()
#     print('Registration successful!', registered_clients)
# def User_dashboard(email):
#     while True:
#         print(f""" \nUSER DASHBOARD 
# Your are welcome back, {registered_clients[email]['Name']}({email})!!!
# 1. View Profile
# 2. Liegeland Properties
# 3. Liegeland Investment
# 4. Liegeland Rentals & Leasing
# 5. contact customer services
# 6. Logout 


# """)

#         choice=input('Enter your option: ').strip()
#         if choice=='1':
#             User=registered_clients[email]
#             print(f"""\n MY PROFILE
#             Name:{User['Name']}
#             Email: {User['Email']}
#             Address: {User['Address']}
#             State_of_origin: {User['State_of_origin']}
#             lga: {User['lga']}
#             Occupation: {User['Occupation']}
#             Country: {User['Country']}
#             identification: {User['identification']}

# """)
#         elif choice=='2':
#             print("""\n--- Available Properties ---
#  1. 2-Bedroom Apartment in Abuja - $90,000
#  2. 3-Bedroom Apartment in Abuja - $110,000
#  3. 2-Bedroom Apartment in Lagos - $80,000
#  4. 3-Bedroom Apartment in Lagos - $100,000
#  5. 4-Bedroom Duplex in Abuja - $150,000
#  6. 3-Bedroom Duplex in Lagos - $120,000
#  7. 4-Bedroom Duplex in Lagos - $140,000
#  8. 3-Bedroom Duplex in Abuja - $130,000
#  9. Farmland in Ondo State (1 acre) - $15,000
# 10. Farmland in Ogun State (1 acre) - $12,000
# 11. Farmland in Edo State (1 acre) - $18,000
# 12. Farmland in Ekiti State (1 acre) - $10,000
# """)
#         elif choice =='3':
#             print("""\n--- Investment Plans ---
#             1. Real Estate Trust Fund - Minimum $5,000
#             2. Agro-Realty Investment - Minimum $2,000
#             3. Diaspora Housing Scheme - Minimum $10,000
# """)
#         elif choice =='4':
#             pas
#         elif choice =='5':
#             print("""\n     📞 OUR CUSTOMER SERVICES:
#                         EMAIL:supportliegeman@gmail.com
#                         PHONE:+234 9076320814
#                         whatsapp NO.:+234 8145745656
# """)
#         elif choice =='6':
#             print('Logging out... Returning to main menu.')
#             break
#         else:
#             print("Invalid selection! please enter a valid option(1-4)")
        
# def sign_in():
#     attempts=3
#     while attempts > 0:
#         email= input("Enter your email: ")
#         password= input('Enter your password: ')
#         if email in registered_clients and registered_clients[email]['Password']== password:
#             print(f'{registered_clients[email]['Name']}, wellcome back')
#             User_dashboard(email)
#             return
#         else:
#             attempts-=1
#             if attempts > 0:
#                 print(f'Invalid username or password. you have {attempts} attempt(s) left')
#             else:
#                 print(f"Sorry, you have been locked out due to multiple failed attempts.")
                
#         if attempts==0:
#             continue

# def landing_page():
#     while True:
#         print("""           Welcome to Liegeland Real Estate Company
#                     Motto: Land of promise, Built on loyalty, Guided by Pride
#                 1. Company Profile
#                 2. sign up
#                 3. sign in
#                 4. Exit    """)
#         User_option=input( "Enter your Option: ").strip()
#         if User_option =='1':
#             profile()
#         elif User_option == "2":
#             sign_up()
#         elif User_option =="3":
#             sign_in()
#         elif User_option =='4':
#             break
#         else:
#             print('Invalid selection! Please enter a valid option(1-4)')
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



# z=10

# def add_num(x): 
#     global b
#     b=3
#     q=18  #local variable
#     sum_all= x + 6 + z + q + b
#     print(sum_all)
# add_num(4)

# def add_num(x, y):
#     sum_all= x + 6 + y + x + z + b
#     print(sum_all)
# add_num(4, 2)

# def subtract_num(i, j):
#     sub_all= i - 6 - j + j
#     print(sub_all)
# subtract_num(28, 3)

# """
# types of arguments
# 1. default args
# 2. keyword args
# 3. psitional args
# 4. arbitrary args
# """

# ## 1. default args
# def add_num(x, y=10):
#     global b
#     b=3
#     q=18  #local variable
#     sum_all= x + 6 + z + q + b
#     print(sum_all)
# add_num(4)

# def add_num(x=10, y=3):
#     global b
#     b=3
#     q=18  #local variable
#     sum_all= x + 6 + z + q + b +y
#     print(sum_all)
# add_num(4)

## 2. keyword args

# def college(name, location):
#     print(name, location)
    
# college(name='SQI', location='Yoaco')
# college(location='Yoaco', name='SQI')

# ## 3. positional args
# def college_class(college, level):
#     print(f'My name is Bolu I study at {college} and my level is {level}')

# college_class('SQI','level2')
# college_class('level2','SQI')

# ## 4. arbitrary args
# def college_class(**kwargs):
#     print(kwargs.keys())
#     print(kwargs.values())

# college_class(name='SQI', level='level2', address='home',name2='titi',name3='dara' )
# college_class('level2','SQI')



#               functions             #
#  func is a block of code that does a particular task


