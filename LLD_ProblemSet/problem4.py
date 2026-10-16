# Problem 1: Inheritance and super()

# Write a class Animal that takes a name and a sound as parameters, with a method speak() that returns the string "<name> says <sound>".
# Then write a class Dog that inherits from Animal. 
# Dog is created with only a name and a breed. It must use super().__init__() to set the name and always pass "Woof" as the sound.
# Add a method describe() to Dog that returns "<name> is a <breed>".

class Animal():
    def __init__(self, name, sound):
        self.name = name 
        self.sound = sound  
    
    def speak(self):
        return f"{self.name} says {self.sound}"
    
# inheritence. 
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof") 
        self.breed = breed 
    
    def describe(self):
        return f"{self.name} is a {self.breed}"
    
    
 
dog = Dog("Rex", "Labrador")
# print(dog.speak())
# print(dog.describe())

#example output: 
# Rex says Woof
# Rex is a Labrador


# -----------------------------------------------------------------------------------------

# Problem 2: Abstraction

# Using the abc module, write an abstract class Shape with two abstract methods: area() and perimeter(). 
# Then write two concrete classes, Rectangle(width, height) and Circle(radius), that implement both methods (use math.pi for circles). 
# Finally, write a function total_area(shapes) that takes a list of shapes and returns the sum of their areas rounded to 2 decimal places. 
# Trying to create a Shape directly should raise a TypeError.

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass 
    
    @abstractmethod
    def perimeter(self):
        pass 

    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width 
        self.height = height 
    
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
       
        

class Circle(Shape):
    def __init__(self, raidus):
        self.raidus = raidus 
        
        
    def area(self):
        return math.pi * (math.pow(self.raidus, 2))
        
    def perimeter(self):
        return 2 * math.pi * self.raidus
    


def total_area(shapes:list):
    
    total = 0 
    
    for shape in shapes:
        total += shape.area()
        
    return total 
        


r = Rectangle(3, 4)
c = Circle(1)
# print(r.area(), r.perimeter())
# print(c.area(), c.perimeter())
# print(total_area([r, c]))


# example output: 
# 12 14
# 15.14


# -----------------------------------------------------------------------------------------


# Problem 3: Polymorphism

# Write a base class Notification with a method send(message) that raises NotImplementedError.
# Then write two subclasses: EmailNotification(email) whose send(message) returns "Email to <email>: <message>", 
# and SMSNotification(phone) whose send(message) returns "SMS to <phone>: <message>". 
# Write a function broadcast(notifications, message) that calls send() on every notification and returns a list of the results. 
# The function should not check the type of any object; it should rely on polymorphism.

from abc import ABC, abstractmethod

class Notification(ABC):
    
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    
    def __init__(self, email):
        self.email = email 
    
    def send(self, message):
        return f"Email to {self.email}: {message}"
        


class SMSNotification(Notification):
    
    def __init__(self, phoneNumber):
        self.phoneNumber = phoneNumber
    
    def send(self, message):
        return f"SMS to {self.phoneNumber}: {message}"



def broadcast(notifications, message):
    
  
    answer = []
    
    for x in notifications:
        
        answer.append(x.send(message))
    
    return answer 
    
    # loop through notifcationmms 


# notifcations -> list of objects 
notifications = [EmailNotification("ana@mail.com"), SMSNotification("555-1234")]
print(broadcast(notifications, "Server down"))

#example output:
# ['Email to ana@mail.com: Server down', 'SMS to 555-1234: Server down']



# -----------------------------------------------------------------------------------------