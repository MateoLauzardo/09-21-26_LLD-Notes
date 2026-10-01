# #NOTE: PROBLEM 1

# # You create a floor by giving it a floor number and how many spots of each type.
# # The floor builds its own spots. You ask it for a free spot of a certain type,
# # mark that spot as occupied, and occupancy() shows how many spots are taken.
# from enum import Enum


class VehicleType(Enum):
    MOTORCYCLE = "motorcycle"
    CAR = "car"
    TRUCK = "truck"


# this class is meant to create parking spot 
class ParkingSpot:
    def __init__(self, spot_id: str, vehicle_type: Enum):
        self.spot_id = spot_id
        self.vehicle_type = vehicle_type
        self.occupied = False


# this class is meant for creating parking floor 
class ParkingFloor:

    # EX: ParkingFloor(1, {VehicleType.CAR: 2, VehicleType.TRUCK: 1})
    def __init__(self, number: int, spot_counts: dict):
        self.number = number 
        self.spot_counts = spot_counts

        #ANCHOR Anything attached to self can be seen by every method of the class.
        self._spots = []
        
        #NOTE step1: loop through spot count, so we get car type and spots / Dict: # {VehicleType.CAR: 2, VehicleType.TRUCK: 1}
        for vech_type, number_of_spots in spot_counts.items():
            
            for x in range(1, number_of_spots + 1):
            
                park_spout = ParkingSpot(f"{number}-{vech_type.name}-{x}", vech_type)

                
                #NOTE: Spots array is going to hold these values 
                # 1-CAR-1 VehicleType.CAR False
                # 1-CAR-2 VehicleType.CAR False
                # 1-TRUCK-1 VehicleType.TRUCK False
                self._spots.append(park_spout)

            
        
        

    # VehicleType.CAR -> its checking if CAR has an avaliable spots which returns the first empty spot that fits or `None`
    def find_available_spot(self, vehicle_type:Enum):
        
        # loop through _spots to see if we have CAR avaliable 
        # spot is just an object of parking spot
        for spot in self._spots:
            
            if spot.vehicle_type == vehicle_type:
                
                # if these is a spot 
                if spot.occupied == False:
                    # return ParkingSpot object -> "spot" 
                    return spot

        # this is ur else 
        return None     
        
            
        
    # returning a string of how much there are vs occupied -> "1/3"
    def occupancy(self):
        
        total_length = len(self._spots)

        occupied = 0 
        
        # keeping count of how many spots are taken
        for spot in self._spots:
            
            if spot.occupied == True:
                occupied += 1
        
        
        answer = f"{occupied}/{total_length}"
        
        return answer 
        
        
# # -----------------

# #NOTE: Example Usage:
# # passees in values to class Parking Floor
# floor = ParkingFloor(1, {VehicleType.CAR: 2, VehicleType.TRUCK: 1})
# # calls the object you create and finds avaliabke spots for the CAR constent
# spot = floor.find_available_spot(VehicleType.CAR)
# print(spot.spot_id)


# # spot is changing value 
# spot.occupied = True
# print(floor.find_available_spot(VehicleType.CAR).spot_id)


# print(floor.occupancy())


# Example Output:
# 1-CAR-1
# 1-CAR-2
# 1/3

# -----------------


# debugging 
# int = 2
# VehicleType.CAR.name 
# string = f"1-{VehicleType.CAR.name}-{int}"
# print(string)


# floor = ParkingFloor(1, {VehicleType.CAR: 2, VehicleType.TRUCK: 1})

# for spot in floor._spots:
#     print(spot.spot_id, spot.vehicle_type, spot.occupied)


# ------------------------------------------------------------------------------------


#NOTE: PROBLEM 2
# An order owns its line items. A line item has no meaning outside the order that
# created it, and deleting the order deletes them. 

# Implement `Order` so that callers CANNOT construct an `OrderLine` and hand it in - 

# the only way to add one is `add_line(product, qty, unit_price)`.

# Note: make the constraint real in code, not just a comment. Then write one


class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.method_calls = 0
        self.hashmap = {} # {product: [qty, unit_price]} 

    # keep track of how many times its being called -> pass down values from each time its called 
    # hashmap -> {product: [qty, unit_price]} 
    def add_line(self, product: str, qty: int, unit_price: float):
        
        # every time its called increment method_calls
        self.method_calls += 1
        
        self.hashmap[product] = [qty, unit_price]
        
        return self.hashmap
        
        
        
        
    # pick up the string, loop through hashmap, remove it 
    def remove_line(self, product: str):
        
        
        
        # loop through hashmap -> {'widget': [2, 9.99], 'gadget': [1, 24.5]} 
        for widget, values in list(self.hashmap.items()):
            if widget == product:
                # remove from hashmap 
                del self.hashmap[widget]
                
                
                
        return

        
        
    # recieve unit_price for EACH object and x amount of items that r in said object and add them all up 
    def total(self):
        
        total = 0 
        
        # loop through hashmap -> {'widget': [2, 9.99], 'gadget': [1, 24.5]} 
        for widget, values in self.hashmap.items():
            math = values[0] * values[1]
            total += math
            
        return round(total, 2)         
            
    


    # (DONE) returns how many lines have been made aka how many times add_line has bee called 
    def line_count(self):
        
        return self.method_calls


# # #NOTE: Example Usage:
# o = Order("O1") # creating instance of class 
# o.add_line("widget", 2, 9.99) # you call the add_line method
# o.add_line("gadget", 1, 24.50) # you call the add_line method
# print(o.line_count()) # should print out 2 (done)
# print(o.total()) # should print out 44.48 (done)
# o.remove_line("widget")
# print(o.total()) # should print out 24.5 

# # Example Output:
# # 2 
# # 44.48
# # 24.5


# #NOTE: debug code:
# # hashmap = {}
# # hashmap["key"] = 1 
# # print(hashmap) {'key': 1}

# print("DEBUGGING:", o.hashmap) # {'widget': [2, 9.99], 'gadget': [1, 24.5]} 


# ------------------------------------------------------------------------------------


# PROBLEM 3
# ---------
# The class below claims composition but leaks its part. Show the leak by
# reproducing the example below, 

# then rewrite `Car` so that discarding the car genuinely invalidates the engine.

# Note: Python will not cascade-delete for you. You must enforce composition
# semantics yourself. Implement `dispose()` so that any method call on a disposed
# engine raises a `RuntimeError`, and explain why exposing the part at all was the
# original mistake.


class Engine:
    def __init__(self, hp: int):
        self.hp = hp
        self.run = True 

    def start(self):
        
        if self.run == True: 
            return f"vroom ({self.hp}hp)"
        else:
            raise("RuntimeError: Engine has been disposed")

class Car:
    def __init__(self, hp: int): 
        # varaible "engine" equals passing the value into another class 
        self.engine = Engine(hp)

    def get_engine(self):
        # e is equal to what is being returned -> this is returning the literaly object 
        # instance for the other Engine class, so if you want to call any methods u need this 
        return self.engine 

    
    
    #NOTE: we want to remove instance of class with this function 
    def dispose(self):
        
        self.engine.run = False 
        
        
            

# # Example Usage:
# c = Car(300) # passing in value 
# e = c.get_engine() # e is now the instance of Engine (a whole other class )
# print(e.start()) # vroom (300hp) -> (done)

# #NOTE: we want to remove instance of class with this function 
# c.dispose()
# print(e.start())

# Example Output:
# vroom (300hp)
# RuntimeError: Engine has been disposed


# debug:
# c = Car(300) # passing in value 
# e = c.get_engine() # literally retruning so e equals the reutrn value 
# print(e.start())



# ------------------------------------------------------------------------------------

# PROBLEM 4
# ---------

#NOTE: Inheritance ("Is-A"): A child class derives from a parent class, automatically gaining its 
# methods and properties. Example: A Dog is an Animal.Composition ("Has-A"): An object is built by containing or referencing other
# independent objects. Example: A Car has an Engine and has 


# The hierarchy below doubles in size every time a new ability is added. 

# Rewrite it using composition so that a bird HOLDS its behaviors instead of inheriting
# them, and show a bird acquiring the ability to fly at runtime - something the
# inheritance version cannot do.

# Note: name the specific problem the inheritance version has, and count how many
# classes you would need for five independent abilities under each approach.


# class Bird: ...
# class FlyingBird(Bird): ...
# class SwimmingBird(Bird): ...
# class FlyingSwimmingBird(FlyingBird, SwimmingBird): ...


class CanSwim:
    pass
        
    

class CanFly:
    pass 
            

# we are doing compostion "has-a" so birds has a ability to swim, and fly 
class Bird:
    
    def __init__(self, name:str, fly_behavior=None, swim_behavior=None):
        self.name = name 
        self.fly_behavior = fly_behavior
        self.swim_behavior = swim_behavior
    
       
    # return a string 
    def describe(self):
        
        # output: # Duck: flies, swims
        
        array = [] 
                        
        if self.fly_behavior:
            array.append("flies")
        
        if self.swim_behavior:
            array.append("swims")
        
        join = (", ".join(array))
        
        describe = f"{self.name}: {join}"
        
        return describe


# # Example Usage:
# penguin = Bird("Penguin", swim_behavior=CanSwim())
# print(penguin.describe())
# duck = Bird("Duck", fly_behavior=CanFly(), swim_behavior=CanSwim())
# print(duck.describe())
# penguin.fly_behavior = CanFly()
# print(penguin.describe())


# Example Output:
# Penguin: swims
# Duck: flies, swims
# Penguin: flies, swims


# ------------------------------------------------------------------------------------

# PROBLEM 5
# ---------
# Implement a `Character` composed of an optional `Weapon`, `Armor`, and a list of
# `Ability` objects, all created and owned by the character's factory method `create()`. 

# Write `attack()`, which returns total damage, 
# return `equip()`, which swaps a weapon and destroys the old one.

# Note: the old weapon must be unusable after the swap. State whether the
# character's abilities are composition or aggregation under YOUR design, and
# defend the choice - both answers are defensible, but only with a reason.
# Evaluate the time and space complexity of `attack()`. Define your variables and
# provide a rationale for why you believe your solution has the stated time and
# space complexity.


class Weapon:
    def __init__(self, name:str, damage:int):
        self.name = name 
        self._damage = damage
        self.destroyed = False
        
        
        
    @property
    def damage(self):
        if self.destroyed:
            raise RuntimeError(f"Weapon {self.name} has been destroyed")
        return self._damage
   
                     
        
        
class Ability:
    def __init__(self, name:str, bonus:int):
        self.name = name 
        self.bonus = bonus



class Character:
    def __init__(self, name, weapon, ability):
        self.name = name 
        self.weapon = weapon
        self.ability = ability
        
        
    # hero = Character.create("Hero", ("sword", 10), [("rage", 5), ("focus", 2)])
    # decorator 
    @classmethod
    def create(cls, name:str, weapon_spec:tuple, ability_specs:list):
        
        
        ability_list = [] #NOTE -> going to pass into cls (just 2 objects being created) / [1. finished_ability, 2. finished_ability]
        
        
        #1.) break down ability -> ("rage", 5), ("focus", 2)]
        for ability in ability_specs:
            # unpack in two varaiables 
            ability_tool, ability_damage = ability
            
            # create object for ability 
            finished_ability = Ability(ability_tool,ability_damage)
            
            # add to list -> []
            ability_list.append(finished_ability)
            
            
        
        #2.) break down weapon -> ("sword", 10)
        weapon_tool, weapon_damage = weapon_spec
        weapon = Weapon(weapon_tool, weapon_damage) #NOTE -> goiong to pass into cls (just 1 object created for weapon)

        
    
        #3.) #ANCHOR -> CLS savees these values to the INIT vales 
        return cls(name, weapon, ability_list)


    # eqip weapon, and attatch damage / hero.equip(("axe", 15))
    def equip(self, sepcs:tuple):
        
        # setting value to True 
        self.weapon.destroyed = True
        
        # replace whats equiped 
        weapon, damage = sepcs
            
        # you set this variable from INIT equal to object 
        self.weapon = Weapon(weapon, damage)
        
        
        
    #grabs what weapon point, rage points, and focus points 
    def attack(self):
        
        total_damage = 0 
        
        total_damage += self.weapon.damage #NOTE -> your able to do .damage cuz self.weapon varialbe is set equaul to object 
        
        for ability in self.ability:
            total_damage += ability.bonus 
            
            
        return total_damage
            
        
# Example Usage:
# hero = Character.create("Hero", ("sword", 10), [("rage", 5), ("focus", 2)])
# print(hero.attack())
# old = hero.weapon
# hero.equip(("axe", 15))
# print(hero.attack())

# try:
#     print(old.damage)
# except RuntimeError as e:
#     print(f"RuntimeError: {e}")


# Example Output:
# 17
# 22
# RuntimeError: Weapon sword has been destroyed


# ------------------------------------------------------------------------------------

# PROBLEM 6

#NOTE: Association -> classes interact temporarily or hold references to each other, but they have completely independent lifecycles. 

# Example of Association 
class Teacher:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name):
        self.name = name
    
    # Association established through a method argument
    def attend_class(self, teacher):
        print(f"Student {self.name} is learning from Teacher {teacher.name}.")

# Both objects exist entirely on their own
# t = Teacher("Mr. Smith")
# s = Student("Alice")
# s.attend_class(t) 

# ----------------------------------------------------------------------------

#NOTE: Aggregation -> ("has-a") You DONT call the class within the INIT method, you just make a parameter and than CALL the class outside of everything 

# Example of Aggreagation 
class Professor:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name, professor):
        self.dept_name = dept_name
        self.professor = professor  # Stores a reference to an outside object

# 1. Create the professor independently
# prof = Professor("Dr. Jones")
# # 2. Pass the professor into the department
# math_dept = Department("Mathematics", prof)
# # 3. If we delete the department, the professor still exists
# del math_dept
# print(prof.name)  # Output: Dr. Jones (Still lives!)

# ----------------------------------------------------------------------------

# Classify each relationship below as composition, aggregation, or association,
# and write a one-line justification for each using the lifetime test. Then
# implement the two you marked composition, proving in your example usage that the
# parts do not survive the whole.

#NOTE: two of these five are genuinely debatable. Identify which two and say what
# additional requirement would settle each one.

# a) ParkingLot  -> ParkingFloor         (Compostion) - ("Part-Of")
# b) ParkingFloor -> ParkingSpot         (Composition) - ("Part-Of")

# c) ParkingSpot -> Vehicle              (Association)

# d) Ticket      -> ParkingSpot          (Association) -> the lack of any whole-part relationship: the vehicle isn't a part of the spot, just temporarily connected to it.
 
# e) ParkingLot  -> Attendant            (Aggregation) - ("has-a")

# Example Usage:
# Write your own demonstration for the two composition relationships.




# the ID, and if its open
class ParkingSpot:
    def __init__(self, ID:int):
        self.ID = ID
        self.taken = False 
        
        
        
    def park(self):
        if self.taken == False:
            self.taken = True
            
        else:
            print("spot is already taken")
    

    def leave(self):
        
        if self.taken == True:
            self.taken = False
        
        else:
            print("youre not parked")





# its number + needs the spots itself (object), 
class ParkingFloor:
    def __init__(self, parkingFloorNumber:int, capacity:int):
        self.parkingFloorNumber = parkingFloorNumber
        self.capacity = capacity
        
        self.list_of_spots = []
        
        # we need to create multiple parking spot objects by looping through range of capicty and each time making an object and passing in ID 
        for spot in range(1, capacity + 1):
            # created an objectof parkingspot and we are passing in the value 1-(capacity/maxnumber of spots)
            parkingspot = ParkingSpot(spot)
            self.list_of_spots.append(parkingspot)
            
                        
    
    #checks how many parking spots are left x/x
    def how_many_spots_left(self):

        
        number_of_taken_spots = 0 
        
        # count how many are taken
        for spot in self.list_of_spots:
            if spot.taken == True:
                number_of_taken_spots += 1
                
            
        spots_left = self.capacity - number_of_taken_spots
        
        
        return spots_left
            
            
    
    
# needs to contain the floor itself (object)
class ParkingLot:
    def __init__(self, floor: list):
        
        #ANCHOR - we do this so we have objects of each instance so we can LOOP through it below and use for methods like total open      
        self.floors = [] 
        
       # [60,60,60,50,50]
        for parkingFloorNumber, capacity in enumerate(floor, start = 1):
            self.floors.append(ParkingFloor(parkingFloorNumber, capacity))
            
        
    def total_open_spots(self):
    
        # need to call total open slots function, make a variable to add each answer together and return it 
        total_variable = 0 
        
        for floor in self.floors:
            total_variable += floor.how_many_spots_left()
            
        return total_variable
        
    
            
# a list of the capacity of each floor, floors represented by indexs 
lot = ParkingLot([60, 60, 60, 50, 50])

print("Open at start:", lot.total_open_spots())            # expect 280

# park 2 cars on floor 1, 1 car on floor 4
lot.floors[0].list_of_spots[0].park() # goes to index 0, which is an object of parking floor which has access to list of spots so index 0 
lot.floors[0].list_of_spots[1].park()
lot.floors[3].list_of_spots[0].park()

print("Floor 1 open:", lot.floors[0].how_many_spots_left())  # expect 58
print("Floor 4 open:", lot.floors[3].how_many_spots_left())  # expect 49
print("Total open:", lot.total_open_spots())                 # expect 277

# edge cases
lot.floors[0].list_of_spots[0].park()    # expect "already taken" message
lot.floors[0].list_of_spots[5].leave()   # expect "not parked" message



 
# Example Output:
# Your demonstration should print evidence that the part is
# unreachable or unusable once the whole is gone.
