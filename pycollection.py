# """

# """

list_of_studt2=list(['kiki','bolu',['titi','ope','ayo']])
list_of_studt3=list(['kiki','bolu',['titi','ope','ayo'],'kemi','jola'])
list_of_item=['1',3j, 6.8, True, ['taiwo','temi']]
list_of_studt4=[['kiki','bolu','tope'],['fola','grace',],'Temi']


# print(type(list_of_item))
# print(type(list_of_studt2))
# print(type(list_of_studt4))
# print(type(list_of_studt3))
# print(len(list_of_item))
# print(len(list_of_studt2))
# print(len(list_of_studt3))
# print(len(list_of_studt4))
# print(list_of_studt3[2])
# print(list_of_studt3[2][2])
# print(list_of_studt4[0][1])
# print(list_of_studt4[1][0])
# print(list_of_studt4[0][1], '\n',list_of_studt4[1][0])
# print(list_of_studt3[:-1])
# print(list_of_studt3[-3:-1])
# print(list_of_studt3[::-2])
# print(list_of_studt3[:-2])

# list_of_studt3.reverse()
# print('reversing all the names: ',list_of_studt3)
# list_of_studt4.append('Temi')
# list_of_studt4.append('Taiwo')
# print('appending a name: ',list_of_studt4)




# class work
# Declare an empty list get 5 student name and age, store them in a varible and display the content of the variable in your teminal
# solution

a = [1, 2, 3]
b = a
b.append(4)
print(a)

# list_student=[]
# for each in range(0,5):
    
#     age_name=input[('enter your name: '), input('enter your age: ')]
#     list_student.append(age_name)
#     print(list_student)
























# list_of_studt=[]

# for each in range(0,3):
#     name=input('Enter your name: ')
#     age=input('Enter your age: ')
#     age_name= name,age
#     list_of_studt.append(age_name)
#     print(list_of_studt)

# for each in range(0,3):
#     age_name=input[('Enter your name: '),input('Enter your age: ')]
#     list_of_studt.append(age_name)
#     print(list_of_studt)


# list_of_studt5=[["Aliu","Habeeb","Fathima"],["Toheeb","Sodiq"]]
# list_of_studt4.extend(list_of_studt5)
# print(list_of_studt4)
# list_of_studt4.insert(2,'Habeebu')
# print(list_of_studt4)

# list_of_studt4.remove('Temi')
# list_of_studt4.pop(1)
# list_of_studt4.pop()
# print(list_of_studt4)


# for list of srting/chars

# lst1=[]
# lst1=[int(item) for item in input("Enter the list item : ").split()]
# print(lst1)



# name='tolu titt'
# print(name.split())












# How to declare a tuples
# fruits=('mango','pawpaw')
# fruits2=tuple(('mango','pawpaw','banana'))
# fruits3=('mango','pawpaw','mango','pawpaw',3j,('temi','dara','taiwo','tk'),['cumcumber','banana'],{1,2,3})
# print(type(fruits2))
# print(len(fruits2))
# print(len(fruits3))
# print(fruits3[3])
# print(fruits2[::1])
# print('index 5:',fruits3[::2])
# print('findings',fruits3[3])
# print('\n index 5:',fruits3[5][0],'\n')

# for name in fruits3[5]:
#     print(name)

# unpacking
# employee=(('Taiwo','taiwo123@gmail.com','liegeman','Male'),('Dara','daradud@gmail.com','doughtboy','Male'),('Temi','iyagbgbo@gmail.com','iyagbogbo','FEmale'))

# employee1,employee2,employee3=employee
# print(employee1)

# print(employee1[0],employee2[0],employee3[0])

# for name, email, username, gender in employee:
#     # print(name)
#     print("\n name of all employee: ",name,"\n")
#     print("\n email of all employee: ",email,"\n")
#     print("\n username of all employee: ",username,"\n")
#     print("\n gender of all employee: ",gender,"\n")
    
    
#     x=0
#     for _,email,_,_, in employee:
#          print("\n name of all employee: ",name,"\n")
#     print("\n email of all employee: ",email,"\n")
#     print("\n username of all employee: ",username,"\n")
#     print("\n gender of all employee: ",gender,"\n")
    
    
    
    
    # SET
    # python set is an ordered collection of data types that is iterable, mutable, and has no duplicable elements.
    
# set1={1, 2, 3, 4}
# set2=set((8 ,4, 3, 9))
# # print(type(set1))
# # print(type(set2))
# set1.add(8)
# set1.update((12, 14, 15))
# set1.remove(15)
# set3=set1.copy()
# set1.add(10)
# print(set3)
# print(set3)
# set1.union(set2)
# set1.intersection(set2)
# set1.difference(set2)
# print(set1)
# set3=set1.difference(set2)
# print(set3)
# electronics.

# electronics={'laptop':'Lenovo','phone':'Nokia', 'mifi':'MTN'}
# electronics2=dict([(12, 'hp'),(13, 'del')])
# electronics=dict(fruit1='mango', fruit2='orange')
# print(type(electronics))
# print(type(electronics2))
# print(type(electronics2[1]))
# print(electronics2)
# print(len(electronics2))
# print(len(electronics))
# print(electronics2.key())
# print(electronics2.item())
# print(electronics2.values())
# print(electronics2['Lenovo'])

# electronic.update(dict(year=2021, color='white'))
# electronic.update(dict(year=2024, color='blue'))
# electronic.update(dict(Laptop='Mac book Pro'))
# electronics.pop("Phone")
# electronics.popitem()
# del electronics['mifi']
# print(electronics)
# print(type(electronics2))
# print(type(electronics2))
