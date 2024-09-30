import random
questions = {
    "1.What is 2 + 2?\n (a)22 (b)4 (c)8 :\n ": "b",
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


registered_students={}
students_completed=[]

for each in range(0,5):
    name=input('Register your name: ')
    matric_number= input('Register your matric number: ')
    print('Registration Successful!')
    registered_students[name]= matric_number
    
def conduct_test(student_name):
    matric_number = input(f"{student_name}, please enter your matric number to login: ")
    
    if student_name not in registered_students or matric_number != registered_students[student_name]:
        print(f"{student_name}, you are not eligible for the test or your matric number is incorrect.")
        return

    if student_name in students_completed:
        print(f"{student_name}, you have already taken the test. You cannot participate again.")
        return
    students_completed.append(student_name)
    ready = input(f"{student_name}, are you ready to take the CBT test? (yes/no): ").strip().lower()

    if ready != 'yes':
        print("Test terminated.")
        return 
    score = 0
    random_questions = random.sample(list(questions.items()), 5)
    
    for question, correct_answer in random_questions:
        answer = input(question + " ")
        if answer.strip().lower() == correct_answer.lower():
            score += 10
    print(f"\n{student_name}, your score is {score}/50.\n")
for student_name in registered_students.keys():
    if student_name in students_completed:
        continue 
    
    next_student = input(f"Is {student_name} available to take the CBT test? (yes/no): ").strip().lower()
    if next_student == 'yes':
        conduct_test(student_name)
    else:
        print(f"{student_name} is not available.")