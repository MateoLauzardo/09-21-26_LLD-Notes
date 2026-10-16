# Problem 1: Coffee Shop Orders
# Concepts: abstract class, enum, polymorphism, super(), static method, class method

# Design a beverage ordering system
# All drinks share a name and a size
# but each drink type calculates its own base price.
# The final cost is the base price times the size multiplier.

from enum import Enum 
from abc import ABC, abstractmethod


#___________________________________________________________________________________

#NOTE: class where values can NOT be edited or changed 
# ✅
class Size(Enum):
    SMALL = 1.0
    MEDIUM = 1.25 
    LARGE = 1.50
    


# ✅
class Beverage(ABC):
    def __init__(self, name, size):
        self.name = name 
        self.size = size 
    
    # ✅
    @abstractmethod
    def base_price(self):
        pass 
    
    # ✅
    def cost(self):
        #! self is the object that called the method 
        return self.base_price() * self.size.value
    
    
    # ✅
    def describe(self):
        # returns a string like "Medium Coffee: $5.00".
        return f"{(self.size.name).capitalize()} {self.name}: ${self.cost():.2f}" 
    
#___________________________________________________________________________________


class Coffee(Beverage):
    
    
    # ✅
    def __init__(self, size, shots=1):
        
        #! super method, parameters r for beverage cuz we are inhering from that class
        #! this is where Beverage gets self.name from and size 
        super().__init__("Coffee", size)
        
        self.shots = shots 
        
        if not Coffee.is_valid_shots(shots):
            raise ValueError("shots must be between 1 and 4")
         
       
        
    
    # ✅  
    def base_price(self):
        if self.shots > 1:
            return 3 + ((self.shots-1) * 0.50)
        else:
            return 3 
      
    
    # ✅
    @staticmethod
    def is_valid_shots(shots):
        # returns True only if shots is between 1 and 4        
        return shots >= 1 and shots <= 4 
    
    
    # ✅
    #NOTE: this method ISNT being used every single time only when you call method.
    #NOTE: this methods purpose is to create order from a string 
    @classmethod
    def from_order(cls, order:str):
        # builds a Coffee from a string like "small coffee 2".
        
        # "small coffee 2"
        split = order.split() # -> "small , coffee,   2"
        
        size = Size[split[0].upper()] 
        
        number_of_shots = int(split[2]) # 2 
        
        #! cls IS the class itself (Coffee). Calling cls(...) creates a new object of that class
        return cls(size, number_of_shots)
        
        
        
        
        
    

class Tea(Beverage):
    def __init__(self, size):
        self.size = size
        super().__init__("Tea", size)
        
        
    def base_price(self):
        return 2.50 
    


        

# Example #1:
# Input: c = Coffee(Size.MEDIUM, shots=3)
#        c.describe()
# Expected Output: "Medium Coffee: $5.00"


c = Coffee(Size.MEDIUM, shots=3)
# print(c.describe())

t = Tea(Size.MEDIUM)
# print(t.describe())


example = Coffee.from_order("small coffee 2")
print(example.describe())


#___________________________________________________________________________________
