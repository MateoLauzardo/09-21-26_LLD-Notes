# Composition means one class is built out of other objects, and those 
# objects are usually created right inside __init__ and stored as attributes.

# Composition -> is a design princible where comp[elx systems or objects
# are built by combining similar, simpler, reusable peices of code. 

# Examples: Car (object) and a car has a engine, wheels, and so on

# ------------------------------------------------------------------------------------

# #NOTE: PROBLEM 1


# # You create a floor by giving it a floor number and how many spots of each type.
# # The floor builds its own spots. You ask it for a free spot of a certain type,
# # mark that spot as occupied, and occupancy() shows how many spots are taken.
# from enum import Enum


# class VehicleType(Enum):
#     MOTORCYCLE = "motorcycle"
#     CAR = "car"
#     TRUCK = "truck"


# # this class is meant to create parking spot 
# class ParkingSpot:
#     def __init__(self, spot_id: str, vehicle_type: Enum):
#         self.spot_id = spot_id
#         self.vehicle_type = vehicle_type
#         self.occupied = False


# # this class is meant for creating parking floor 
# class ParkingFloor:

#     # EX: ParkingFloor(1, {VehicleType.CAR: 2, VehicleType.TRUCK: 1})
#     def __init__(self, number: int, spot_counts: dict):
#         self.number = number 
#         self.spot_counts = spot_counts

#         #ANCHOR Anything attached to self can be seen by every method of the class.
#         self._spots = []
        
#         #NOTE step1: loop through spot count, so we get car type and spots / Dict: # {VehicleType.CAR: 2, VehicleType.TRUCK: 1}
#         for vech_type, number_of_spots in spot_counts.items():
            
#             for x in range(1, number_of_spots + 1):
            
#                 park_spout = ParkingSpot(f"{number}-{vech_type.name}-{x}", vech_type)

                
#                 #NOTE: Spots array is going to hold these values 
#                 # 1-CAR-1 VehicleType.CAR False
#                 # 1-CAR-2 VehicleType.CAR False
#                 # 1-TRUCK-1 VehicleType.TRUCK False
#                 self._spots.append(park_spout)

            
        
        

#     # VehicleType.CAR -> its checking if CAR has an avaliable spots which returns the first empty spot that fits or `None`
#     def find_available_spot(self, vehicle_type:Enum):
        
#         # loop through _spots to see if we have CAR avaliable 
#         # spot is just an object of parking spot
#         for spot in self._spots:
            
#             if spot.vehicle_type == vehicle_type:
                
#                 # if these is a spot 
#                 if spot.occupied == False:
#                     # return ParkingSpot object -> "spot" 
#                     return spot

#         # this is ur else 
#         return None     
        
            
        
#     # returning a string of how much there are vs occupied -> "1/3"
#     def occupancy(self):
        
#         total_length = len(self._spots)

#         occupied = 0 
        
#         # keeping count of how many spots are taken
#         for spot in self._spots:
            
#             if spot.occupied == True:
#                 occupied += 1
        
        
#         answer = f"{occupied}/{total_length}"
        
#         return answer 
        
        
        


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


# class Order:
#     def __init__(self, order_id: str):
#         self.order_id = order_id
#         self.method_calls = 0
#         self.hashmap = {} # {product: [qty, unit_price]} 

#     # keep track of how many times its being called -> pass down values from each time its called 
#     # hashmap -> {product: [qty, unit_price]} 
#     def add_line(self, product: str, qty: int, unit_price: float):
        
#         # every time its called increment method_calls
#         self.method_calls += 1
        
#         self.hashmap[product] = [qty, unit_price]
        
#         return self.hashmap
        
        
        
        
#     # pick up the string, loop through hashmap, remove it 
#     def remove_line(self, product: str):
        
        
        
#         # loop through hashmap -> {'widget': [2, 9.99], 'gadget': [1, 24.5]} 
#         for widget, values in list(self.hashmap.items()):
#             if widget == product:
#                 # remove from hashmap 
#                 del self.hashmap[widget]
                
                
                
#         return

        
        
#     # recieve unit_price for EACH object and x amount of items that r in said object and add them all up 
#     def total(self):
        
#         total = 0 
        
#         # loop through hashmap -> {'widget': [2, 9.99], 'gadget': [1, 24.5]} 
#         for widget, values in self.hashmap.items():
#             math = values[0] * values[1]
#             total += math
            
#         return round(total, 2)         
            
    


#     # (DONE) returns how many lines have been made aka how many times add_line has bee called 
#     def line_count(self):
        
#         return self.method_calls


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
        
        
            
        


# Example Usage:
c = Car(300) # passing in value 
e = c.get_engine() # e is now the instance of Engine (a whole other class )
print(e.start()) # vroom (300hp) -> (done)

#NOTE: we want to remove instance of class with this function 
c.dispose()
print(e.start())

# Example Output:
# vroom (300hp)
# RuntimeError: Engine has been disposed


# debug:
c = Car(300) # passing in value 
# e = c.get_engine() # literally retruning so e equals the reutrn value 
# print(e.start())

