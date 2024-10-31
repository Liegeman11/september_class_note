# num= int(input('enter your number: '))
# if num % 2 ==0:
#     print('The number you enter is an even number.')
# else:
#     print('The number you enter is an odd number.')
    
    
    
# val1=int(input('Enter a number: '))
# val2=2
# print(f'if the result is one the number you enter is an odd number and if it is zero the number you enter is an even number. Your result is {val1%val2}')
# val2=[-4]
# print(not val2)
# print(val1%val2)
# print(val1>val2)
# print(val1<val2)
    
    
# score= 25
# score +=10
# score -=100
# print(score)

# student1= "johnwicko"
# print(len(student1))
# print(student1[1:8])
# print(student1[-4:-1])
# print(student1[1::2])
# print(student1.count('o'))
# print(student1.find('o'))
# print(student1.endswith('e'))
# print(student1.endswith('e'))
# print(student1.isalnum)

# Build a palidriom checker

# slipt, strip, replace, isnum 

# write a demo on how a cooperative sector works


# word=input('Enter a word: ').strip()
# reversed_word= word[::-1]
# print(reversed_word)

# result= word == reversed_word
# print(result)

# if word == reversed_word:
#     print(f"'{word1}' is a palindrome.")
    
# else:
#     print(f"'{word1}'. is not a palindrome")


# name= '   toluwani is a python instructor'
# # print(name.strip())
# # print(name.split())
# print(name.replace('t','S',1))
# print(name.replace('instructor','Student'))





"""
list- this is a data type that s ordered changeable index and can accept any other data type
"""

""""
tuple

"""
# print("""
#                                     welcome to JPGROUPS OF SCHOOL
#                 SELECT
#                 1.REGISTER
#                 2.EXIT
# """)
# user_option=input("Enter your option: ")
# list_of_name=[]
# logged_in_user=[]
# if user_option == '1':
#     for each in range(0,2):
#         user=input('Enter you name: ').lower().strip()
#         # age=int(input('Enter your age: '))
#         # address=input('Enter your address: ').lower().strip()
#         password=input('Enter password: ')
#         print(f'{user} You are successfully registered!')
#         list_of_name.append([user, password])
#     print(list_of_name)
#     while True:
#         user_name=input('Enter your name: ')
#         user_password=input('Enter your password to login: ').lower().strip()
#         if user_name in logged_in_user:
#             print(f'{user_name}, you have already logged in. you cannot login again')
#             continue
#         login_Successfully= False
#         for name in list_of_name:  
#             if user_name == name[0] and user_password == name[1]:
#                 print(f'Welcome {user_name} You are successfully logged in!')
#                 login_Successfully= True
#                 logged_in_user.append(user_name)
#         if login_Successfully == False:
#             print('Incorrect name or password. please try again or register first')
# else:
#     exit()

# student_info=(('kike', 'blue','1000'),('tolu', 'yellow', '5000'),('malik','green', '2000'),('isreal', 'black','3000'))
# info1,info2,info3,info4=student_info
# print(info1)
# print(info1[0],info2[0],info3[0],info4[0])
# for name,color,acct_bal in student_info:
#     print(name)
#     print(f'{name} | {color}')
    
# info1,*other,info4=student_info
# print(info1)
# print(other)


                        #dictionaries#

# itm={'name1':'bankole','name2':'bankole','name3':'bankole','name4':'bankolew'}
# itms=dict(name1='bankole',name2='bankole',name3='bankole',name4='bankolew')
# # print(itm['name1'])
# # print(itms['name4'])
# # print(itms.items())
# # print(itms.keys())
# # print(itms.values())

# # for ky, val in itm.items():
# #     print(f'{ky} : {val}')
# print('i am name 1', itm.get('name1'))
# itm.update(dict(name1='boluwatife'))
# # itms.update({'name2':'bolu'})
# print(itm)
# set.intersection
# import sys

# print("""                       WELCOME TO THE GAME

#                             1.PARTICIPATE
#                             2. EXIT
# """)
# choice=input("Enter your option: ").lower().strip()
# options=set(['mango', 'pawpaw','orange','pineapple','banana'])
# if choice =='1':
#     print(options)
#     ans=options.pop()
#     answer=input('Guess the right output: ').lower().strip()
#     print(ans)
#     score =0
#     if answer  == ans:
#         print("Good of you...")
#         score +=50
#     else:
#         print(f"You are wrong. The correct answer is {ans}")
#     print('Total score: ', score)
# else:
#     exit()




# questions={   
#                 "1.What is the primary function of the legislative branch of government: (a) To enforce laws (b) To interpret laws (c) To make laws (d) To implement polices ":'c',
#                 "2.Which of the following is not a renewable source of energy (a)Solar energy (b) Wind energy (c) Coal (d) Hydropower ":'c',
#                 "3.What is the value of x? when 3x + 7 = 22 (a)10 (b)2 (c)5 (d)7 ":'c',
#                 "4.In plants, photosynthesis primary takes place in which part? (a)Roots (b)Stem (c)Leaves (d)Flowers":'c',
#                 "5.which of the following is the longest river in Nigeria (a)River Benue (b)River Kaduna (c)River Niger (d)River Osun ":'c',
#                 "6.what is the term for an increase in the general level of prices? (a)Deflation (b)Inflation (c)Recession (d)Depression ":'b'
#                 # "7.":


# }
# print("""
# #                                     welcome to JPGROUPS OF SCHOOL
# #                 SELECT
# #                 1.REGISTER
# #                 2.EXIT
# # """)
# user_option=input("Enter your option(1-2): ")
# list_of_users={}
# logged_in_user=[]
# if user_option == '1':
#     for each in range(0,2):
#         while True:
#             user=input('Enter your name : ').lower().strip()
#             if user in list_of_users:
#                 print(f"{user} already exists, please use another name.")
#                 continue
#             age=int(input('Enter your age: '))
#             address=input('Enter your address: ').lower().strip()
#             password=input('Enter password: ')
#             print(f'{user} You are successfully registered!')
            
#         # list_of_name.append([user, password])
#             list_of_users[user]=password
#             print(list_of_users)
#             break
#     print(list_of_users)
#     while True:
#         user_name=input('Enter your name to login: ').lower().strip()
#         user_password=input('Enter your password to login: ')
#         if user_name in logged_in_user:
#             print(f'{user_name}, you have already logged in and take the test. you cannot login again')
#             continue
#         login_Successfully= False
#         for name in list_of_users:  
#             if user_name == name[0] and user_password == name[1]:
#                 print(f'Welcome {user_name} You are successfully logged in!')
#                 login_Successfully= True
#                 logged_in_user.append(user_name)
#         if login_Successfully == False:
#             print('Incorrect name or password. please try again or register first')
#             continue
#         ready=input(f"{user_name}, are you ready to take the cbt test?(yes or no): ").strip().lower()
#         if ready != "yes":
#             print(f'{user_name},Test terminated. you are not taking the test.')
#             continue
#         score=0
#         for question, correct_answer in questions.items():
#             answer=input(question+ " ")
#             if answer == correct_answer:
#                 score+=10
#         print(f"{user_name}, You total score is {score}/50")
# else:
#     exit()
    
# set1 = set(map(int, input("Enter elements of the first set, separated by spaces: ").split()))
# set2 = set(map(int, input("Enter elements of the second set, separated by spaces: ").split()))
# while True:
#     print("""               
#     1. Intersection
#     2. Subset
#     3. Symmetric Difference
#     4. Difference
#     5. Superset
#     6. Disjoint
#     7. Subset
#     """)

#     choice = input("Choose the operation you want to perform (1-7): ")

#     if choice == '1':
#         result = set1.intersection(set2)
#         print("Intersection:", result)
#     elif choice == '2':
#         result = set1.issubset(set2)
#         print("Is Subset:", result)
#     elif choice == '3':
#         result = set1.symmetric_difference(set2)
#         print("Symmetric Difference:", result)
#     elif choice == '4':
#         result = set1.difference(set2)
#         print("Difference (set1 - set2):", result)
#     elif choice == '5':
#         result = set1.issuperset(set2)
#         print("Is Superset:", result)
#     elif choice == '6':
#         result = set1.isdisjoint(set2)
#         print("Is Disjoint:", result)
#     elif choice == '7':
#         result = set1.issubset(set2)
#         print("Is Subset:", result)
#     else:
#         print("Invalid choice.")
        

#     another=input("Do you want to perform another operation(yes/no): ").strip().lower()
#     if another != 'yes':
#         print('Exiting the program')
#         exit()
    

                    #CONDITIONAL STATEMENT#
# name="Malik"
# if name =='malick':
#     print("yeeeeeh! you know my name")
# else:
#     print("You are wrong")

# name="Macus"
# if name =='malick':
#     print("yeeeeeh! you know my name")
# else:
#     if name == 'surajudeen':
#         print("I have a nice name")
#     else:
#         if name == "bankole":
#             print('I an the tall man of the class.')
#         else:
#             print("All the names does not match!!!")
            

            
























































# num=int(input('Enter a number: '))
# if num % 2 == 0:
#     print(f"{num} is an even number.")
# else:
#     print(f"{num} is an odd number.")

# num=int(input('Enter a number: '))
# for i in range(0, 10):
#         if i % num == 0:
#             print(f"{num} is a prime number.")
#             break
# else:
#     print(f"{num} is not a prime number.")


# num=int(input('Enter a number: '))
# for i in range(2, num):
#     if num % i == 0:
#         print(f"{num} is not a prime number.")
#         break
# else:
#     print(f"{num} is a prime number.")
    
# num = int(input('enter a number>>>  '))
# while True:
#     for i in range(0, 10):
#         if num % 2 == 0:
#             print(f"this is an even number")
#             break
#     else:
#         print(f"this is an odd number")
#         break
#     another=input("Do you want to input another number(yes/no): ")
#     if another != 'yes':
#         break
#     else:

# num = int(input('enter a number>>>  '))
# while True:
#     for i in range(0, 10):
#         if num % 2 == 0:
#             print(f"this is an even number")
#             break
#     else:
#         print(f"this is an odd number")
#         break
#     another=input("Do you want to input another number(yes/no): ")
#     if another != 'yes':
#         another=num
#         print(another)
#         break
#     else:
#         print(f"enter a number")
        
        
                        #    TENARY EXPRESSION CONDITIONAL STATEMENT   #    
# age=int(input('Enter your age: '))
# status=" You are still a Child" if age < 13 else "You are a Teenager" if age <18 else 'You are an Adult'
# print(status)

# num=int(input('Enter a number: '))
# result="This is an even number" if num % 2 ==0 else 'this number is an odd number' 
# print(result)

# num=int(input('Enter a number: '))
# result="This number is a negative number" if num <0 else 'this number is a positive number' 
# print(result)

# num=int(input('Enter a number: '))
# for i in range(2,num):
#     result="This number is a prime number" if num % i ==0  else 'this number is not a prime number' 
#     print(result)

                                #  loop  #

# num=0
# while num <5:
#     print("Hello")
#     num+=1
    
# list_itm=['Taiwo','Tolu', 'Bimbo', 'Kunle']
# for name in list_itm:
#     print('\n'+name)
# num_time=0
# for each in range(5):
#     num_time+=1
#     print(f"Round {num_time}")
#     username=input("Enter your name: ")
#     pawd=input("Enter your password: ")
#     address=input("Enter your address: ")
# num_time=0
# for i in range(1,13):
#     num_time+=1
#     print(f"\nMultiplication Table {num_time}")
#     for j in range(13):
#         print(f"{i}*{j}= {i*j}", end="\t")

# sets=[]
# print("Hello you are welcome")
# num_of_user=int(input("Enter number of student to register: "))
# set_element={}
# for each in range(1,num_of_user+1):
#     number_col=int(input(f"Enter number of a column in student {each} details: "))
#     for all in range(1, number_col+1):
#         name=input(f"Enter the name of colum {all}: ")
        

# print("Hello, you are welcome!")
# num_of_user = int(input("Enter the number of students to register: "))

# students = []  # List to store each student's details

# for each in range(1, num_of_user + 1):
#     print(f"\nEntering details for student {each}:")
#     number_col = int(input(f"Enter the number of columns for student {each} details: "))
    
#     student_info = {}  # Dictionary to store individual student's details
#     for col in range(1, number_col + 1):
#         column_name = input(f"Enter the name of column {col}: ")
#         column_value = input(f"Enter the value for '{column_name}': ")
#         student_info[column_name] = column_value  # Add detail to the student's dictionary
    
#     students.append(student_info)  # Add the student's details to the main list

# # Display all students' details
# print("\nRegistered Students:")
# for idx, student in enumerate(students, start=1):
#     print(f"\nStudent {idx} details:")
#     for key, value in student.items():
#         print(f"{key}: {value}")

# print("Hello, you are welcome!")
# sets=[]
# num_of_set=int(input("Enter the number of set you want to work with: "))
# for each in range(1,num_of_set+1):
#     print(f"\n Entering the details in set {each}")
#     num_element=int(input(f"\n Enter the number of element in set {each}: "))
#     set_info=[]
#     for all in range(1,num_element+1):
#         enter_element=int(input(f"\n Enter element {all}in set {each}: "))
#         set_info.append(enter_element)
#     sets.append(set_info)
    
# # while True:
#     print("""               
#     1. Intersection
#     2. Subset
#     3. Difference
#     4. Symmetric Difference
#     5. Disjoint 
#     6. Subset
#     7. Superset
#     """)

#     choice = input("Choose the operation you want to perform (1-7): ")
#     if choice in ['1', '2', '3', '4', '5', '6', '7']:
#         selected_indices = input("Enter the indices of sets to work with (e.g., 1 2): ")
#         selected_sets = [sets[int(index) - 1] for index in selected_indices.split() if index.isdigit() and 1 <= int(index) <= num_of_set]
        
#         if len(selected_sets) < 2:
#             print("Please select at least two valid sets.")
#             continue

#         if choice == '1':
#             result = set.intersection(*selected_sets)
#             print("Intersection of selected sets:", result)
#         elif choice == '2':
#             result = set.union(*selected_sets)
#             print("Union of selected sets:", result)
#         elif choice == '3':  # Difference
#             result = selected_sets[0].difference(*selected_sets[1:])
#             print("Difference of selected sets:", result)
#         elif choice == '4':  # Symmetric Difference
#             result = set.symmetric_difference(*selected_sets)
#             print("Symmetric Difference of selected sets:", result)
#         elif choice == '5':  # Disjoint
#             result = all(selected_sets[i].isdisjoint(selected_sets[j]) for i in range(len(selected_sets)) for j in range(i + 1, len(selected_sets)))
#             print("Are the selected sets pairwise disjoint?", result)
#         elif choice == '6':  # Subset
#             result = all(selected_sets[0].issubset(s) for s in selected_sets[1:])
#             print("Is the first set a subset of all selected sets?", result)
#         elif choice == '7':  # Superset
#             result = all(selected_sets[0].issuperset(s) for s in selected_sets[1:])
#             print("Is the first set a superset of all selected sets?", result)
#     else:
#         print("Invalid choice. Please select a number between 1 and 7.")


#     another=input("Do you want to perform another operation(yes/no): ").strip().lower()
#     if another != 'yes':
#         print('Exiting the program')
#         exit()
    
# print("Hello, you are welcome!")
# sets = []
# num_of_set = int(input("Enter the number of sets you want to work with: "))
# for each in range(1, num_of_set + 1):
#     print(f"\nEntering the details for set {each}")
#     num_element = int(input(f"Enter the number of elements in set {each}: "))
#     set_info = set()
#     for all in range(1,num_element+1):
#         enter_element = int(input(f"Enter element {all} in set {each}: "))
#         set_info.add(enter_element)
#     sets.append(set_info)

# while True:
#     print("""               
#     1. Intersection
#     2. Union
#     3. Difference
#     4. Symmetric Difference
#     5. Disjoint
#     6. Subset
#     7. Superset
#     """)

#     choice = input("Choose the operation you want to perform (1-7): ")
#     if choice in ['1', '2', '3', '4', '5', '6', '7']:
#         selected_indices = input("Enter the indices of sets to work with (e.g., 1 2): ")
#         selected_sets = [sets[int(index) - 1] for index in selected_indices.split() if index.isdigit() and 1 <= int(index) <= num_of_set]
        
#         if len(selected_sets) < 2:
#             print("Please select at least two valid sets.")
#             continue

#         if choice == '1':
#             result = set.intersection(*selected_sets)
#             print("Intersection of selected sets:", result)
#         elif choice == '2':
#             result = set.union(*selected_sets)
#             print("Union of selected sets:", result)
#         elif choice == '3':  # Difference
#             result = selected_sets[0].difference(*selected_sets[1:])
#             print("Difference of selected sets:", result)
#         elif choice == '4':  # Symmetric Difference
#             result = set.symmetric_difference(*selected_sets)
#             print("Symmetric Difference of selected sets:", result)
#         elif choice == '5':
#             result = all(selected_sets[each].isdisjoint(selected_sets[all]) for each in range(len(selected_sets)) for all in range(each + 1, len(selected_sets)))
#             print("Are the selected sets pairwise disjoint?", result)
#         elif choice == '6':
#             result = all(selected_sets[0].issubset(s) for s in selected_sets[1:])
#             print("Is the first set a subset of all selected sets?", result)
#         elif choice == '7':
#             result = all(selected_sets[0].issuperset(s) for s in selected_sets[1:])
#             print("Is the first set a superset of all selected sets?", result)
#     else:
#         print("Invalid choice. Please select a number between 1 and 7.")

#     another = input("Do you want to perform another operation (yes/no)? ").strip().lower()
#     if another != 'yes':
#         print('Exiting the program')
#         break



from functools import reduce

print("Hello, you are welcome!")
sets = []
num_of_set = int(input("Enter the number of sets you want to work with: "))

# Collect elements for each set
for each in range(1, num_of_set + 1):
    print(f"\nEntering the details for set {each}")
    num_element = int(input(f"Enter the number of elements in set {each}: "))
    set_info = set()  # Using a set directly
    for all in range(1, num_element + 1):
        enter_element = int(input(f"Enter element {all} in set {each}: "))
        set_info.add(enter_element)
    sets.append(set_info)  # Appending the set directly

# Menu for set operations
while True:
    print("""               
    1. Intersection
    2. Union
    3. Difference
    4. Symmetric Difference
    5. Disjoint
    6. Subset
    7. Superset
    """)

    choice = input("Choose the operation you want to perform (1-7): ")
    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        selected_indices = input("Enter the indices of sets to work with (e.g., 1 2): ")
        selected_sets = [sets[int(index) - 1] for index in selected_indices.split() if index.isdigit() and 1 <= int(index) <= num_of_set]
        
        if len(selected_sets) < 2:
            print("Please select at least two valid sets.")
            continue

        if choice == '1':  # Intersection
            result = reduce(lambda x, y: x & y, selected_sets)
            print("Intersection of selected sets:", result)
        elif choice == '2':  # Union
            result = reduce(lambda x, y: x | y, selected_sets)
            print("Union of selected sets:", result)
        elif choice == '3':  # Difference
            result = reduce(lambda x, y: x - y, selected_sets)
            print("Difference of selected sets:", result)
        elif choice == '4':  # Symmetric Difference
            result = reduce(lambda x, y: x ^ y, selected_sets)
            print("Symmetric Difference of selected sets:", result)
        elif choice == '5':  # Disjoint
            result = all(selected_sets[i].isdisjoint(selected_sets[j]) for i in range(len(selected_sets)) for j in range(i + 1, len(selected_sets)))
            print("Are the selected sets pairwise disjoint?", result)
        elif choice == '6':  # Subset
            result = all(selected_sets[0].issubset(s) for s in selected_sets[1:])
            print("Is the first set a subset of all selected sets?", result)
        elif choice == '7':  # Superset
            result = all(selected_sets[0].issuperset(s) for s in selected_sets[1:])
            print("Is the first set a superset of all selected sets?", result)
    else:
        print("Invalid choice. Please select a number between 1 and 7.")

    another = input("Do you want to perform another operation (yes/no)? ").strip().lower()
    if another != 'yes':
        print('Exiting the program')
        break



# print("Hello, you are welcome!")
# sets = []
# num_of_set = int(input("Enter the number of sets you want to work with: "))

# # Collect elements for each set
# for each in range(1, num_of_set + 1):
#     print(f"\nEntering the details for set {each}")
#     num_element = int(input(f"Enter the number of elements in set {each}: "))
#     set_info = set()  # Using a set directly
#     for all in range(1, num_element + 1):
#         enter_element = int(input(f"Enter element {all} in set {each}: "))
#         set_info.add(enter_element)
#     sets.append(set_info)  # Appending the set directly

# # Menu for set operations
# while True:
#     print("""               
#     1. Intersection
#     2. Union
#     3. Difference
#     4. Symmetric Difference
#     5. Disjoint
#     6. Subset
#     7. Superset
#     """)

#     choice = input("Choose the operation you want to perform (1-7): ")
#     if choice in ['1', '2', '3', '4', '5', '6', '7']:
#         selected_indices = input("Enter the indices of sets to work with (e.g., 1 2): ")
#         selected_sets = [sets[int(index) - 1] for index in selected_indices.split() if index.isdigit() and 1 <= int(index) <= num_of_set]
        
#         if len(selected_sets) < 2:
#             print("Please select at least two valid sets.")
#             continue

#         if choice == '1':  # Intersection
#             result = set.intersection(*selected_sets)
#             print("Intersection of selected sets:", result)
#         elif choice == '2':  # Union
#             result = set.union(*selected_sets)
#             print("Union of selected sets:", result)
#         elif choice == '3':  # Difference
#             result = selected_sets[0].difference(*selected_sets[1:])
#             print("Difference of selected sets:", result)
#         elif choice == '4':  # Symmetric Difference (handled iteratively)
#             result = selected_sets[0]
#             for s in selected_sets[1:]:
#                 result = result.symmetric_difference(s)
#             print("Symmetric Difference of selected sets:", result)
#         elif choice == '5':  # Disjoint
#             result = all(selected_sets[i].isdisjoint(selected_sets[j]) for i in range(len(selected_sets)) for j in range(i + 1, len(selected_sets)))
#             print("Are the selected sets pairwise disjoint?", result)
#         elif choice == '6':  # Subset
#             result = all(selected_sets[0].issubset(s) for s in selected_sets[1:])
#             print("Is the first set a subset of all selected sets?", result)
#         elif choice == '7':  # Superset
#             result = all(selected_sets[0].issuperset(s) for s in selected_sets[1:])
#             print("Is the first set a superset of all selected sets?", result)
#     else:
#         print("Invalid choice. Please select a number between 1 and 7.")

#     another = input("Do you want to perform another operation (yes/no)? ").strip().lower()
#     if another != 'yes':
#         print('Exiting the program')
#         break

