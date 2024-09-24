# create a cbt question application
# solution

# questions = {
#     "1.What is 2 + 2?\n (a)22 (b)4 (c)8 :\n ": "b",
#     "2.What is the capital of France?\n (a)USA (b)Ghana (c)Paris:\n": "c",
#     "3.What is 10 / 2?\n (a)3 (b)5 (c)12:\n ": "b",
#     "4.What is the largest planet in the solar system?\n (a)Pluto (b)Venus (c)Mars (d)Jupiter :\n ": "d",
#     "5.What is the boiling point of water in degrees Celsius?\n (a)95 (b)90 (c)100 (d)35 :\n ": "c",
#     "6.What is 5 * 6?\n (a)11 (b)56 (c)30 (d)1 :\n ": "c",
#     "7.What is the square root of 16?\n (a)4 (b)64 (c)36 (d)2 :\n  ": "a",
#     "8.In what year did the Titanic sink?\n (a)1991 (b)1912 (c)1921 (d)1921 :\n ": "b",
#     "9.What is the chemical symbol for water?\n (a)Au (b)H2O (c)HO2 (d)gu :\n ": "b",
#     "10.What is the chemical symbol for gold?\n (a)Au (b)H2O (c)HO2 (d)gu :\n ": "a"
# }

# registered_students={}

# for each in range(0,5):
#     name= input("enter your name: ")
#     matric_number= input("enter your matric number: ")
#     registered_students[matric_number]= name
    
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
#     print(f"\n{matric_number}, your score is {score}/100.\n")
        
#     if each < 4:
#         next_student = input("Is the next student available to take the CBT test? (yes/no): ").lower()
#         if next_student != 'yes':
#             print("Test terminated.")
#             break
        
        
