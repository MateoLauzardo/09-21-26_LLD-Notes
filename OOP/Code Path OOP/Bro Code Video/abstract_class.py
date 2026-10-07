
#!SECTION -> ABSTRACT CLASSES (litterally 1 of the princelpesl of OOP) Think of it as "something apart that won't change,"






#___________________________________________________________________________________


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


#___________________________________________________________________________________


# abstract class -> class that has abstract method. What this does it basically allows you to call this SAME class in other classes 
# you can pass in parma


# NOTE: the reason for abstract is anything that calls itself choice NEEDS TO HAVE THE METHODS 
class Choice(ABC):
    
    @abstractmethod
    def decision(self):
        pass 
        

class paper(Choice):
    
    def decision(self): #NOTE: you never change the function into something new. the whole point of abstraction is a promise every Choice has decision(), and you call it like this."
        print("paper") 

class rock(Choice):
    
    def decision(self):
        print("rock")


class scizzor(Choice):
    
    def decision(self):
        return super().decision()
    
#___________________________________________________________________________________


    


