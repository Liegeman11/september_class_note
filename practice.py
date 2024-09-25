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
        
        
import random

# Step 1: Create a dictionary for the CBT questions and their correct answers
questions = {
    "What is 2 + 2?": "4",
    "What is the capital of France?": "Paris",
    "What is 10 / 2?": "5",
    "What is the largest planet in the solar system?": "Jupiter",
    "What is the boiling point of water in degrees Celsius?": "100",
    "Which language is spoken in Brazil?": "Portuguese",
    "What is 5 * 6?": "30",
    "What is the square root of 16?": "4",
    "In what year did the Titanic sink?": "1912",
    "What is the chemical symbol for gold?": "Au"
}

# Step 2: Register three students by collecting names and matric numbers
registered_students = {}  # Dictionary to store student names and matric numbers
students_completed = []   # List to store students who have already taken the test

# Register three students
for i in range(3):
    # name = input(f"Register the name of student {i + 1}: ")
    # matric_number = input(f"Register the matric number of student {i + 1}: ")
    name = input("Register your name: ")
    matric_number = input("Register your matric no: ")
    registered_students[name] = matric_number  # Store the student info in the dictionary
    
# Step 3: Function to conduct the test
def conduct_test(student_name):
    # Login with matric number
    matric_number = input(f"{student_name}, please enter your matric number to login: ")
    
    # Verify that the student is eligible and has not participated yet
    if student_name not in registered_students or matric_number != registered_students[student_name]:
        print(f"{student_name}, you are not eligible for the test or your matric number is incorrect.")
        return

    if student_name in students_completed:
        print(f"{student_name}, you have already taken the test. You cannot participate again.")
        return

    # Mark the student as having participated
    students_completed.append(student_name)

    # Ask if the student is ready to take the test
    ready = input(f"{student_name}, are you ready to take the CBT test? (yes/no): ").strip().lower()

    if ready != 'yes':
        print("Test terminated.")
        return  # Stop if the student is not ready

    # Step 4: Initialize the score for this student
    score = 0

    # Step 5: Ask 5 random questions from the 10 CBT questions
    random_questions = random.sample(list(questions.items()), 5)  # Select 5 random questions
    
    for question, correct_answer in random_questions:
        answer = input(question + " ")  # Ask the question
        if answer.strip().lower() == correct_answer.lower():  # Check if the answer is correct
            score += 10  # Add 10 points for each correct answer

    # Step 6: Show the student's score
    print(f"\n{student_name}, your score is {score}/50.\n")

# Step 7: Ask each student if they are available to take the test
for student_name in registered_students.keys():
    if student_name in students_completed:
        continue  # Skip the student if they've already taken the test
    
    next_student = input(f"Is {student_name} available to take the CBT test? (yes/no): ").strip().lower()
    if next_student == 'yes':
        conduct_test(student_name)  # Call the function for this student
    else:
        print(f"{student_name} is not available.")
        
        
        
        
        
        import random

# Step 1: Create a dictionary for the CBT questions and their correct answers
questions = {
    "What is 2 + 2?": "4",
    "What is the capital of France?": "Paris",
    "What is 10 / 2?": "5",
    "What is the largest planet in the solar system?": "Jupiter",
    "What is the boiling point of water in degrees Celsius?": "100",
    "Which language is spoken in Brazil?": "Portuguese",
    "What is 5 * 6?": "30",
    "What is the square root of 16?": "4",
    "In what year did the Titanic sink?": "1912",
    "What is the chemical symbol for gold?": "Au"
}

# Step 2: Register three students by collecting their names and matric numbers
registered_students = {}  # Dictionary to store student names and matric numbers
students_completed = []   # List to store students who have already taken the test

# Register three students
for i in range(3):
    name = input(f"Register the name of student {i + 1}: ")
    matric_number = input(f"Register the matric number of student {i + 1}: ")
    registered_students[name] = matric_number  # Store the student info in the dictionary

# Step 3: Start the CBT test process for registered students
for student_name in registered_students.keys():
    
    if student_name in students_completed:
        continue  # Skip the student if they've already taken the test
    
    # Ask if the student is available to take the test
    next_student = input(f"Is {student_name} available to take the CBT test? (yes/no): ").strip().lower()
    
    if next_student != 'yes':
        print(f"{student_name} is not available.")
        continue

    # Step 4: The student must login with their name and matric number
    matric_number = input(f"{student_name}, please enter your matric number to login: ")
    
    # Step 5: Verify that the student is eligible
    if matric_number != registered_students[student_name]:
        print(f"{student_name}, your matric number is incorrect. You are not eligible for the test.")
        continue
    
    # Check if the student has already completed the test
    if student_name in students_completed:
        print(f"{student_name}, you have already taken the test. You cannot participate again.")
        continue

    # Mark the student as having participated
    students_completed.append(student_name)

    # Step 6: Ask if the student is ready to take the test
    ready = input(f"{student_name}, are you ready to take the CBT test? (yes/no): ").strip().lower()

    if ready != 'yes':
        print(f"{student_name}, test terminated. You are not taking the test.")
        continue

    # Step 7: Initialize the score for this student
    score = 0

    # Step 8: Randomly select 5 questions from the 10 available CBT questions
    random_questions = random.sample(list(questions.items()), 5)  # Select 5 random questions
    
    for question, correct_answer in random_questions:
        # Step 9: Ask the questions and check the answers
        answer = input(question + " ")  # Ask the question
        if answer.strip().lower() == correct_answer.lower():  # Check if the answer is correct
            score += 10  # Add 10 points for each correct answer

    # Step 10: Show the student's score
    print(f"\n{student_name}, your score is {score}/50.\n")

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


