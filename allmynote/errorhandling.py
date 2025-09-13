


# for i in range(1,4):
#     try:
#         rand_num=int(input('Enter a number: '))
#         print(f'the num is {rand_num}')
#     except ValueError:
#         print('enter an integer')
    
    
# num=[1, 2, 3]
# try:
#     print('second element = %d' %(num[3]))
#     print('fourth element = %d' %(num[2]))
    
# except IndexError:
#     print('index out of range')
# finally:
#     print('program completed')

# amt= 1000
# amount=int(input('Enter an amount: '))
# if amount <= amt:
#     print('you are eliglible to purchase the goods.')
# elif amount > amt:
#     print('you are not eliglible to purchase the goods.')
# elif amount< amt:
#     print('Out of range! Enter a correct amount.')
# else :
#     print('Out of range! Enter a correct amount.')
#     exit()



# try:
#     set1=int(input('Enter your first set: '))
#     set2=int(input('Enter your second set: '))
#     union_result= set1 + set2
#     print(union_result)
# except IndexError:
#     print(union_result)
    

# try:
#     set1=input('Enter your first set: ')
#     set2=input('Enter your second set: ')
#     union_result= set1 .union(set2)
# except ValueError:
#         print('enter an integer')



import re
email = "bola@gmail.com"
# if email.endswith(".com"):
#     print("invalid email")
# else:
#     print("invalid")
val_search = re.search("^@.*com$", email)
if val_search:
    print('valid email')
else:
    print("invalid")