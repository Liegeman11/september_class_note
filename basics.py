
#single line commenting
#below is multiline commenting
# print("""
# Health is\n Wealth
# """)
# escape characters: \n(new line)

# print("i am now a certified python developer")

"""
variable definition
variable declaration
variable rules
"""
# student_name='Temi','Dara','tikristi','Taiwo'
# print(student_name)

# the name must be descriptive
# you should not start naming with numbering
# do not use reserve words for naming
# no spacing in between names 
# you can not special characters to begin your naming

# fruits='orange','mango'
# fruit2='orange',

# _name='bolu'
# print(_name)

##naming conventions
# pascal
# snake case
# camel casing

# nameOfStudent='Grace'   #camel casing
# name_of_student='Grace'  #snake casing
# NameOfStudent='Grace'    #pascal casing

# #inbuilt python function
# print(type(fruits))
# print(type(fruit2))
# print(len(fruit2))
# print(len(fruit2))
# names_Of_Student=input('what is your name')


# class work: 

# names_Of_patient=input('what is your name:  ')
# age=input('How old are you: ')
# address=input('where do you live>>>> ')
# first_time_patient=print("""is this your first time here>>> 
#                              type:'yes i am new patient' or 'no i am not a new patient'
#                                                >>>""")
# print('my name is '+names_Of_patient+' i am '+age+ 'years old.\n'+'i live at ' +address+ ' and '+first_time_patient)
# print('my name is',names_Of_patient,' i am',age, 'years old.\n','i live at' ,address, 'and',first_time_patient)
# print(f'my name is {names_Of_patient}, i am {age}years old.\n i live at {address} and {first_time_patient}')


# operators python OPERATORS AND IT underscores
# In python programming, operators in general are use to perform operations on values and variables
# types of operators in python
# Arithmetic Opeartors
# comparism Operators
# Logical Operators
# Assignment operators
# Identity OPerators and MEmbership Operators


"""
Operators
Operators in general are used to perform operations on values and variable
Types of operators
1. Arithmetic Operators
2. Comparison Operators
3. Logical Operators
4. Assignment Operators
5. Identity Operators and Membership Operators
"""
"""
Operators
1. Arithmetic Operators

+ Addition: add two operands: x + y
- Subtraction: subtracts two operands x - y
* Multiplication: multiplies to operands x * y
/ Division (float): divides the first operand by the second x / y
// Division (floor): divides the first operand by the second x // y
% Modulus: returns the remainder when the first operand is divided by the second x % y
** Power: returns first raised to power second operand x ** y
"""

"""
2. Comparison Operators

> Greater than: True if the left operand is greater than the right x > y
< Less than: True if the left operand is greater than the right x < y
== Equal to: True if both operands are equal x == y
!= Equal to: True if both operands are equal x != y
>= Greater than or equal to: True if the left operand is greater than or equal to the right operand x >= y
<= Less than or equal to: True if the left operand is greater than or equal to the right operand x <= y
"""

"""
3. Logical Operators

AND: True if both the operand are true x AND y
OR: True if either the operand are true x OR y
NOT: 1. True if the operand is false not x
    2. If one operand is 1 the outcome will be 0
"""

# value2=7
# result=not value2
# # result = bool(value2)
# print(result)

# a= 'mango'
# b= 'orange'
# if len(a) and len(b) == 5:
#     print('both  are the same length')
# else:
#     print('both of them are not of the same length')


# a=11
# b=3
# b +=a
# print(b)
# b -=a
# print(b)
# b *=a
# print(b)
# b <<=a
# print(b)



"""x = 24
y = 20
list = [10, 20, 30, 40, 50]
if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")
"""

"""
score=0
question=input('What is your name: ')
ans=['Dray', 'Dara']
if question in ans:
    score+=5
    print('Correct',score)
else:
    print('Oh noo', score)
"""

# name='  fukunmi olarenwaju'
# # print(len(name))
# name[0]='B'
# print(name)
# print(name.replace('f','b','1'))
# print(name.replace)
studentName='Darasimiamaladudu'
# newName=studentName[0:13] + 'lafun'
# newName=list(studentName)
# newName=[13:]='pupa'
# print(type(newName))
# print(studentName[-4:])
print(studentName[-13:-9])
print(studentName[-17:-13])
print(studentName[-17:-9])
print(studentName[-9:-4])
print(studentName[-4:])
print(studentName[5::3])
# print(name.strip().capitalize())
# print(name.replace())