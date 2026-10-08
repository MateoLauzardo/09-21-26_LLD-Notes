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


#1.) No dependencies first (enums, helpers like Engine). (✅)
#2.) Then the parent / base class (Vehicle). (✅)
#3.) Then the children (Car, Aircraft). (✅)
#4.) Then the most complex class last (multiple inheritance like FlyingCar).


#! Step 2: Parent (vechile)

# Vehicle
# __init__(name, fuel, horsepower)
# start()
# describe()
# move() (abstract)

#! Step 3: Children (car, aircraft)

# Car
# __init__(wheels=4, **kwargs)
# describe()
# move()

# Aircraft
# __init__(max_altitude, **kwargs)
# describe()
# move()

#! Step 4: Most complex (FlyingCar)

# FlyingCar
# __init__(**kwargs)
# toggle_mode()
# move()


# -------------------------------------------------------------------


#TODO - review this stuff 
# super needs to be reviewed 
# kwargssd 



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
        return round(hp *0.7457, 1)

#2.) parent
class Vehicle(ABC):
    def __init__(self, name:str, fuel, horsepower:int):
        self.name = name 
        self.fuel = fuel
        #! composition 
        self.engine = Engine(horsepower)

    def start(self):
        self.engine.start()
        return f"{self.name} engine ({self.engine.horsepower}hp) started."

    def describe(self):
        return f"{self.name} [{self.fuel.name}]"

    @abstractmethod
    def move(self):
        return
    
    

class Car(Vehicle):
    #! kwargs allows you to pass any number of NEW parameters attirbutes 
    def __init__(self, wheels=4, **kwargs):
        super().__init__(**kwargs)
        self.wheels = wheels
        
        
    def describe(self):
        return f"{super().describe()} | wheels: {self.wheels}"


    def move(self):
        return f"{self.name} is moving"



class Aircraft(Vehicle):
    def __init__(self, max_altitude, **kwargs):
        self.max_altitude = max_altitude
        super().__init__(**kwargs)


    def describe(self):
        return f"{super().describe()} | max altitude: {self.max_altitude}"


    def move(self):
        return f"{self.name} is flying"
    


#3.) multi inheritence
class FlyingCar(Car, Aircraft):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # flag
        self.mode_value = "road"
    
    
    def mode(self):
        return f"{self.mode_value}"
        

    def toggle_mode(self):
        if self.mode_value == "road":
            self.mode_value = "air"
            return self.mode()
        else:
            self.mode_value = "road"
            return self.mode()


    def move(self):
        if self.mode_value == "road":
            return f"{self.name} is moving"
        else:
            return f"{self.name} is flying"
    
    

# -------------------------------------------------------------------

    
# Example #1:
car = Car(name="Civic", fuel=FuelType.GAS, horsepower=150)
# print(car.describe())
# Expected Output: "Civic [GAS] | wheels: 4"

fc = FlyingCar(name="SkyRider", fuel=FuelType.HYBRID, horsepower=300, max_altitude=10000)
print(fc.move())        #  →  "SkyRider is moving"      (same as Car.move)
print(fc.toggle_mode()) #      fc.mode        →  "air"

