# create a cbt question application
# solution
import random
questions = {
    "1.What is 2 + 2?\n (a)22 (b)4 (c)8 \nanswer: ": "b",
    "2.What is the capital of France?\n (a)USA (b)Ghana (c)Paris:\n": "c",
    "3.What is 10 / 2?\n (a)3 (b)5 (c)12:\n ": "b",
    "4.What is the largest planet in the solar system?\n (a)Pluto (b)Venus (c)Mars (d)Jupiter :\n ": "d",
    "5.What is the boiling point of water in degrees Celsius?\n (a)95 (b)90 (c)100 (d)35 :\n ": "c",
    "6.What is 5 * 6?\n (a)11 (b)56 (c)30 (d)1 :\n ": "c",
    "7.What is the square root of 16?\n (a)4 (b)64 (c)36 (d)2 :\n  ": "a",
    "8.In what year did the Titanic sink?\n (a)1991 (b)1912 (c)1921 (d)1921 :\n ": "b",
    "9.What is the chemical symbol for water?\n (a)Au (b)H2O (c)HO2 (d)gu :\n ": "b",
    "10.What is the chemical symbol for gold?\n (a)Au (b)H2O (c)HO2 (d)gu :\n ": "a"
}

# registered_students={}
# student_completed=[]

# for each in range(0,5):
#     name= input("enter your name: ").lower()
#     matric_number= input("enter your matric number: ")
#     registered_students[matric_number]= name
# print(registered_students)
    
# for each in range(0,5):
#     matric_number = input("Enter your matric no to check if you are eligible for the test: ")

#     if matric_number not in registered_students:
#         print(f"{matric_number}, you are not eligible for the test. Please register first.\n")
#         continue
#     ready = input(f"{matric_number}, are you ready to take the CBT test? (yes/no): ").lower()
#     if ready !='yes':
#         print('Test terminated.')
#         continue
#     score=0
#     for question, correct_answer in questions.items():
#         answer = input(question + " ")
#         if answer == correct_answer:
#             score += 10
#     print(f"\n{matric_number}, your score is {score}/100.\n".center(200))
        
#     if each < 4:
#         next_student = input("Is the next student available to take the CBT test? (yes/no): ").lower()
#         if next_student != 'yes':
#             print("Test terminated.")





    
    

registered_students = {}  
students_completed = []   

for each in range(0,3):
    name = input("Register your name: ")
    matric_number = input("Register your matric number: ")
    print("Registration successful!")
    registered_students[name] = matric_number 
print(registered_students)
print("hello 1", students_completed)
for student_name in registered_students.keys():
    
    if student_name in students_completed:
        print("hello 2 in loop", students_completed)
        continue  
    next_student = input(f"Is {student_name} available to take the CBT test? \n(yes/no): ").strip().lower()
    
    if next_student != 'yes':
        print(f"{student_name} is not available.")
        continue
    matric_number = input(f"{student_name}, please enter your matric number to login: ")
    
    if matric_number != registered_students[student_name]:
        print(f"{student_name}, your matric number is incorrect. You are not eligible for the test.")
        continue
    if student_name in students_completed:
        print(f"{student_name}, you have already taken the test. You cannot participate again.")
        continue

    students_completed.append(student_name)
    print("hello appended", students_completed)

    ready = input(f"{student_name}, are you ready to take the CBT test? (yes/no): ").strip().lower()

    if ready != 'yes':
        print(f"{student_name}, test terminated. You are not taking the test.")
        continue

    score = 0
    random_questions = random.sample(list(questions.items()), 3) 
    
    for question, correct_answer in random_questions:
        answer = input(question + " ") 
        if answer.lower() == correct_answer.lower():  
            score += 10 
    print(f"\n{student_name}, your score is {score}/50.\n")



















# registered_students={}
# students_completed=[]
# def student_list():
#     for each in range(0,3):
#         name=('Register your name: ')
#         matric_number=('Register your matric number: ')
#         # registered_students[name]= matric_number
#         registered_student = name, matric_number
#         registered_students.append(registered_student)
#     print(registered_students)
# student_list()


