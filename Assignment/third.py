# Build even and odd number checker
# collect names of student and group them into two different department
# set five structural cbt questions and grade the student

# Solutions

"""
1.
number = int(input('Enter a number: '))
if numder % 2 == 0:
    print('The number you enter is an even number')
    else:
        print('The number you enter is an odd numder')

"""

"""
2.
name = input('Enter your name: ')
if len(name) %  9 == 5:
    print('You are in Data Science')
else :
    print('You are in Web development')
"""


score = 0
question=input('1. Input is used to collect value from: ')
ans = ( 'User','user')
if question in ans:
    score+=10
    print("That's right")
else:
    print("ooh no, That's wrong")
question=input('2. Variable are like container use to store: ')
ans = ( 'Data','data')
if question in ans:
    score+=10
    print("That's right")
else:
    print("ooh no, Olodo ni ee")
question=input('3. The basic structural and functional unit of all living organism is: ')
ans = ( 'Cell','cell')
if question in ans:
    score+=10
    print("That's right")
else:
    print("ooh no, Olodo ni ee")
question=input('4. An electronic machine devices that processes data and stores information is: ')
ans = ( 'Computer','computer')
if question in ans:
    score+=10
    print("That's right")
else:
    print("ooh no, Olodo ni ee")
question=input('5. The capital of Nigeria is: ')
ans = ( 'Abuja','abuja')
if question in ans:
    score+=10
    print("That's right")
else:
    print("ooh no, Olodo ni ee")
question=input('6. The creator that created all things in a creative ways is: ')
ans = ( 'God', 'GOD')
if question in ans:
    score+=10
    print("That's right")
else:
    print("ooh no, Olodo ni ee")
question=input('7. The place where we learn to read and write is called: ')
ans = ( 'School','school')
if question in ans:
    score+=10
    print("That's right")
else:
    print("ooh no, Olodo ni ee")
question=input('8. what is the smallest unit of matter: ')
ans = ( 'Atom','atom')
if question in ans:
    score+=10
    print("That's right")
else:
    print("ooh no, Olodo ni ee")
question=input('9. Anything that has mass,weight and occupies space is called: ')
ans = ( 'Matter','matter')
if question in ans:
    score+=10
    print("That's right")
else:
    print("ooh no, Olodo ni ee")
question=input('10. The groups of two or more atoms bonded together by chemical bonds is called: ')
ans = ( 'Molecules','molecules')
if question in ans:
    score+=10
    print("That's right")
else:
    print("ooh no, Olodo ni ee")
print('Total',score)



















