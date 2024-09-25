# def landing_page():
#     print("""
#                         1.Login
#                         2.register
#                         3.make enquiry
#                         4.exit
#         """)
#     user=input('select option>>>> ')
#     if user == '1':
#         print('welcome')
#     elif user == '2':
#         print('welcome!!! you can now register ')
#     elif user == '3':
#         print('what do you want? ')
#     elif user == '4':
#         exit()
# landing_page()

z=10

def add_num(x):
    global b
    b=3
    q=18  #local variable
    sum_all= x + 6 + z + q + b
    print(sum_all)
add_num(4)

# def add_num(x, y):
#     sum_all= x + 6 + y + x + z + b
#     print(sum_all)
# add_num(4, 2)

def subtract_num(i, j):
    sub_all= i - 6 - j + j
    print(sub_all)
subtract_num(28, 3)

"""
types of arguments
1. default args
2. keyword args
3. psitional args
4. arbitrary args
"""

## 1. default args
def add_num(x, y=10):
    global b
    b=3
    q=18  #local variable
    sum_all= x + 6 + z + q + b
    print(sum_all)
add_num(4)

def add_num(x=10, y=3):
    global b
    b=3
    q=18  #local variable
    sum_all= x + 6 + z + q + b +y
    print(sum_all)
add_num(4)

## 2. keyword args

def college(name, location):
    print(name, location)
    
college(name='SQI', location='Yoaco')
college(location='Yoaco', name='SQI')

## 3. psitional args
def college_class(college, level):
    print(f'My name is Bolu I study at {college} and my level is {level}')
    
college_class('SQI','level2')
college_class('level2','SQI')

## 4. arbitrary args
def college_class(**kwargs):
    print(kwargs.keys())
    print(kwargs.values())
    
college_class(name='SQI', level='level2', address='home',name2='titi',name3='dara' )
college_class('level2','SQI')

