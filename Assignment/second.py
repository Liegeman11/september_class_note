# Display an output that describe a student with a matric number and department
# build a static entrance app to describe yourself as SQI student and specify if you have paid

# SOLUTION
# NameOfStudent=input('Please provide your full name: ')
# MatricNumber=input('Provide your matric number: ')
# Department=input('Provide your deparment name: ')
# print('My name is '+NameOfStudent+ ', ''with matric numder '+MatricNumber+', from the '+Department+' department.')



# print('SQI Student Info')
# NameOfStudent=print('Full name:','Emmanuel Taiwo Micheal')
# MatricNumber=print('Matric number:','12345')
# Department=print('Deparment name:','Data Ssience')
# PaymentStatus=print('Payment:','Paid')

# print("""                  
#                             Full name:Emmanuel Taiwo Micheal     
#                             Matric number:12345
#                             Deparment:Data Ssience
#                             Payment:Paid
# """)
# name=input('Enter your name: ')
# matric_number=input('Enter your matric number: ')
# dept=input('Enter your department: ')
# print(f'my name is {name}, from department of {dept} with a matric number {matric_number}')



# print("""                     
#                             enter your full name:Taiwo Emmanuel Micheal
#                             Enter your department:Data Science
#                             enter your matric number:203421
#                             payment status:paid
      


# """)
# for number in range(0, 5):
# for number in range(0, 5):
#     number=int(input('Enter your number: '))
#     if number % 2 ==0:
#         print('The number you entered is an  even')
#     else:
#         print('The number you entered is an odd')
        
# for name in range(1,6):
#     name=input('Enter your name: ')
#     if len(name) % 2 ==0:
#         print('You are in web department')
#     else:
#         print('You are in Data science department')
# score = 0
# question=input('1. Input is used to collect value from: ')
#         ans = ( 'User','user')

# score=0
# for question, correct_anwser in questions.items():
#     answer= input(questions + " ")
#     if answer == correct_anwser:
#         score +=10
#     print('Total score', score)
# score=0
# for question, correct_answer in questions.items():
#     answer = input(question + " ")
#     if answer == correct_answer:
#         score += 10
# print(f"\n Congratulation, your score is {score}/40.\n".center(2000))


# questions= { "1. Input is used to collect value from: ":"user",
#             '2. Variable are like container use to store: ':'data',
#             '3. The basic structural and functional unit of all living organism is: ':'cell',
#             '4. An electronic machine devices that processes data and stores information is: ':'computer',
#             '5. The capital of Nigeria is: ':'abuja',
#             '6. The creator that created all things in a creative ways is: ':'God',
#             '7. The place where we learn to read and write is called: ':'school',
#             '8. what is the smallest unit of matter: ':'atom',
#             '9. Anything that has mass,weight and occupies space is called: ':'matter',
#             '10. The groups of two or more atoms bonded together by chemical bonds is called: ':'molecules'
# }
# score=0
# for question, correct_answer in questions.items():
#     answer= input(question + "").lower().strip()
#     if answer == correct_answer:
#         score +=10
#         print("that's right")
#     else:
#         print("ooh no, Olodo ni ee")
# print(f'\n Good job!!! \n your score is {score}/100'.center(2000))

# set1=int(input('Enter your first set: ').split())
# set2=int(input('Enter your second set: ').split())
# print("\nset operations:")
# print("""                                   1: union
#                                             2: intersection
#                                             3: difference(set2 - set1)
#                                             4: difference(set1 - set2)
#                                             5: superset(set2 - set1)
#                                             6: subset(set2 - set1)
#                                             7: superset(set1 - set2)
#                                             8: subset(set1 - set2)
#         """)
# operation1 =int(input("\nChoose a set operation by entering number (1-8): "))
# if operation1 == '1':
#     result = set1.union(set2)
# elif operation1 == '2':
#     result = set1.intersection(set2)
# elif operation1 == '3':
#     result=set1.different(set2)
# elif operation1 == '4':
#     result=set2.different(set1)
# else:
#     result= 'Invalid operation'

# print("\nResult of the operation: ", result)
# Input two sets from the user
# set1 = set(int, input('Enter elements of your first set separated by space: ').split())
# set2 = set(int, input('Enter elements of your second set separated by space: ').split())

# Display set operations menu
# print("\nSet Operations:")
# print("""1: Union
# 2: Intersection
# 3: Difference (set2 - set1)
# 4: Difference (set1 - set2)
# 5: Is Set2 a Superset of Set1?
# 6: Is Set2 a Subset of Set1?
# 7: Is Set1 a Superset of Set2?
# 8: Is Set1 a Subset of Set2?
# """)

# # Ask the user to choose an operation
# operation1 = input("\nChoose a set operation by entering a number (1-8): ")

# # Perform the operation based on user input
# if operation1 == '1':
#     result = set1.union(set2)
# elif operation1 == '2':
#     result = set1.intersection(set2)
# elif operation1 == '3':
#     result = set2.difference(set1)
# elif operation1 == '4':
#     result = set1.difference(set2)
# elif operation1 == '5':
#     result = set2.issuperset(set1)
# elif operation1 == '6':
#     result = set2.issubset(set1)
# elif operation1 == '7':
#     result = set1.issuperset(set2)
# elif operation1 == '8':
#     result = set1.issubset(set2)
# else:
#     result = "Invalid operation"

# # Display the result of the operation
# print("\nResult of the operation:", result)
registered_students={}
students_completed=[]
for each in range(0, 3):
    name=input('Enter your name: ')
    matric_number=input('Enter your matric number: ')
    registered_students[name]= matric_number
for student_name in registered_students.keys():
    if student_name in students_completed:
        continue
    next_student=input(f'is {student_name } available to take the test(yes or no): ')
    if ready != 'yes':
        print('test terminated!')
        continue
    attempts=3
    while attempts > 0:
        matric_number=input(f'{student_name} enter your matric number to check if you are eligible to take the test: ')
        
#     if student_name 
# for each in range(0, 3):