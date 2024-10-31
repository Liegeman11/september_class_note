


for i in range(1,4):
    try:
        rand_num=int(input('Enter a number: '))
        print(f'the num is {rand_num}')
    except ValueError:
        print('enter an integer')
    
    
num=[1, 2, 3]
try:
    print('second element = %d' %(num[3]))
    print('fourth element = %d' %(num[2]))
    
except IndexError:
    print('index out of range')
finally:
    print('program completed')