


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

#____________________________________________
