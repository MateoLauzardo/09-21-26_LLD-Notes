
#!SECTION -> MULTI INHERITENCE 
#STUB - think of it as an object that needs to inherit both x and y (fishes are both predator and pray) 

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

#_______________________________________________________________________________________