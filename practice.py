# num_str = "100"
# # num_int = int(num_str)
# num_int = float(num_str)
# # num_int = str(num_str)
# print(num_int)

# numbers = [1, 2, 3, 4]
# print(sum(numbers)) 

# numbers = [1, 2, 3, 4, 0.5]
# print(min(numbers))  # Outputs: 1
# print(max(numbers))

# num=(-5)
# print(abs(num))

# print(round(234.43256, 2))

# numbers = [1, 2, 3, 4, 0.5]
# print(sorted(numbers))

# str1 = "Hello"
# str2 = "World"
# print(str1+ " " +str2)  
# result = str1 + " " + str2
# print(result)  

# list1 = [1, 2, 3,]
# list2 = [4, 5, 6]
# print(list1 + list2)

# result = list1 + list2
# print(result)  

# y='I am in love '
# x='with my God'
# z=y + x
# print('\n',z)

# list1 = [1, 2, 3, 4]
# list2 = list1
# list1.append(5)
# print(list2)

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)  

#single line commenting
#below is multiline commenting
# print("""
# Health is\n Wealth
# """)
# # escape characters: \n(new line)

# print("i am now a certified python developer")
# _name='bolu'
# print(_name)

# fruits='orange','mango'
# fruit2=("orange")

# print(type(fruits))
# print(type(fruit2))
# print(len(fruits))
# print(len(fruit2))

# value2=7
# result=not value2
# # result = bool(value2)
# print(result)



# value1='toluwani'
# value2='titilope'
# if len(value1) and len(value2) == 8:
#     print('they are of the same lenght')
# else:
#     print('they are not of the same lenght')

# a= 'mango'
# b= 'orange'
# if len(a) and len(b) == 4:
#     print('both  are the same length')
# else:
#     print('both of them are not of the same length')

# a=11
# b=3
# b +=a
# print(b)
# b -=a
# print(b)
# b *=a
# print(b)
# b <<=a
# print(b)


# x= 20
# y= 30
# list=[10, 20, 40, 60, 70]
# if ( x not in list):
#     print('not found')
# else:
#     print('found')

# score=0
# x = 24
# y = 20
# list = [10, 20, 30, 40, 50]
# if ( y or x not in list):
#     score+=5
#     print(" present in given list:",score)
# else:
#     print(" NOT present in given list:", score)
# """

# """
# score=0
# question=input('What is your name: ')
# ans=['Dray', 'Dara']
# if question in ans:
#     score+=5
#     print('Correct:',score)
# else:
#     print('Oh noo:', score)

# score =0
# question=input('1. Input is used to collect value from: ')
# ans = ( 'User','user')
# if question in ans:
#     score+=5
# else:
#     score+=0
# question=input('2. Variable are like container use to store: ')
# ans = ( 'Data','data')
# if question in ans:
#     score+=5
# else:
#     score+=0
# question=input('3. The basic structural and functional unit of all living organism is: ')
# ans = ( 'Cell','cell')
# if question in ans:
#     score+=5
    
# else:
#     score+=0
# print('Total:',score)

# print("""                  
#                             Full name:Emmanuel Taiwo Micheal     
#                             Matric number:12345
#                             Deparment:Data Ssience
#                             Payment:Paid
# """)

# NameOfStudent=input('Please provide your full name: ')
# MatricNumber=input('Provide your matric number: ')
# Department=input('Provide your deparment name: ')


# n=input("""
#                 Please provide your full name:
#                 Provide your matric number:
#                 Provide your deparment name:
# """)
# print("My name is " + n)
# name=' fukunmi flarenwaju'
# print(len(name))
# print(name.replace('f', 'b'))
# print(name.replace)
# studentName='Darasimiamaladudu'
# newName=studentName[0:13] + 'lafun'
# newName=list(studentName)
# newName=[13:]='pupa'
# print(type(newName))
# print(studentName[-4:])
# print(studentName[-13:-9])
# print(studentName[-17:-13])
# print(studentName[-17:-9])
# print(studentName[-9:-4])
# print(studentName[-4:])
# print(studentName[5::3])
# print(name.strip().capitalize())
# print(name.replace())

# Step 1: Create a dictionary for the CBT questions and their correct answers
# questions = {
#     "What is 2 + 2?": "4",
#     "What is the capital of France?": "Paris",
#     "What is 10 / 2?": "5",
#     "What is the largest planet in the solar system?": "Jupiter",
#     "What is the boiling point of water in degrees Celsius?": "100",
#     "Which language is spoken in Brazil?": "Portuguese",
#     "What is 5 * 6?": "30",
#     "What is the square root of 16?": "4",
#     "In what year did the Titanic sink?": "1912",
#     "What is the chemical symbol for gold?": "Au"
# }

# # Step 2: Collect information for exactly three students
# registered_students = {}  # Dictionary to store registered student names and matric numbers

# # Ask each student for their name and matric number to register
# for each in range(3):
#     name = input("Enter your name: ")
#     matric_number = input("enter your matric no: ")
#     registered_students[matric_number] = name  # Store the student info in the dictionary

# # Step 3: Ask each student if they want to take the CBT test
# for each in range(3):
#     name = input("Enter your matric no to check if you are eligible for the test: ")
    
#     # Check if the student is registered
#     if name not in registered_students:
#         print(name + ' you are not eligible for the test. Please register first.''\n')
#         continue  # Skip to the next student

#     # Ask if the registered student is ready to take the test
#     ready = input("name +' are you ready to take the CBT test? (yes/no)': ").strip().lower()

#     if ready != 'yes':
#         print("Test terminated.")
#         break  # Stop if the student is not ready

#     # Step 4: Initialize the score for this student
#     score = 0

#     # Step 5: Ask the questions and calculate the score
#     for question, correct_answer in questions.items():
#         answer = input(question + " ")  # Ask the question
#         if answer.strip().lower() == correct_answer.lower():  # Check if the answer is correct
#             score += 10  # Add 10 points for each correct answer

#     # Step 6: Show the student's score
#     print(f"\n{name}, your score is {score}/100.\n")

#     # Step 7: Ask if the next student is available
#     if each < 2:  # Only ask if it's not the last student
#         next_student = input("Is the next student available to take the CBT test? (yes/no): ").strip().lower()
#         if next_student != 'yes':
#             print("Test terminated.")
#             break
        
        
# import random

# # Step 1: Create a dictionary for the CBT questions and their correct answers
# questions = {
#     "What is 2 + 2?": "4",
#     "What is the capital of France?": "Paris",
#     "What is 10 / 2?": "5",
#     "What is the largest planet in the solar system?": "Jupiter",
#     "What is the boiling point of water in degrees Celsius?": "100",
#     "Which language is spoken in Brazil?": "Portuguese",
#     "What is 5 * 6?": "30",
#     "What is the square root of 16?": "4",
#     "In what year did the Titanic sink?": "1912",
#     "What is the chemical symbol for gold?": "Au"
# }

# # Step 2: Register three students by collecting names and matric numbers
# registered_students = {}  # Dictionary to store student names and matric numbers
# students_completed = []   # List to store students who have already taken the test

# # Register three students
# for i in range(3):
#     # name = input(f"Register the name of student {i + 1}: ")
#     # matric_number = input(f"Register the matric number of student {i + 1}: ")
#     name = input("Register your name: ")
#     matric_number = input("Register your matric no: ")
#     registered_students[name] = matric_number  # Store the student info in the dictionary
    
# # Step 3: Function to conduct the test
# def conduct_test(student_name):
#     # Login with matric number
#     matric_number = input(f"{student_name}, please enter your matric number to login: ")
    
#     # Verify that the student is eligible and has not participated yet
#     if student_name not in registered_students or matric_number != registered_students[student_name]:
#         print(f"{student_name}, you are not eligible for the test or your matric number is incorrect.")
#         return

#     if student_name in students_completed:
#         print(f"{student_name}, you have already taken the test. You cannot participate again.")
#         return

#     # Mark the student as having participated
#     students_completed.append(student_name)

#     # Ask if the student is ready to take the test
#     ready = input(f"{student_name}, are you ready to take the CBT test? (yes/no): ").strip().lower()

#     if ready != 'yes':
#         print("Test terminated.")
#         return  # Stop if the student is not ready

#     # Step 4: Initialize the score for this student
#     score = 0

#     # Step 5: Ask 5 random questions from the 10 CBT questions
#     random_questions = random.sample(list(questions.items()), 5)  # Select 5 random questions
    
#     for question, correct_answer in random_questions:
#         answer = input(question + " ")  # Ask the question
#         if answer.strip().lower() == correct_answer.lower():  # Check if the answer is correct
#             score += 10  # Add 10 points for each correct answer

#     # Step 6: Show the student's score
#     print(f"\n{student_name}, your score is {score}/50.\n")

# # Step 7: Ask each student if they are available to take the test
# for student_name in registered_students.keys():
#     if student_name in students_completed:
#         continue  # Skip the student if they've already taken the test
    
#     next_student = input(f"Is {student_name} available to take the CBT test? (yes/no): ").strip().lower()
#     if next_student == 'yes':
#         conduct_test(student_name)  # Call the function for this student
#     else:
#         print(f"{student_name} is not available.")
        
        
        
        
        
#         import random

# # Step 1: Create a dictionary for the CBT questions and their correct answers
# questions = {
#     "What is 2 + 2?": "4",
#     "What is the capital of France?": "Paris",
#     "What is 10 / 2?": "5",
#     "What is the largest planet in the solar system?": "Jupiter",
#     "What is the boiling point of water in degrees Celsius?": "100",
#     "Which language is spoken in Brazil?": "Portuguese",
#     "What is 5 * 6?": "30",
#     "What is the square root of 16?": "4",
#     "In what year did the Titanic sink?": "1912",
#     "What is the chemical symbol for gold?": "Au"
# }

# # Step 2: Register three students by collecting their names and matric numbers
# registered_students = {}  # Dictionary to store student names and matric numbers
# students_completed = []   # List to store students who have already taken the test

# # Register three students
# for i in range(3):
#     name = input(f"Register the name of student {i + 1}: ")
#     matric_number = input(f"Register the matric number of student {i + 1}: ")
#     registered_students[name] = matric_number  # Store the student info in the dictionary

# # Step 3: Start the CBT test process for registered students
# for student_name in registered_students.keys():
    
#     if student_name in students_completed:
#         continue  # Skip the student if they've already taken the test
    
#     # Ask if the student is available to take the test
#     next_student = input(f"Is {student_name} available to take the CBT test? (yes/no): ").strip().lower()
    
#     if next_student != 'yes':
#         print(f"{student_name} is not available.")
#         continue

#     # Step 4: The student must login with their name and matric number
#     matric_number = input(f"{student_name}, please enter your matric number to login: ")
    
#     # Step 5: Verify that the student is eligible
#     if matric_number != registered_students[student_name]:
#         print(f"{student_name}, your matric number is incorrect. You are not eligible for the test.")
#         continue
    
#     # Check if the student has already completed the test
#     if student_name in students_completed:
#         print(f"{student_name}, you have already taken the test. You cannot participate again.")
#         continue

#     # Mark the student as having participated
#     students_completed.append(student_name)

#     # Step 6: Ask if the student is ready to take the test
#     ready = input(f"{student_name}, are you ready to take the CBT test? (yes/no): ").strip().lower()

#     if ready != 'yes':
#         print(f"{student_name}, test terminated. You are not taking the test.")
#         continue

#     # Step 7: Initialize the score for this student
#     score = 0

#     # Step 8: Randomly select 5 questions from the 10 available CBT questions
#     random_questions = random.sample(list(questions.items()), 5)  # Select 5 random questions
    
#     for question, correct_answer in random_questions:
#         # Step 9: Ask the questions and check the answers
#         answer = input(question + " ")  # Ask the question
#         if answer.strip().lower() == correct_answer.lower():  # Check if the answer is correct
#             score += 10  # Add 10 points for each correct answer

#     # Step 10: Show the student's score
#     print(f"\n{student_name}, your score is {score}/50.\n")








############################################################################################




# print('hello, world')
# a=2
# b=5
# print(a + b)


# name='taiwo'
# age='10'
# print(name)
# print(age)
# print(name + age)

# score = 85
# if score >= 90:
#     print('Grade A')
# # elif score >= 80:
# #     print('Grade B')
# elif score >= 50:
#     print('Grade C')
# else:
#     print('Grade D')

# age = 18
# is_student = True

# if age < 18 and is_student:
#     print('you are an adult student')
# else:
#     print('You are a teenager')
# if age >= 18 and is_student:
#     print('you are an adult student')
# else:
#     print('You are a teenager')

# fruits=('orange', 'mango', 'pineapple', 'apple', 'banana')
# for fruit in fruits:
#     print(fruit)

# a = 1
# while a <= 5:
#     print(a)
#     a +=1

# for each in range(1, 6):
#     if each ==3:
#         break
#     print(each)
    
# for i in range(1, 6):
#     if i ==3:
#         break
#     print(i)
    
    
# x= -3
# if x > 0:
#     print('the number is positive')
# elif x < 0:
#     print('the numder is negative')
# else:
#     print('the number is Zero')


# num= 1
# while num <= 10:
#     print(num)
#     num +=1
    
# names=('kike','Titi', 'Tobi', 'Temi')
# for name in names:
#     print(type(name))
#     print(name)

#                      #   functions #

# def greet(names):
#     print(f'hello, {names}')
# greet('sola')
# greet('kunle')

# def add_num(a, b):
#     # return a + b
#     add_all= 
#     print(add_num)
# # res= add_num(5, 8)
# add_num(5, 8)
# # print(res)

# def add_num (x, y):
#     sum_all= x + y
#     print(sum_all)
# add_num(3, 6)
        
        
# def add_num(v, y):
#     return v+ y
# res= add_num(4, 8)
# print(res)
        
        
# def greet(names='tolu'):
#     print(f'hello, {names}')
# greet()
# greet('kunle')

# def greet( names, name ='tolu'):
#     print(f'hello, {names} and {name}')
# greet('titi')
# greet('kunle')
# greet('kunle','titi')
      
      
# def multi(a, b, c):
#     return a * b * c
# res=multi(3, 5, 2)
# print(res)

# def multi(a, b, c):
#     multiple= a * b * c
#     print(multiple)
# multi(3, 5, 2)
        
# def show_age(age='25'):
#     # age=25
#     print(age)
# show_age()

# def greet_user(name='sola',location='Yoaco'):
#     print(f'Welcome {name}, Do you stayed at {location}?')
# greet_user()

# def square_number(x):
#     return (x)**2
# res=square_number(4)
# print(res)

# def square_number(x):
#     return x * x
# res=square_number(4)
# print(res)

# 𝞹𝞹𝞹𝞹𝞹𝞹𝞹𝞹

# def square_number(x):
#     square_num= (x)**2
#     print(square_num)
# square_number(10)

# def calculate_area(𝞹):
#     radius= 7
#     return 𝞹 * radius**2
# res=calculate_area(3.14159)
# print(res)

# def calculate_area(radius):
#     pi=3.14159
#     cal_area= pi * radius *radius
#     print(cal_area)
# calculate_area(7)

# def calculate_area(radius):
#     𝞹=3.14159
#     return 𝞹 * radius**2
# area=calculate_area(7)
# print(area)


#                   ##  list_data_type   ##

# fruits=['banana', 'orange', 'mango', 'apple']
# print(fruits[3])
# print(fruits[2:4])        # slicing a list
# print(type(fruits))
# fruits[2]='pineapple'
# fruits.append('blueberry')
# fruits.remove('orange')
# print(fruits)


#                   ##  tuples_data_type   ##

# my_tuple=('banana', 'orange', 'mango', 'apple')
# print(my_tuple[2])


#                   ##  Dictionaries_data_type   ##

# person={"name":"john", "age":"25", "city":"New york"}
# print(person["name"])
# print(person['age'])
# person["age"]= 27
# person["job"]= 'Engineering'
# del person["city"]
# print(person)

#  exercise
# (1)
# movies=['Jenifer', 'home sweet home', 'happiness', 'kings of boys',"comando", 'fast and furious']
# print(movies[1])
# print(movies[5])
# print(movies[-1])
# print(movies[1::4])

# (2)
# numbers=(4 , 6 , 3)
# print(sum(numbers))

# (3)
# info={"first_name":"Tobi", "last_name":"Olatunji", "age":"27"}
# print(info["first_name"])
# print(info["last_name"])
# print(info["age"])
# print("My name is " + info["first_name"] + " " + info["last_name"] + ", i am " + info["age"] +"years old.")
# info['city']='USA'
# print(info)
        
        
#          # loop with list   #

# fruits=['orange', 'mango', 'banana', 'apple', 'pineapple']
# for fruit in fruits:
#     print(fruit)
# for i in range(len(fruits)):
#     print(f'index {i}:{fruits[i]}')
#     print(fruits)
# print('\n',fruits)
# print(f'index {1}:{fruits[1]}')


#          # loop with tuple   #


# numbers=(1, 2, 3, 4, 5)
# for number in numbers:
#     print(number)


#          # loop with dictionaries   #
# person={"name":"john", "age":"25", "city":"New york"}
# for key in person:
#     print(key)
# for values in person.values():
#     print(values)
# for key, values in person.items():
#     print(f'{key}:{values}')


#                ##   Using break, continue and else in loops    ##
# numbers=[1, 2, 3, 4, 5, 6]
# for num in numbers:
#     if num ==3:
#         break
#     print(num)
# for num in numbers:
#     if num ==3:
#         continue
#     print(num)

# animals=["Monkey", "Dog","Sheep", "Lion","Elephant"]

# for animal in animals:
#     print(animal)
    
# cities=('Lagos', 'Ibadan','Port Harcourt')
# for city in cities:
#     print(city)

# Book_Authors={'There is a place called tomorrow':'Mr Thomas', 'REaders are Leaders':'Dr. Solomon', 'Health is Wealth':'prof. Akinade'}
# for key, values in Book_Authors.items():
#     print(f'{key} by {values}')
    
    
# numbers=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# for num in numbers:
#     if num ==7:
#         break
#     print(num)
        
        
# for num in range(1, 11):
#     if num ==7:
#         break
#     print(num)
    
# file = open("example.txt","w")
# file.write("this is a new line of text.\n")
# file.close
# file =open('example.txt', 'a')
# file.write('this text is appended')
# file.close()
# file = open('example.txt', "r")
# content= file.read()
# print(content)
# file.close()

#######                               OOP                     ##################


class Dog:
    def __init__(self, name, breed):
        self.name=name
        self.breed=breed
    def bark(self):
        re



# def login():
#     pin = "1234"
#     attempts = 3
#     while attempts > 0:
#         entered_pin = input("Enter your PIN: ")
#         if entered_pin == pin:
#             print("Login successful.")
#             return True
#         else:
#             attempts -= 1
#             print(f"Incorrect PIN. Attempts remaining: {attempts}")
#     print("Access denied.")
#     return False

# def check_balance(balance):
#     print(f"Your current balance is: #{balance:.2f}")

# def transfer(balance):
#     if balance <= 0:
#         print("Insufficient balance for transfer.")
#         return balance

#     account_number = input("Enter the recipient's 10-digit account number: ")
#     if len(account_number) != 10 or not account_number.isdigit():
#         print("Invalid account number. Must be 10 digits.")
#         return balance

#     amount = float(input("Enter amount to transfer: "))
#     if amount <= 0:
#         print("Transfer amount must be greater than zero.")
#     elif amount > balance:
#         print("Insufficient funds for this transfer.")
#     else:
#         balance -= amount
#         print(f"Successfully transferred #{amount:.2f} to account {account_number}.")
#         check_balance(balance)
#     return balance

# def main():
#     balance = 7000.00

#     if login():
#         while True:
#             print("\nATM Menu:")
#             print("1. Check Balance")
#             print("2. Transfer Money")
#             print("3. Logout")
#             choice = input("Choose an option (1-3): ")

#             if choice == '1':
#                 check_balance(balance)
#             elif choice == '2':
#                 balance = transfer(balance)
#             elif choice == '3':
#                 print("Logged out successfully.")
#                 break
#             else:
#                 print("Invalid choice. Please try again.")

# if __name__ == "_main_":
#     main()
        
        
# def login():
#     pin = '1234'
#     attempt = 3
#     while attempt > 0:
#         input_pin = input('Enter your pin: ')
#         if input_pin == pin:
#             print('Login successful.')
#             return True
#         else:
#             attempt -= 1
#             if attempt > 0:
#                 print(f'Incorrect PIN. You have {attempt} attempts left.')
#             else:
#                 print('Too many incorrect attempts. Exiting.')
#                 return False

# def check_balance(balance):
#     print(f'Your current balance is: #{balance}.')
# def transfer(balance):
#     if balance <= 0:
#         print('Insufficient balance for transfer.')
#         return balance

#     account_number = input("Enter the recipient's 10-digit account number: ")
#     if len(account_number) != 10 or not account_number.isdigit():
#         print('Invalid account number. Must be 10 digits.')
#         return balance

#     amount = int(input('Enter the amount: '))
#     if amount <= 0:
#         print('Transfer amount must be greater than zero.')
#     elif amount > balance:
#         print('Insufficient funds for this transfer.')
#     else:
#         balance -= amount
#         print(f'Successfully transferred #{amount} to account {account_number}.')
#         check_balance(balance)
    
#     return balance

# def withdraw(balance):
#     amount = int(input("Enter amount to withdraw: "))
#     if 0 < amount <= balance:
#         balance -= amount
#         print(f"#{amount} has been withdrawn.")
#         check_balance(balance)
#     elif amount > balance:
#         print("Insufficient funds.")
#     else:
#         print("Invalid amount. Please enter a positive number.")
#     return balance

# def main():
#     balance = 5000

#     if login():
#         while True:
#             print("\n=== ATM Main Menu ===")
#             print("1. Check Balance")
#             print("2. Transfer Money")
#             print("3. Withdraw Money")
#             print("4. Exit")
#             choice = input('Choose an option (1-4): ')

#             if choice == '1':
#                 check_balance(balance)
#             elif choice == '2':
#                 balance = transfer(balance)
#             elif choice == '3':
#                 balance = withdraw(balance)
#             elif choice == '4':
#                 print('Logged out successfully. Thanks for using the ATM machine.')
#                 exit()
#             else:
#                 print('Invalid choice. Please select a valid option.')
# main()

# import random as rd
# pd=('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRXTUVW')
# random_pd= rd.choices(pd)
# num= rd.randint(0000, 9999)
# uba_acc_num= '20' + str(num)
# print(uba_acc_num)

        
        
        
        
        
        
        
        
        
        
        
        
class BankUSSD:
    def __init__(self):
        self.balance = 10000000
        self.pin = "1234"  
        self.service_code = "*234#"
        self.access_granted = False

    def main(self):
        entered_code = input("Enter USSD code (e.g., *234#): ")
        self.access_service(entered_code)

        if self.access_granted:
            while True:
                self.display_menu()
                choice = input("Please select an option: ")
                
                if choice == '1':
                    self.buy_airtime()
                elif choice == '2':
                    self.check_balance()
                elif choice == '3':
                    self.transfer()
                elif choice == '4':
                    self.withdraw()
                elif choice == '5':
                    print("Thank you for using our service.")
                    break
                else:
                    print("Invalid option selected. Please try again.")

    def display_menu(self):
        print("Welcome to Bank USSD Service")
        print("1. Buy Airtime")
        print("2. Check Balance")
        print("3. Transfer")
        print("4. Withdraw")
        print("5. Exit")

    def access_service(self, entered_code):
        if entered_code == self.service_code:
            self.access_granted = True
            print("Access granted to USSD service.")
        else:
            print("Incorrect USSD code. Access denied.")
            exit()

    def verify_pin(self, entered_pin):
        return entered_pin == self.pin

    def deduct_service_fee(self):
        service_fee = 5
        if self.balance >= service_fee:
            self.balance -= service_fee
            return True
        else:
            print("Insufficient balance to cover the service fee.")
            return False

    def buy_airtime(self):
        entered_pin = input("Enter your PIN to confirm: ")
        if not self.verify_pin(entered_pin):
            print("Incorrect PIN. Transaction canceled.")
            return
        phone_number = input("Enter the recipient's phone number: ")
        if len(phone_number) != 11 or not phone_number.isdigit():
            print('Invalid account number. Must be 10 digits.')
            return
        airtime_amount = float(input('Enter the amount: '))
        if airtime_amount <= 0:
            print('Transfer amount must be greater than zero.')
        elif airtime_amount > self.balance:
            print('Insufficient funds for this transfer.')
        else:
            self.balance -= airtime_amount
            print(f'Successfully transferred #{airtime_amount} to this phone number:{phone_number}.')
            # self.check_balance()
            print(f"Remaining balance: #{self.balance}")
    def check_balance(self):
        entered_pin = input("Enter your PIN to confirm: ")
        if not self.verify_pin(entered_pin):
            print("Incorrect PIN. Transaction canceled.")
            return
        else:
            print(f'Your current balance is: #{self.balance}.')

    def transfer(self):
        entered_pin = input("Enter your PIN to confirm: ")
        if not self.verify_pin(entered_pin):
            print("Incorrect PIN. Transaction canceled.")
            return

        if self.balance <= 0:
            print('Insufficient balance for transfer')
            return
        
        account_number = input("Enter the recipient's 10-digit account number: ")
        if len(account_number) != 10 or not account_number.isdigit():
            print('Invalid account number. Must be 10 digits.')
            return
        
        amount = float(input('Enter the amount: '))
        if amount <= 0:
            print('Transfer amount must be greater than zero.')
        elif amount > self.balance:
            print('Insufficient funds for this transfer.')
        else:
            self.balance -= amount
            print(f'Successfully transferred #{amount} to account {account_number}.')
            # self.check_balance()
            print(f"Remaining balance: #{self.balance}")

    def withdraw(self):
        entered_pin = input("Enter your PIN to confirm: ")
        if not self.verify_pin(entered_pin):
            print("Incorrect PIN. Transaction canceled.")
            return

        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"#{amount} has been withdrawn.")
            # self.check_balance()
            print(f"Remaining balance: #{self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid amount. Please enter a positive number.")

bank_ussd = BankUSSD()
bank_ussd.main()

        
        
        
        
        


