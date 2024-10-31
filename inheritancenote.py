# class Animal:
#     animal_type='mammals'
#     def __init__(self, name, breed):
#         self.name=name
#         self.breed=breed

#     def run(self):
#         print(f'{self.name} is running')
        
#     def eat(self):
#         print(f'{self.name} is eating')
        
# class Dog(Animal):
#     def __init__(self, name, breed, height):
#         super().__init__(name,breed)
#         self.height= height
#     def makesound(self):
#         return (f'{self.name} is barking')

# class Goat(Animal):
    
#     def __init__(self, name, breed, behavior):
#         super().__init__(name,breed)
#         self.behavior= behavior
#     def makesound(self):
#         return (f'{self.name} is bleating')

# dog1=Dog('stacey', 'rottweiler', '24')
# goat1=Goat('eran iya osogbo', 'west african dwarf', 'stubborn')

# print(dog1.animal_type)
# print(goat1.animal_type)
# # print(dog1.eat())
# dog1.eat()
# # print(goat1.eat())
# goat1.eat()
# print(dog1.makesound())
# print(goat1.makesound())
# # print(goat1.animal_type)



# class Vehicle:
#     Engine= 'one'
#     Brake= 'one'
    
    
#     def __init__(self,types, model, wheels, meansOfTransport, engine_type):
#         self.types=types
#         self.model=model
#         self.wheels=wheels
#         self.meansOfTransport=meansOfTransport
#         self.engine_type=engine_type
        
#     def mobility(self):
#         return (f'The {self.model}, a {self.wheels} wheels  {self.types}, is primarly used for {self.meansOfTransport} transportation. it has {Vehicle.Engine} engine of {self.engine_type} and {Vehicle.Brake} brake. ')
        
# class Car(Vehicle):
#     pass
# class Truck(Vehicle):
#     pass
# class Buses(Vehicle):
#     pass
# class Motorcycles(Vehicle):
#     pass
# class Bicycle(Vehicle):
#     pass
# class Train(Vehicle):
#     pass
# class Airplane(Vehicle):
#     pass
# class Ship(Vehicle):
#     pass
        
# my_Car=Car('car','Lexus lx600', 'Four', 'Road', 'V8')
# my_truck=Truck('truck','GMC Sierra 1500', 'eight', 'Road', 'V6')
# my_buses=Buses('Buses','Maxzda', 'Four', 'Road', 'V7')
# my_motorcycles=Motorcycles('motorcycle','boxer', 'two', 'Road', 'V2')
# my_bicycle=Bicycle('Bicycle','Lexus lx600', 'Four', 'two', 'V8')
# my_ship=Ship('ship','Lexus lx600', 'Four', 'water', 'V8')
# my_airplane=Airplane('airplane','Lexus lx600', 'Four', 'air', 'V8')
# my_train=Train('train','Lexus lx600', 'Four', 'Road', 'V8')
# print(my_Car.mobility())
# print(my_truck.mobility())
# print(my_buses.mobility())
# print(my_motorcycles.mobility())
# print(my_bicycle.mobility())
# print(my_ship.mobility())
# print(my_airplane.mobility())
# print(my_train.mobility())
    





# class Vehicle:
#     Engine = 'one'
#     Brake = 'one'
    
#     def __init__(self, types, model, wheels, meansOfTransport, engine_type):
#         self.types = types
#         self.model = model
#         self.wheels = wheels
#         self.meansOfTransport = meansOfTransport
#         self.engine_type = engine_type
        
#     def mobility(self):
#         return (f'The {self.model}, a {self.wheels}-wheeled {self.types}, is primarily used for {self.meansOfTransport} transportation. It has {Vehicle.Engine} engine of {self.engine_type} type and {Vehicle.Brake} brake.')

# class Car(Vehicle):
#     pass

# class Truck(Vehicle):
#     pass

# class Buses(Vehicle):
#     pass

# class Motorcycles(Vehicle):
#     pass

# class Bicycle(Vehicle):
#     pass

# class Train(Vehicle):
#     pass

# class Airplane(Vehicle):
#     pass

# class Ship(Vehicle):
#     pass

# my_Car = Car('car', 'Lexus LX600', 'Four', 'Road', 'V8')
# my_truck = Truck('truck', 'GMC Sierra 1500', 'Eight', 'Road', 'V6')
# my_buses = Buses('bus', 'Mazda', 'Four', 'Road', 'V7')
# my_motorcycles = Motorcycles('motorcycle', 'Boxer', 'Two', 'Road', 'V2')
# my_bicycle = Bicycle('bicycle', 'Trek FX 3', 'Two', 'Human-powered', 'None')
# my_ship = Ship('ship', 'Titanic', 'None', 'Water', 'Diesel')
# my_airplane = Airplane('airplane', 'Boeing 747', 'eighteen', 'Air', 'Jet Engine')
# my_train = Train('train', 'TGV', 'None', 'Rail', 'Electric')

# print(my_Car.mobility())
# print(my_truck.mobility())
# print(my_buses.mobility())
# print(my_motorcycles.mobility())
# print(my_bicycle.mobility())
# print(my_ship.mobility())
# print(my_airplane.mobility())
# print(my_train.mobility())



# class Vehicle:
#     Engine = 'one'
#     Brake = 'one'
    
#     def __init__(self, types, model, wheels, meansOfTransport, engine_type, purpose, park, reverse, speed, trafficator):
#         self.types = types
#         self.model = model
#         self.wheels = wheels
#         self.purpose = purpose
#         self.meansOfTransport = meansOfTransport
#         self.engine_type = engine_type
#         self.park=park
#         self.reverse=reverse
#         self.speed=speed
#         self.trafficator=trafficator
        
#     def mobility(self):
#         return (f'The {self.model}, a {self.wheels}-wheeled {self.types}, is primarily used for {self.meansOfTransport} transportation. It has {Vehicle.Engine} engine of {self.engine_type} type and {Vehicle.Brake} brake.')
        
# class Car(Vehicle):
#     def __init__(self,types, model, wheels, meansOfTransport, engine_type, purpose, capacity):
#         super().__init__(types, model, wheels, meansOfTransport, engine_type, purpose)
#         self.capacity = capacity
        
    
#     def detailed(self):
#         return (super().mobility() + f" It is typically {self.capacity} and designed for {self.purpose} transportation.")

# class Truck(Vehicle):
#     def __init__(self, model, wheels, meansOfTransport, engine_type, purpose, loads_capacity):
#         super().__init__('truck', model, wheels, meansOfTransport, engine_type, purpose)
#         self.loads_capacity = loads_capacity

#     def detailed(self):
#         return (super().mobility() + f" It has a cargo capacity of {self.loads_capacity} tons. it is typically designed for {self.purpose} transportation")

# class Buses(Vehicle):
#     def __init__(self, model, wheels, meansOfTransport, engine_type, purpose, passenger_capacity):
#         super().__init__('bus', model, wheels, meansOfTransport, engine_type, purpose)
#         self.passenger_capacity = passenger_capacity

#     def mobility(self):
#         return (super().mobility() + f" It can carry {self.passenger_capacity} passengers. it is typically designed for {self.purpose} transportation")

# class Motorcycles(Vehicle):
#     def __init__(self, model, wheels, meansOfTransport, engine_type, purpose, is_open):
#         super().__init__('motorcycle', model, wheels, meansOfTransport, engine_type, purpose)
#         self.is_open = is_open

#     def mobility(self):
#         return (super().mobility() + f" It is an {self.is_open} vehicle. it is typically designed to {self.purpose} more easily than larger vechile.")

# class Bicycle(Vehicle):
#     def __init__(self, model, wheels, meansOfTransport, purpose):
#         super().__init__('bicycle', model, wheels, meansOfTransport, 'None', purpose)

#     def mobility(self):
#         return (super().mobility() + f" It is human-powered and doesn't have an engine. it is typically designed for{self.purpose} and transpotation.")

# class Train(Vehicle):
#     def __init__(self, model, wheels, meansOfTransport, engine_type, purpose, rail_type):
#         super().__init__('train', model, wheels, meansOfTransport, engine_type, purpose)
#         self.rail_type = rail_type

#     def mobility(self):
#         return (super().mobility() + f" It runs on {self.rail_type} tracks.")

# class Airplane(Vehicle):
#     def __init__(self, model, wheels, meansOfTransport, engine_type, purpose, wingspan):
#         super().__init__('airplane', model, wheels, meansOfTransport, engine_type, purpose)
#         self.wingspan = wingspan

#     def mobility(self):
#         return (super().mobility() + f" It has a wingspan of {self.wingspan} meters. it is typically designed for {self.purpose} transportation")

# class Ship(Vehicle):
#     def __init__(self, model, wheels, meansOfTransport, engine_type, purpose, deck_size):
#         super().__init__('ship', model, wheels, meansOfTransport, engine_type, purpose)
#         self.deck_size = deck_size

#     def mobility(self):
#         return (super().mobility() + f" It has a deck size of {self.deck_size} square meters. it is typically designed for {self.purpose} transportation")

# my_Car = Car('car','Lexus LX600', 'Four', 'Road', 'V8','personal', 'smaller',)
# my_truck = Truck('GMC Sierra 1500', 'Eight', 'Road', 'V6', 'loads', 5)
# my_buses = Buses('Mazda', 'Four', 'Road', 'V7','public', 50)
# my_motorcycles = Motorcycles('Boxer', 'Two', 'Road', 'V2','navigate through tight spaces and traffic', 'open')
# my_bicycle = Bicycle('Trek FX 3', 'Two', 'Human-powered', 'sports')
# my_ship = Ship('Titanic', 'None', 'Water', 'Diesel','public', 1000)
# my_airplane = Airplane('Boeing 747', 'eighteen', 'Air','Jet Engine', 'public', 60)
# my_train = Train('TGV', 'None', 'Rail', 'Electric', 'public', 'high-speed')

# print(my_Car.mobility())
# # print(Car.mobility())
# print(my_truck.mobility())
# print(my_buses.mobility())
# print(my_motorcycles.mobility())
# print(my_bicycle.mobility())
# print(my_ship.mobility())
# print(my_airplane.mobility())
# print(my_train.mobility())


name= 'tolu'
color= 'red'
weight= '50kg'
age= 20
print(name, color, weight, age)
print(f'my name is {name}, i am putting on {color} grown. i am {age} years old with a weight of {weight}')


first_name=input('enter your first name: ')
last_name=input('Enter your last name: ')
location=input('Where is your location: ')
address=input('where do you live: ')
email=input('Enter your email address: ')
details={'first_name':first_name, 'last_name':last_name, 'location':location, 'address':address, 'email': email}
print(details)