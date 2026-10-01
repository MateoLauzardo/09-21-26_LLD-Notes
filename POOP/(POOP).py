

#!SECTION -> MULTI INHERITENCE 

# grandparent
class Animal():
    
    def __init__(self, name:str):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")


# parent
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")
        
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")
        

# child
class Rabbit(Prey):
    pass

class Fox(Predator):
    pass 

#NOTE: Multi Inheritence (inherit from more then one parent)
class Fish(Prey, Predator):
    pass


# creating objects 
# rabbit = Predator("Bugs")
# hawk = Prey("Tony")
# fish = Fish("Nemo")

# # testing 
# fish.eat()
# fish.sleep()
# fish.hunt()

#____________________________________________

#NOTE: Own Example 
# grand parent class 
# parent class 
# child class 

# grandparent
class Car():
    def __init__(self, name:str):
        self.name = name 
        
    def drive(self):
        print("drive")
        
    def stop(self): 
        print("stop")
        
# parent 
class Honda(Car):
    def honda_honk(self):
        print("HONDAHONK!")


class Ford(Car):
    def ford_honk(self):
        print("FORDHONK!")
        
        
# child
class Honda_2026(Honda):
    pass
    
class Ford_2026(Ford):
    pass

# multi inhertience
class Fusion_car(Honda, Ford):
    pass

# objects
honda = Honda_2026("honda_mateo")
ford = Ford_2026("ford_mateo")
fusion = Fusion_car("fusion_mateo")

# honda.honda_honk()
# ford.ford_honk()
# honda.drive()

# fusion.honda_honk()
# fusion.ford_honk()

#____________________________________________

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

#!SECTION -> super() function

#NOTE: this function is used in a child class to call methods
# from a parent class



#NOTE: super class (instead of having color and filled in each constructor which would add more lines of code, super class stores all values that you want to be reusable for other classes)

# parent
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
        
    def describe(self):
        print(f"it is {self.color} and its {self.filled} that its filled.")
    
        
# child
class Circle(Shape):
    def __init__(self, color:str, filled:bool, raidus:int):
        super().__init__(color, filled)
        self.raidus = raidus
    
    def describe(self):
        super().describe()
        print(f"its a circle with an area of {3.14 * self.raidus * self.raidus} cm^2")
        
        
class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width
        
    def describe(self):
        super().describe()
        print(f"its a square with an area of {self.width * self.width} cm^2")
        
class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height
        
    def describe(self):
        super().describe()
        print(f"its a Traingle with an area of {self.width * self.height / 2} cm^2")

# objects
circle = Circle("yellow", True, 5)
square = Square("red", False, 10)
triangle = Triangle("blue", True, 5, 10)



#NOTE: outputs
# print(circle.color)
# print(circle.raidus)
# print(f"the circles color is {circle.color}")

# circle.describe()
# square.describe()
# triangle.describe()

