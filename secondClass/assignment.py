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
#         print('Existing the program')
#         exit()
    
    
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
#     result="This number is a prime number" if num % i ==0 else 'this number is not a prime number' 
#     print(result)




list_of_optn=['1.buy airtime', '2.buy data', '3.borrow airtime', '4.check balance', '5.share with friends and family', '6.recharge']
buy_data=['1.TopDeal4Me', '2.Data4Me', '3.Smart Data','4.Combo4Me' ]
def main():
    users=input('Enter a code: ')
    if users != '*234#':
        print('Invalid entry!')
    else:
        for each in list_of_optn:
            print(each)
        option=input('Select an option: ')
        if option == '1':
            phone_no=input('Enter your phone number:  ')
            if len(phone_no) != 11:
                print("The number you enter is invalid!")
                return
            amount=int(input('Enter the amount; '))
            if amount >= 50:
                print('Airtime recharge successful')
            else:
                print('the amount must not be less than 50')
                return
        if option == '2':
            for each in buy_data:
                print(each)
                data_plan=input('Select a plan: ')
                if data_plan == '1':
                    TopDeal()
            
main()
def TopDeal():
    print("""   1.Get 10GB +20 voice mins for N2,000(1 month)
                1.Get 50GB +30 voice mins for N5,500(1 month) 
                1.Get 80GB +40 voice mins for N11,000(1 month) 
    """)
    opt=input('Enter an option: ')
    if opt == '1':
        print('Data purchase successful. you have received 10GB +20 voice mins for N2,000. Valid for one month')
    elif opt =='2':
        print('Data purchase successful. you have received 50GB +30 voice mins for N2,000. Valid for one month')
    elif opt =='3':
        print('Data purchase successful. you have received 80GB +40 voice mins for N2,000. Valid for one month')
    else:
        print('Invalid selection!')
        return


