#!SECTION -> ABSTRACT CLASSES / METHODS 

from abc import ABC, abstractmethod

# inheriting from ABC -> 
#NOTE cant create a vechile object
#NOTE the methods will be inherited from children


# parent, ABC creates ABM that you dont ever want to be changed 
class Vechine(ABC):
    
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
# child, so you have to create child class to inherit and MUST call all methods 
class Car(Vechine):
    
    def go(self):
        print("u drive the car")
    
    def stop(self):
        print("u stop the car")


class Truck(Vechine):
    def go(self):
        print("u drive the Truck")
        
    def stop(self):
        print("u stop the Truck")


class Boat(Vechine):
    def go(self):
        print("u sail the boat")
        
    def stop(self):
        print("u anchor the boat")


# output:
# car = Car()
# car.go()
# car.stop()

# truck = Truck()
# truck.go()
# truck.stop()

# boat = Boat()
# boat.go()
# boat.stop()


#____________________________________________