# composition -> a realtionship where one object contains the refrences to other
#                INDEPENDENT objects.Composed object directly owns its componenets, which cannot 
#                exist independently. 

# difference between aggregation and composition and aggreagtion classes can live on its own while comp can not.

#! Composition "owns-a" relationship / you create an object in the constructor 


# __________________________________________________________________

class Engine():
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel():
    def __init__(self, size):
        self.size = size 


# this is comp cuz we are creating the engine and wheel objects in another class. car owns engine and wheels
class Car():
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model 
        
        #! -> if we were to delte these objects they would sease to exist.
        self.engine = Engine(horse_power) #NOTE car owns an engine
        self.wheel = [] #NOTE car owns 4 wheels
        for wheel in range(4):
            self.wheel.append(Wheel(wheel_size))
        
        
    def display(self):
        return f"Your car is a {self.make}, its model is {self.model}, it has {self.engine.horse_power} hourse power and ur wheels size is: {self.wheel[0].size} inches."
    
        
car = Car(make="Honda", model="Civic2026", horse_power="500", wheel_size=18)
car2 = Car(make="Honda", model="Civic2015", horse_power="300", wheel_size=12)
print(car.display())
print(car2.display())