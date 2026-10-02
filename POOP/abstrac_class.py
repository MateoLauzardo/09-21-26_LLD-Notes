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


# abstract class -> class that has abstract method. What this does it basically allows you to call this SAME class in other classes 
# you can pass in parma
class Choice(ABC):
    
    @abstractmethod
    def decision(self):
        pass
        

class paper(Choice):
    
    def decision(self, finger: int): #TODO - find out answer to this question 
        print("paper") 

class rock(Choice):
    
    def decision(self):
        print("rock")


class scizzor(Choice):
    
    def decision(self):
        return super().decision()
    
    
    
#____________________________________________




# parent / super function
class Animal():
    
    def __init__(self, name:str):
        self.name = name 
    
    def eat(self):
        print(f"the {self.name} eat!")
    
    def sleep(self):
        print(f"the {self.name} is sleeping")
    
# child
class Cat(Animal):
    
    def __init__(self, name: str, color: str):
        super().__init__(name) # animal class handels the name / super function
        self.color = color 
    
    def speak(self):
        print("meow")
        
    def cat_color(self):
        print(f"the {self.name}s color is {self.color}")
    
    
    #NOTE: calling other class methind in FUNCTIONS based off inheritence 
    def night_routine(self):
        self.eat()
        self.sleep()
        self.speak()
        
    

cat = Cat("cat", "yellow") # cat doesnt have its own constructor so borrows Animals 
cat.night_routine()
    
    
animal = Animal("dog")
# animal.eat()
# animal.sleep()
# animal.speak()  #NOTE: you see this wont work becuase that class is only for Cat. When you call Cat it gets ALL of animals stuff + its own stuff 
    
    
# ____________________________________________


