"""
OOP
how to create a class 
what is class
what is object
Attribute
Initializing
instance
inheritance
methods
"""

class Animal:
    def sleep(self):
        print('The dog is sleeping')

# dog=Animal()
# print(dog.sleep())
# class Employee:
#     bonus=0.3
#     def __init__(self, name, location, salary):
#         self.name=name
#         self.location= location
#         self.salary= salary
#     def staff_detail(self):
#         detail=(f'my name is {self.name} and i am from {self.location}. my salary is {self.salary}')
#         return detail
#     def annual_bonus(self):
#         self.salary= self.salary * self.bonus
#         return self.salary
# emp1=Employee('shalom', 'lagos', '10000')
# emp2=Employee('joshua', 'niger', '5000')
# emp3=Employee('tesleem', 'oyo', '2000')

# emp1.name='shalom'
# emp1.location='lagos'
# emp1.salary='10000'

# emp2.name='joshua'
# emp2.location='niger'
# emp2.salary='5000'

# emp3.name='tesleem'
# emp3.location='oyo'
# emp3.salary='2000'

# print('for emp1 details: ', emp1.staff_detail())
# print()
# print('for emp2 details: ', emp2.staff_detail())
# print('for emp1 details: ', emp1.annual_bonus())
# print('for emp2 details: ', emp2.annual_bonus())
# print('for emp3 details: ', emp3.staff_detail())
# print('for emp3 details: ', emp3.annual_bonus())


# class StoreSale:
#     bonus =0.3
#     def __init__(self, name, price, date, quantity, sale_rep):
#         self.name = name
#         self.price = price 
#         self.date = date
#         self.quantity = quantity
#         self.sale_rep = sale_rep
        
#     def sale_report(self):
#         self.total_cost= int(self.price)* int(self.quantity[0])
#         report= (f'the product sold is {self.name} by {self.sale_rep}. The total price is {self.total_cost}')
#         return report
#     def give_bonus(self):
#         give_b=self.total_cost * self.bonus
#         actual_b=self.total_cost -give_b
#         return f'You have a bonus of {self.bonus} and the money you are paying is {actual_b}'        
        
        
# StoreSale1=StoreSale('milo', '1800', '2024/08/4', '2 role', 'Temi')
# StoreSale2=StoreSale('milk', '1400', '2024/08/4', '2 role','Taiwo')

# print(StoreSale1.name)
# print(StoreSale1.price)
# print(StoreSale2.name)
# print(StoreSale2.price)
# print(StoreSale2.sale_report())
# print(StoreSale2.give_bonus())

# class_work
class Person:
    def __init__(self, name, age):
        self.name= name
        self.age = age
    def talk(self):
        report=(f'My name is {self.name}. I am {self.age} years old.')
        return report
Person1=Person('Tayo','12')
print(Person1.talk())

class Person:
    def __init__(self, name, age):
        self.name= name
        self.age = age
    def talk(self):
        print(f'My name is {self.name}. I am {self.age} years old.')
Person1=Person('Tayo','12')
Person1.talk()
