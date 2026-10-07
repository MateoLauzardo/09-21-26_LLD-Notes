
#!SECTION -> super() function -> tell youself, what attibutes in constructor are being repeated over and over 




#___________________________________________________________________________________

# ps (instead of having color and filled in each constructor which would add more lines of code, super class stores all values
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

# outputs
# print(circle.color)
# print(circle.raidus)
# print(f"the circles color is {circle.color}")

# circle.describe()
# square.describe()
# triangle.describe()

#_______________________________________________________________________________________


#super function + inheritence: 
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
    
    def __init__(self, name: str, color: str, age:int):
        super().__init__(name) # animal class handels the name / super function
        self.color = color # this is not apart of the super class so we call these by itself 
        self.age = age # this is not apart of the super class so we call these by itself 
        
    
    def speak(self):
        print("meow")
        
    def cat_color(self):
        print(f"the {self.name}s color is {self.color}")
    
    
    #NOTE: calling other class methind in FUNCTIONS based off inheritence 
    def night_routine(self):
        self.eat()
        self.sleep()
        self.speak()
        
    

cat = Cat("cat", "yellow", 10) # cat doesnt have its own constructor so borrows Animals 
cat.night_routine()
cat.sleep()
    
    
animal = Animal("dog")
# animal.eat()
# animal.sleep()
# animal.speak()  #NOTE: you see this wont work becuase that class is only for Cat. When you call Cat it gets ALL of animals stuff + its own stuff 

#_______________________________________________________________________________________