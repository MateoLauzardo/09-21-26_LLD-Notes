# Polymorphism -> means to have many forms. "poly" means many

#                   Two ways to achieve are:
#                   1.) inheritence 
#                   2. Duck Typing 


from abc import ABC, abstractmethod

#NOTE: abstract class 
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    
    def __init__(self, raidus):
        self.raidus = raidus
    
    def area(self):
        return 3.14 * self.raidus ** 2
    
    def raidus_test(self):
        return self.raidus



class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height 
    
    #!SECTION this is the example of poly we r calling area() the same way on any of them without knowing which class you're dealing with, and each responds with its own version
    def area(self):
        return self.base * self.height * 0.5 

class Square(Shape):
    
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2


class Pizza(Circle):
    def __init__(self, topping: str, raidus: int):
        super().__init__(raidus)
        self.topping = topping



# shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]

# for shape in shapes: 
#     print(f"shape area is: {shape.area()}cm")
    
pizza = Pizza("pepperoni", 15)
print(pizza.topping) #the attribute
print(f"pizza area is: {pizza.area()}")  #literally the math from parent class )
print(f"testing method for raids: {pizza.raidus_test()}")