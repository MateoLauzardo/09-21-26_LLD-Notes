
#NOTE Question 1 (Encapsulation)

# Write a class BankAccount that stores an owner’s name 
# and a private balance (self.__balance). 
# The balance must not be changed directly from outside the class.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner 
        self.balance = balance

    def deposit(self, amount):
        
        if amount < 0:
            return False 
        else:
            self.balance += amount
            return True

    def withdraw(self, amount):
        
        total = self.balance - amount
        
        if total < 0:
            return False 
        else:
            self.balance = total
            return True

    def get_balance(self):
        
        return self.balance
    

acct = BankAccount("Ana", 100)
# print(acct.deposit(50))
# print(acct.withdraw(500))
# print(acct.deposit(-20))
# print(acct.get_balance())

# output:
# True
# False
# False
# 150


# -------------------------------------------------------------------

#NOTE Question 2 (Abstraction)

# Write an abstract class Shape using Python’s abc module.
# It declares two abstract methods, area() and perimeter(), 
# so Shape itself cannot be instantiated. 
# Then write two concrete subclasses:

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
    
    def __init__(self, length, width):
        self.length = length 
        self.width = width
        
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    
    def __init__(self, raidus):
        self.raidus = raidus
        
    def area(self):
        return math.pi * (math.pow(self.raidus, 2))
    
    def perimeter(self):
        return (2 * math.pi) * self.raidus


# usage:
r = Rectangle(3, 4)
c = Circle(1)
# print(r.area())
# print(r.perimeter())
# print(round(c.area(), 2))

try:
    s = Shape()
except TypeError:
    # print("Cannot instantiate Shape")
    pass
    
    
# example:
# 12
# 14
# 3.14
# Cannot instantiate Shape


# -------------------------------------------------------------------

#NOTE Question 3 (Inheritance)

# Write a class Employee with a name and a monthly salary. 
# Its method annual_pay() returns salary * 12.
# Then write a subclass Manager 
# that also takes a yearly bonus. 
# Manager must call the parent constructor with super()
# and override annual_pay() 
# so that it returns the parent’s annual pay plus the bonus.

class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    def annual_pay(self):
        return self.salary * 12 


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def annual_pay(self):
        return (self.salary * 12) + self.bonus 
    
e = Employee("Sam", 4000)
m = Manager("Lee", 5000, 10000)
# print(e.annual_pay())
# print(m.annual_pay())
# print(isinstance(m, Employee))

# example output:
# 48000
# 70000
# True


# -------------------------------------------------------------------

#NOTE Question 4 (Polymorphism)

# Write a base class Notifier with a method send(message) 
# that raises NotImplementedError. 
# Then write three subclasses that each override send():

# EmailNotifier returns "Email: <message>"
# SMSNotifier returns "SMS: <message>"
# PushNotifier returns "Push: <message>"

# Finally, write a function broadcast() 
# that takes a list of notifiers and a message, 
# and returns a list of the results of calling send() on each one. 
# broadcast() must not check the type of any notifier.


from abc import ABC, abstractmethod
import math


class Notifier(ABC):
    
    @abstractmethod
    def send(self, message):
        return
        

class EmailNotifier(Notifier):
    
    def send(self, message):
        self.message = message
        return f"Email: {self.message}"

class SMSNotifier(Notifier):
    
    def send(self, message):
        self.message = message
        return f"SMSNotifier: {self.message}"

class PushNotifier(Notifier):
   
   def send(self, message):
       self.message = message
       return f"Push: {self.message}"


# list of objects
def broadcast(notifiers, message):
    
    answer = [] 
    
    for x in notifiers:
        z = x.send(message)
        answer.append(z)
        
    return answer 


notifiers = [EmailNotifier(), SMSNotifier(), PushNotifier()]
# print(broadcast(notifiers, "Server down"))


# ['Email: Server down', 'SMS: Server down', 'Push: Server down']



# -------------------------------------------------------------------

#NOTE Question 5 (Composition)

# Write a class Engine that takes horsepower 
# and has a method start() that returns "Engine started".

# Then write a class Car that takes a model and horsepower. 
# The Car must create its own Engine inside its constructor 
# and store it as self.engine, 
# so the engine cannot exist without the car. 
# Car.start() returns the engine’s message followed by 
# ". <model> is ready."


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower 

    def start(self):
        return "Engine started"


class Car:
    def __init__(self, model, horsepower):
        self.model = model 
        self.engine = Engine(horsepower)


    def start(self):
        return f"{self.engine.start()}. {self.model} is ready"
    
    
car = Car("Civic", 158)
# print(car.start())
# print(car.engine.horsepower)

# output:
# Engine started. Civic is ready.
# 158


# -------------------------------------------------------------------

# Write a class Professor that takes a name. 
# Then write a class Department that takes a department name 
# and holds a list of professors.
# Professors are created outside the department 
# and passed in, so they keep existing after the department is deleted.

class Professor:
    def __init__(self, name):
        self.name = name 

class Department:
    def __init__(self, name):
        self.name = name 
        self.list_of_professors = [] 

    def add_professor(self, professor):
        self.list_of_professors.append(professor)

    def remove_professor(self, professor):
        self.list_of_professors.remove(professor)

    def professor_names(self):
        
        names = [] 
        
        for professors in self.list_of_professors:
            
            x = professors.name
            names.append(x)
            
        return names 
            
            
p1 = Professor("Dr. Kim")
p2 = Professor("Dr. Patel")
cs = Department("Computer Science")
print(cs.name)
cs.add_professor(p1)
cs.add_professor(p2)
print(cs.professor_names())
cs.remove_professor(p1)
print(cs.professor_names())
del cs
print(p1.name)

# output:
# ['Dr. Kim', 'Dr. Patel']
# ['Dr. Patel']
# Dr. Kim