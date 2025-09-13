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



