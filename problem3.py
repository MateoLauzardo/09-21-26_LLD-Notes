# Concepts: abstract class, composition, enum, multiple inheritance, cooperative super(), polymorphism, static method

#! abstract class -> absolutely the same. Where you have the decorater and you have a function in a class that you are able to call in other classes, but can NOT change parameters 
#! composition -> "own-a" when you create object of other class in the constructor of another 
#! Enum -> pass in the parameter of class and you set values that DO NOT change / .name .value
#! multi inheritence -> class is an instace of two other classes
#! polymorphism -> means multiple times other classes have same method 
#! static method -> method in class anyone can call  

# Design a vehicle system where a FlyingCar inherits from both Car and Aircraft.

# The key challenge is making super() work correctly through Python's Method Resolution Order (MRO) 

# so every parent's __init__ and describe() runs exactly once.


#NOTE: 
# Build from no dependencies toward many dependencies.
# Make the parent work before the child.
# Use **kwargs with super() to keep multiple inheritance working.
# Get one example fully working before expanding.


# No dependencies first (enums, helpers like Engine).
# Then the parent / base class (Vehicle).
# Then the children (Car, Aircraft).
# Then the most complex class last (multiple inheritance like FlyingCar).


# -------------------------------------------------------------------

from abc import ABC, abstractmethod
from enum import Enum

#1. no dependencies
class FuelType(Enum):
    GAS = "gas"
    ELECTRIC = "electric"
    HYBRID = "hybrid"

#1. helpers 
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.running = False


    def start(self):
        self.running = True 
        
    @staticmethod
    def hp_to_kw(hp):
        return (hp *0.7457, 1)


class Vehicle(ABC):
    def __init__(self, name, fuel, horsepower):
        pass

    def start(self):
        pass

    def describe(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def __init__(self, wheels=4, **kwargs):
        pass

    def describe(self):
        pass

    def move(self):
        pass

class Aircraft(Vehicle):
    def __init__(self, max_altitude, **kwargs):
        pass

    def describe(self):
        pass

    def move(self):
        pass

class FlyingCar(Car, Aircraft):
    def __init__(self, **kwargs):
        pass

    def toggle_mode(self):
        pass

    def move(self):
        pass
    
    

# -------------------------------------------------------------------

    
# Example #1:
car = Car(name="Civic", fuel=FuelType.GAS, horsepower=150)
car.describe()
print(car)
# Expected Output: "Civic [GAS] | wheels: 4"