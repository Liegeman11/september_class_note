# create a cbt question application

#                   solution
    
import random
questions = {
    ">>.What is 2 + 2?\n (a)22 (b)4 (c)8 \nanswer: ": "b",
    ">>.What is the capital of France?\n (a)USA (b)Ghana (c)Paris:\n": "c",
    ">>.What is 10 / 2?\n (a)3 (b)5 (c)12:\n ": "b",
    ">>.What is the largest planet in the solar system?\n (a)Pluto (b)Venus (c)Mars (d)Jupiter :\n ": "d",
    ">>.What is the boiling point of water in degrees Celsius?\n (a)95 (b)90 (c)100 (d)35 :\n ": "c",
    ">>.What is 5 * 6?\n (a)11 (b)56 (c)30 (d)1 :\n ": "c",
    ">>.What is the square root of 16?\n (a)4 (b)64 (c)36 (d)2 :\n  ": "a",
    ">>.In what year did the Titanic sink?\n (a)1991 (b)1912 (c)1921 (d)1921 :\n ": "b",
    ">>.What is the chemical symbol for water?\n (a)Au (b)H2O (c)HO2 (d)gu :\n ": "b",
    ">>.What is the chemical symbol for gold?\n (a)Au (b)H2O (c)HO2 (d)gu :\n ": "a",
    ">>.What is the primary function of the legislative branch of government: (a) To enforce laws (b) To interpret laws (c) To make laws (d) To implement polices ":'c',
    ">>.Which of the following is not a renewable source of energy (a)Solar energy (b) Wind energy (c) Coal (d) Hydropower ":'c',
    ">>.What is the value of x? when 3x + 7 = 22 (a)10 (b)2 (c)5 (d)7 ":'c',
    ">>.In plants, photosynthesis primary takes place in which part? (a)Roots (b)Stem (c)Leaves (d)Flowers":'c',
    ">>.which of the following is the longest river in Nigeria (a)River Benue (b)River Kaduna (c)River Niger (d)River Osun ":'c'
}
print("""
#                                     WELCOME TO DESTINY GROUP OF SCHOOL
#                 SELECT
#                 1.REGISTER
#                 2.EXIT
# """)
user_option=input("Enter your option(1-2): ")
registered_students = {}  
students_completed = []   
if user_option == '1':
    for each in range(0,3):
        while True:
            name = input("Register your name: ")
            if name in registered_students:
                print(f"{name} already exists, please use another name.")
                continue
            matric_number = input("Register your matric number: ")
            if matric_number in registered_students:
                print(f"{matric_number} already exists, please use another name.")
                continue
            print("Registration successful!")
            registered_students[name] = matric_number
            break 
    print(registered_students)
# print("hello 1", students_completed)
    for student_name in registered_students.keys():
        if student_name in students_completed:
            continue  
        next_student = input(f"Is {student_name} available to take the CBT test? \n(yes/no): ").strip().lower()
    
        if next_student != 'yes':
            print(f"{student_name} is not available.")
            continue
        attempt = 3
        while attempt > 0:
            matric_number = input(f"{student_name}, please enter your matric number to login: ").lower().strip()
            if matric_number == registered_students[student_name]:
                break 
            else:
                attempt -= 1
                if attempt > 0:
                    print(f"Incorrect matric number. You have {attempt} attempts left.")
                else:
                    print(f"Sorry, {student_name}, you have been locked out due to multiple failed attempts.")
                    break
        if attempt == 0:
            continue
        if student_name in students_completed:
            print(f"{student_name}, you have already taken the test. You cannot participate again.")
            continue
        students_completed.append(student_name)
        # print("hello appended", students_completed)

        ready = input(f"{student_name}, are you ready to take the CBT test? (yes/no): ").strip().lower()

        if ready != 'yes':
            print(f"{student_name}, test terminated. You are not taking the test.")
            continue

        score = 0
        random_questions = random.sample(list(questions.items()), 5) 
    
        for question, correct_answer in random_questions:
            answer = input(question + " ") 
            if answer.lower() == correct_answer.lower():  
                score += 10 
        print(f"\n{student_name}, your score is {score}/50.\n")
    else:
        exit()



















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
