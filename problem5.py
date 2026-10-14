# Write a class Engine that takes horsepower as a parameter and has a method start() that returns "Engine with <horsepower> HP started". 
# Then write a class Car that takes a make (string) and an engine (an Engine object).
# Car should not inherit from Engine; it should contain one. 
# Car.start() should return "<make>: " followed by whatever its engine’s start() returns.

class Engine():
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine with {self.horsepower} HP started"
    

class Car():
    # Engine -> instance of Engine, literally an object 
    def __init__(self, make, number):
        self.make = make 
        self.engine = Engine(number)
        
    
    def start(self):
        return f"{self.make}: {self.engine.start()}"
    



car = Car("Toyota", 300)
print(car.start())

# output: 
# Toyota: Engine with 300 HP started