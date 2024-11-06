# create a cbt question application

#                   solution
    
# import random
# questions = {
#     ">>.What is 2 + 2?\n (a)22 (b)4 (c)8 \nanswer: ": "b",
#     ">>.What is the capital of France?\n (a)USA (b)Ghana (c)Paris:\n": "c",
#     ">>.What is 10 / 2?\n (a)3 (b)5 (c)12:\n ": "b",
#     ">>.What is the largest planet in the solar system?\n (a)Pluto (b)Venus (c)Mars (d)Jupiter :\n ": "d",
#     ">>.What is the boiling point of water in degrees Celsius?\n (a)95 (b)90 (c)100 (d)35 :\n ": "c",
#     ">>.What is 5 * 6?\n (a)11 (b)56 (c)30 (d)1 :\n ": "c",
#     ">>.What is the square root of 16?\n (a)4 (b)64 (c)36 (d)2 :\n  ": "a",
#     ">>.In what year did the Titanic sink?\n (a)1991 (b)1912 (c)1921 (d)1921 :\n ": "b",
#     ">>.What is the chemical symbol for water?\n (a)Au (b)H2O (c)HO2 (d)gu :\n ": "b",
#     ">>.What is the chemical symbol for gold?\n (a)Au (b)H2O (c)HO2 (d)gu :\n ": "a",
#     ">>.What is the primary function of the legislative branch of government: (a) To enforce laws (b) To interpret laws (c) To make laws (d) To implement polices ":'c',
#     ">>.Which of the following is not a renewable source of energy (a)Solar energy (b) Wind energy (c) Coal (d) Hydropower ":'c',
#     ">>.What is the value of x? when 3x + 7 = 22 (a)10 (b)2 (c)5 (d)7 ":'c',
#     ">>.In plants, photosynthesis primary takes place in which part? (a)Roots (b)Stem (c)Leaves (d)Flowers":'c',
#     ">>.which of the following is the longest river in Nigeria (a)River Benue (b)River Kaduna (c)River Niger (d)River Osun ":'c'
# }

# registered_students = {}  
# students_completed = []   
# def register_student():
#     while True:
#         name = input("Register your name: ")
#         if name in registered_students:
#             print(f"{name} already exists, please use another name.")
#             continue
#         matric_number = input("Register your matric number: ")
#         if matric_number in registered_students:
#             print(f"{matric_number} already exists, please use another name.")
#             continue
#         registered_students[name] = matric_number
#         print("Registration successful",registered_students)
        
#         another=input("Do you want to register another student(yes/no): ").strip().lower()
#         if another != 'yes':
#             break

# def take_test():
#     for student_name in registered_students.keys():
#         if student_name in students_completed:
#             continue  
#         attempt = 3
#         while attempt > 0:
#             matric_number = input("please enter your matric number to login: ").lower().strip()
#             if matric_number == registered_students:
#                 break 
#             else:
#                 attempt -= 1
#                 if attempt > 0:
#                     print(f"Incorrect matric number. You have {attempt} attempts left.")
#                 else:
#                     print(f"Sorry, you have been locked out due to multiple failed attempts.")
#                     break
#         if attempt == 0:
#             main()
#         if student_name in students_completed:
#             print(f", you have already taken the test. You cannot participate again.")
#             continue
#         students_completed.append(student_name)

#         ready = input(", are you ready to take the CBT test? (yes/no): ").strip().lower()

#         if ready != 'yes':
#             print(f"{student_name}, test terminated. You are not taking the test.")
#             continue

#         score = 0
#         random_questions = random.sample(list(questions.items()), 5) 
    
#         for question, correct_answer in random_questions:
#             answer = input(question + " ") 
#             if answer.lower() == correct_answer.lower():  
#                 score += 10 
#         print(f"\n{student_name}, your score is {score}/50.\n")
# def main():
#     print("""
#                                      WELCOME TO DESTINY GROUP OF SCHOOL
#                  SELECT
#                  1.REGISTER
#                  2.TAKE THE TEST
#                  3.EXIT
#     """)
    
#     user_option=input("Enter your option(1-3): ")
#     if user_option == '1':
#         register_student()
#         main()
#     elif user_option == '2':
#         if not registered_students:
#             print("No student register. Please register first")
#             main()
#         else:
#             take_test()
#     elif user_option == '3':
#         print('Thanks for using our service')
#         exit()
#     else:
#         print("Invalid selection!. Please enter a valid option")
#         exit()
# main()

        # next_student = input(f"Is {student_name} available to take the CBT test? \n(yes/no): ").strip().lower()
    
        # if next_student != 'yes':
        #     print(f"{student_name} is not available.")
        #     continue


# import random

# # Questions bank with correct answers
# questions = {
#     ">>.What is 2 + 2?\n (a)22 (b)4 (c)8 \nAnswer: ": "b",
#     ">>.What is the capital of France?\n (a)USA (b)Ghana (c)Paris:\nAnswer: ": "c",
#     ">>.What is 10 / 2?\n (a)3 (b)5 (c)12:\nAnswer: ": "b",
#     ">>.What is the largest planet in the solar system?\n (a)Pluto (b)Venus (c)Mars (d)Jupiter :\nAnswer: ": "d",
#     ">>.What is the boiling point of water in degrees Celsius?\n (a)95 (b)90 (c)100 (d)35 :\nAnswer: ": "c",
#     ">>.What is 5 * 6?\n (a)11 (b)56 (c)30 (d)1 :\nAnswer: ": "c",
#     ">>.What is the square root of 16?\n (a)4 (b)64 (c)36 (d)2 :\nAnswer: ": "a",
#     ">>.In what year did the Titanic sink?\n (a)1991 (b)1912 (c)1921 (d)1921 :\nAnswer: ": "b",
#     ">>.What is the chemical symbol for water?\n (a)Au (b)H2O (c)HO2 (d)gu :\nAnswer: ": "b",
#     ">>.What is the chemical symbol for gold?\n (a)Au (b)H2O (c)HO2 (d)gu :\nAnswer: ": "a",
#     ">>.What is the primary function of the legislative branch of government?\n (a) To enforce laws (b) To interpret laws (c) To make laws (d) To implement policies\nAnswer: ": 'c',
#     ">>.Which of the following is not a renewable source of energy?\n (a)Solar energy (b) Wind energy (c) Coal (d) Hydropower\nAnswer: ": 'c',
#     ">>.What is the value of x? when 3x + 7 = 22\n (a)10 (b)2 (c)5 (d)7\nAnswer: ": 'c',
#     ">>.In plants, photosynthesis primarily takes place in which part?\n (a)Roots (b)Stem (c)Leaves (d)Flowers\nAnswer: ": 'c',
#     ">>.Which of the following is the longest river in Nigeria?\n (a)River Benue (b)River Kaduna (c)River Niger (d)River Osun\nAnswer: ": 'c'
# }

# registered_students = {}
# students_completed = []

# def register_student():
#     while True:
#         name = input("Register your name: ").strip()
#         if name in registered_students:
#             print(f"{name} already exists, please use another name.")
#             continue
#         matric_number = input("Register your matric number: ").strip()
#         if matric_number in registered_students.values():
#             print(f"{matric_number} already exists, please use another matric number.")
#             continue
#         registered_students[name] = matric_number
#         print("Registration successful.", registered_students)
        
#         another = input("Do you want to register another student (yes/no)? ").strip().lower()
#         if another != 'yes':
#             break

# def take_test():
#     for student_name in registered_students.keys():
#         if student_name in students_completed:
#             print(f"{student_name}, you have already taken the test. You cannot participate again.")
#             continue
        
#         attempt = 3
#         while attempt > 0:
#             matric_number = input("Please enter your matric number to login: ").strip()
#             if matric_number == registered_students[student_name]:
#                 break
#             else:
#                 attempt -= 1
#                 print(f"Incorrect matric number. You have {attempt} attempt(s) left.")
#                 if attempt == 0:
#                     print(f"Sorry, you have been locked out due to multiple failed attempts.")
#                     return

#         students_completed.append(student_name)
#         ready = input(f"{student_name}, are you ready to take the CBT test? (yes/no): ").strip().lower()
#         if ready != 'yes':
#             print(f"{student_name}, test terminated. You are not taking the test.")
#             continue

#         score = 0
#         random_questions = random.sample(list(questions.items()), 5)
        
#         for question, correct_answer in random_questions:
#             answer = input(question + " ").strip().lower()
#             if answer == correct_answer:
#                 score += 10  # Each question is worth 10 points
        
#         print(f"\n{student_name}, your score is {score}/50.\n")

# def main():
#     while True:
#         print("""
#             WELCOME TO DESTINY GROUP OF SCHOOL
#             Select an option:
#             1. Register
#             2. Take the Test
#             3. Exit
#         """)

#         user_option = input("Enter your option (1-3): ").strip()
#         if user_option == '1':
#             register_student()
#         elif user_option == '2':
#             if not registered_students:
#                 print("No students registered. Please register first.")
#             else:
#                 take_test()
#         elif user_option == '3':
#             print("Thanks for using our service!")
#             break
#         else:
#             print("Invalid selection! Please enter a valid option (1-3).")

# main()


# import random

# # Questions bank with correct answers
# questions = {
#     ">>.What is 2 + 2?\n (a)22 (b)4 (c)8 \nAnswer: ": "b",
#     ">>.What is the capital of France?\n (a)USA (b)Ghana (c)Paris:\nAnswer: ": "c",
#     ">>.What is 10 / 2?\n (a)3 (b)5 (c)12:\nAnswer: ": "b",
#     ">>.What is the largest planet in the solar system?\n (a)Pluto (b)Venus (c)Mars (d)Jupiter :\nAnswer: ": "d",
#     ">>.What is the boiling point of water in degrees Celsius?\n (a)95 (b)90 (c)100 (d)35 :\nAnswer: ": "c",
#     ">>.What is 5 * 6?\n (a)11 (b)56 (c)30 (d)1 :\nAnswer: ": "c",
#     ">>.What is the square root of 16?\n (a)4 (b)64 (c)36 (d)2 :\nAnswer: ": "a",
#     ">>.In what year did the Titanic sink?\n (a)1991 (b)1912 (c)1921 (d)1921 :\nAnswer: ": "b",
#     ">>.What is the chemical symbol for water?\n (a)Au (b)H2O (c)HO2 (d)gu :\nAnswer: ": "b",
#     ">>.What is the chemical symbol for gold?\n (a)Au (b)H2O (c)HO2 (d)gu :\nAnswer: ": "a",
#     ">>.What is the primary function of the legislative branch of government?\n (a) To enforce laws (b) To interpret laws (c) To make laws (d) To implement policies\nAnswer: ": 'c',
#     ">>.Which of the following is not a renewable source of energy?\n (a)Solar energy (b) Wind energy (c) Coal (d) Hydropower\nAnswer: ": 'c',
#     ">>.What is the value of x? when 3x + 7 = 22\n (a)10 (b)2 (c)5 (d)7\nAnswer: ": 'c',
#     ">>.In plants, photosynthesis primarily takes place in which part?\n (a)Roots (b)Stem (c)Leaves (d)Flowers\nAnswer: ": 'c',
#     ">>.Which of the following is the longest river in Nigeria?\n (a)River Benue (b)River Kaduna (c)River Niger (d)River Osun\nAnswer: ": 'c'
# }

# registered_students = {} 
# students_completed = []   

# def register_student():
#     while True: 
#         name = input("Register your name: ").strip()
#         if name in registered_students:
#             print(f"{name} already exists, please use another name.")
#             return
    
#         matric_number = input("Register your matric number: ").strip()
#         if matric_number in registered_students.values():
#             print(f"{matric_number} already exists, please use another matric number.")
#             return
#         registered_students[name] = matric_number
#         print("Registration successful!", registered_students)
#         another= input('Do you want to register another student (yes/no): ').lower().strip()
#         if another != 'yes':
#             break

# def take_test():
#     if not registered_students:
#         print("No students are registered. Please register first.")
#         return

#     student_name = input("Enter your name to log in and take the test: ").strip()
#     if student_name not in registered_students:
#         print("You are not registered. Please register first.")
#         return
#     if student_name in students_completed:
#         print(f"{student_name}, you have already taken the test. You cannot participate again.")
#         return
    
#     attempt = 3
#     while attempt > 0:
#         matric_number = input("Please enter your matric number to log in: ").strip()
#         if matric_number == registered_students[student_name]:
#             break
#         else:
#             attempt -= 1
#             if attempt > 0:
#                 print(f"Incorrect matric number. You have {attempt} attempts left.")
#             else:
#                 print(f"Sorry, {student_name}, you have been locked out due to multiple failed attempts.")
#                 return
    
#     students_completed.append(student_name)
#     print(f"{student_name}, let's begin your test.")

#     score = 0
#     random_questions = random.sample(list(questions.items()), 5)

#     for question, correct_answer in random_questions:
#         answer = input(question + " ").strip().lower()
#         if answer == correct_answer:
#             score += 10 
#             students_completed.append[score]
#     print(f"\n{student_name}, your score is {score}/50.\n")
# def get_result():
#     if not register_student:
#         print("you have to register first")
#     student_name=input("Enter your name to log in and get your result: ")
#     if student_name not in students_completed:
#         print("You have not take the test. Please take the test first.")
#         return
#     attempt=3
#     while attempt > 0:
#         matric_no= input("Enter your matric number to log in: ")
#         if matric_no == students_completed[student_name]:
#             break
#         else:
#             attempt -=1
#             if attempt > 0:
#                 print(f"Incorrect matric number. You have {attempt} attempts left.")
#             else:
#                 print(f"Sorry, {student_name} You have been locked out  due to multiple incorrect attempt")
#                 return
#     print(f"{student_name}, this is your result: ")
#     print(f"\n{student_name}, your result is {score}/50.\n")
                
                
# def main():
#     while True:
#         print("""
#             WELCOME TO DESTINY GROUP OF SCHOOL
#             Select an option:
#             1. Register
#             2. Take the Test
#             4. Get result
#             3. Exit
#         """)

#         user_option = input("Enter your option (1-3): ").strip()
#         if user_option == '1':
#             register_student()
#         elif user_option == '2':
#             take_test()
#         elif user_option == '4':
#             get_result()
#         elif user_option == '3':
#             print("Thanks for using our service!")
#             break
#         else:
#             print("Invalid selection! Please enter a valid option (1-3).")

# main()



import random

questions = {
    ">>.What is 2 + 2?\n (a)22 (b)4 (c)8 \nAnswer: ": "b",
    ">>.What is the capital of France?\n (a)USA (b)Ghana (c)Paris:\nAnswer: ": "c",
    ">>.What is 10 / 2?\n (a)3 (b)5 (c)12:\nAnswer: ": "b",
    ">>.What is the largest planet in the solar system?\n (a)Pluto (b)Venus (c)Mars (d)Jupiter :\nAnswer: ": "d",
    ">>.What is the boiling point of water in degrees Celsius?\n (a)95 (b)90 (c)100 (d)35 :\nAnswer: ": "c",
    ">>.What is 5 * 6?\n (a)11 (b)56 (c)30 (d)1 :\nAnswer: ": "c",
    ">>.What is the square root of 16?\n (a)4 (b)64 (c)36 (d)2 :\nAnswer: ": "a",
    ">>.In what year did the Titanic sink?\n (a)1991 (b)1912 (c)1921 (d)1921 :\nAnswer: ": "b",
    ">>.What is the chemical symbol for water?\n (a)Au (b)H2O (c)HO2 (d)gu :\nAnswer: ": "b",
    ">>.What is the chemical symbol for gold?\n (a)Au (b)H2O (c)HO2 (d)gu :\nAnswer: ": "a",
    ">>.What is the primary function of the legislative branch of government?\n (a) To enforce laws (b) To interpret laws (c) To make laws (d) To implement policies\nAnswer: ": 'c',
    ">>.Which of the following is not a renewable source of energy?\n (a)Solar energy (b) Wind energy (c) Coal (d) Hydropower\nAnswer: ": 'c',
    ">>.What is the value of x? when 3x + 7 = 22\n (a)10 (b)2 (c)5 (d)7\nAnswer: ": 'c',
    ">>.In plants, photosynthesis primarily takes place in which part?\n (a)Roots (b)Stem (c)Leaves (d)Flowers\nAnswer: ": 'c',
    ">>.Which of the following is the longest river in Nigeria?\n (a)River Benue (b)River Kaduna (c)River Niger (d)River Osun\nAnswer: ": 'c'
}

registered_students = {}  
students_completed = {}   

def register_student():
    while True: 
        name = input("Register your name: ").strip()
        if name in registered_students:
            print(f"{name} already exists, please use another name.")
            return
    
        matric_number = input("Register your matric number: ").strip()
        if matric_number in registered_students.values():
            print(f"{matric_number} already exists, please use another matric number.")
            return
        registered_students[name] = matric_number
        print("Registration successful!", registered_students)
        
        another = input('Do you want to register another student (yes/no): ').lower().strip()
        if another != 'yes':
            break

def take_test():
    if not registered_students:
        print("No students are registered. Please register first.")
        return

    student_name = input("Enter your name to log in and take the test: ").strip()
    if student_name not in registered_students:
        print("You are not registered. Please register first.")
        return
    if student_name in students_completed:
        print(f"{student_name}, you have already taken the test. You cannot participate again.")
        return
    
    attempt = 3
    while attempt > 0:
        matric_number = input("Please enter your matric number to log in: ").strip()
        if matric_number == registered_students[student_name]:
            break
        else:
            attempt -= 1
            if attempt > 0:
                print(f"Incorrect matric number. You have {attempt} attempts left.")
            else:
                print(f"Sorry, {student_name}, you have been locked out due to multiple failed attempts.")
                return
    
    score = 0
    random_questions = random.sample(list(questions.items()), 5)

    for question, correct_answer in random_questions:
        answer = input(question + " ").strip().lower()
        if answer == correct_answer:
            score += 10 
    
    students_completed[student_name] = score
    # print(f"\n{student_name}, your score is {score}/50.\n")

def get_result():
    if not registered_students:
        print("You have to register first.")
        return
    
    student_name = input("Enter your name to log in and get your result: ").strip()
    if student_name not in students_completed:
        print("You have not taken the test. Please take the test first.")
        return
    
    attempt = 3
    while attempt > 0:
        matric_no = input("Enter your matric number to log in: ").strip()
        if matric_no == registered_students[student_name]:
            break
        else:
            attempt -= 1
            if attempt > 0:
                print(f"Incorrect matric number. You have {attempt} attempts left.")
            else:
                print(f"Sorry, {student_name}, you have been locked out due to multiple incorrect attempts.")
                return
    
    print(f"{student_name}, this is your result:")
    print(f"Your score is {students_completed[student_name]}/50.\n")
    if students_completed[student_name] == 50:
        print('Excellent Result keep it up')
    elif students_completed[student_name] == 40:
        print('Good result, Welldone... ')
    elif students_completed[student_name] ==30:
        print('This is an average result, put more effort next time!')
    else:
        print('This is a low performance, buckle up next time! ')
                
def main():
    while True:
        print("""
            WELCOME TO DESTINY GROUP OF SCHOOL
            Select an option:
            1. Register
            2. Take the Test
            3. Get Result
            4. Exit
        """)

        user_option = input("Enter your option (1-4): ").strip()
        if user_option == '1':
            register_student()
        elif user_option == '2':
            take_test()
        elif user_option == '3':
            get_result()
        elif user_option == '4':
            print("Thanks for using our service!")
            break
        else:
            print("Invalid selection! Please enter a valid option (1-4).")
main()










# registered_students={}
# students_completed=[]
# for each in range(0, 3):
#     name=input('Enter your name: ')
#     matric_number=input('Enter your matric number: ')
#     registered_students[name]= matric_number
# for each in range(0, 3):
#     ready=input(f'is {student_name } available to take the test(yes or no): ')
#     if ready != 'yes':
#         print('test terminated!')
#         continue
# # attempt=3
# # for attempt >0:
# # matric=input(f'{student_name}Enter your matric number to check if you are eligible for the test')
# # if student_name or matric_number == registered_students:
# #     print(f'{student_name} are you ready to take the test(yes or no)')
# #     attempt -=1
# #     for attempt >0:
# #         print(f"{student_name}")




register_students={}

