class Vehicle:
    Engine = 'one'
    Brake = 'one'
    
    def __init__(self, types, model, wheels, meansOfTransport, engine_type):
        self.types = types
        self.model = model
        self.wheels = wheels
        self.meansOfTransport = meansOfTransport
        self.engine_type = engine_type
        
    def mobility(self):
        return (f'The {self.model}, a {self.wheels}-wheeled {self.types}, is primarily used for {self.meansOfTransport} transportation. It has {Vehicle.Engine} engine of {self.engine_type} type and {Vehicle.Brake} brake.')

class Car(Vehicle):
    def __init__(self, model, wheels, meansOfTransport, engine_type, trunk_capacity):
        super().__init__('car', model, wheels, meansOfTransport, engine_type)
        self.trunk_capacity = trunk_capacity
    
    def mobility(self):
        return (super().mobility() + f" It also has a trunk with {self.trunk_capacity} liters of capacity.")

class Truck(Vehicle):
    def __init__(self, model, wheels, meansOfTransport, engine_type, cargo_capacity):
        super().__init__('truck', model, wheels, meansOfTransport, engine_type)
        self.cargo_capacity = cargo_capacity

    def mobility(self):
        return (super().mobility() + f" It has a cargo capacity of {self.cargo_capacity} tons.")

class Buses(Vehicle):
    def __init__(self, model, wheels, meansOfTransport, engine_type, passenger_capacity):
        super().__init__('bus', model, wheels, meansOfTransport, engine_type)
        self.passenger_capacity = passenger_capacity

    def mobility(self):
        return (super().mobility() + f" It can carry {self.passenger_capacity} passengers.")

class Motorcycles(Vehicle):
    def __init__(self, model, wheels, meansOfTransport, engine_type, is_open):
        super().__init__('motorcycle', model, wheels, meansOfTransport, engine_type)
        self.is_open = is_open

    def mobility(self):
        return (super().mobility() + f" It is {'an open' if self.is_open else 'a closed'} vehicle.")

class Bicycle(Vehicle):
    def __init__(self, model, wheels, meansOfTransport):
        super().__init__('bicycle', model, wheels, meansOfTransport, 'None')

    def mobility(self):
        return (super().mobility() + " It is human-powered and doesn't have an engine.")

class Train(Vehicle):
    def __init__(self, model, wheels, meansOfTransport, engine_type, rail_type):
        super().__init__('train', model, wheels, meansOfTransport, engine_type)
        self.rail_type = rail_type

    def mobility(self):
        return (super().mobility() + f" It runs on {self.rail_type} tracks.")

class Airplane(Vehicle):
    def __init__(self, model, wheels, meansOfTransport, engine_type, wingspan):
        super().__init__('airplane', model, wheels, meansOfTransport, engine_type)
        self.wingspan = wingspan

    def mobility(self):
        return (super().mobility() + f" It has a wingspan of {self.wingspan} meters.")

class Ship(Vehicle):
    def __init__(self, model, wheels, meansOfTransport, engine_type, deck_size):
        super().__init__('ship', model, wheels, meansOfTransport, engine_type)
        self.deck_size = deck_size

    def mobility(self):
        return (super().mobility() + f" It has a deck size of {self.deck_size} square meters.")

my_Car = Car('Lexus LX600', 'Four', 'Road', 'V8', 500)
my_truck = Truck('GMC Sierra 1500', 'Eight', 'Road', 'V6', 5)
my_buses = Buses('Mazda', 'Four', 'Road', 'V7', 50)
my_motorcycles = Motorcycles('Boxer', 'Two', 'Road', 'V2', True)
my_bicycle = Bicycle('Trek FX 3', 'Two', 'Human-powered')
my_ship = Ship('Titanic', 'None', 'Water', 'Diesel', 1000)
my_airplane = Airplane('Boeing 747', 'eighteen', 'Air', 'Jet Engine', 60)
my_train = Train('TGV', 'None', 'Rail', 'Electric', 'high-speed')

print(my_Car.mobility())
print(my_truck.mobility())
print(my_buses.mobility())
print(my_motorcycles.mobility())
print(my_bicycle.mobility())
print(my_ship.mobility())
print(my_airplane.mobility())
print(my_train.mobility())
