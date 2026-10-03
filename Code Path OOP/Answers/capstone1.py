# PROBLEM 1  (Enum)
# ---------
# A traffic light cycles RED -> GREEN -> YELLOW -> RED. Use an Enum for the

# colors and implement `next_light()` so it returns the next color in the cycle.

# Note: do not use strings like "red" anywhere. The point of an Enum is that a
# typo like "rde" becomes impossible.

# Evaluate the time and space complexity of `next_light()`. Define your variables
# and provide a rationale for why you believe your solution has the stated time
# and space complexity.
# =============================================================================
 
from enum import Enum
 
class Light(Enum):
    #name #value 
    RED = 1
    GREEN = 2
    YELLOW = 3
 
def next_light(light):
        
    if light.name == Light.RED.name:
        return Light.GREEN

    if light.name == Light.GREEN.name:
        return Light.RED
    
    if light.name == Light.YELLOW.name:
        return Light.RED
 
# Complexity of next_light():
# Time: o(n)
# Space:
# Variables:
# Rationale:
 
 
def example_problem_1():
    print(next_light(Light.RED))
    print(next_light(Light.GREEN))
    print(next_light(Light.YELLOW))
    
answer1 = example_problem_1()
 
# Example Output:
# Light.GREEN
# Light.YELLOW
# Light.RED
 
 


# =============================================================================
# PROBLEM 3  (Composition)
# ---------
# A house is made of rooms. A room has no meaning outside its house, and when the
# house is demolished, its rooms go with it. 

# Implement `House` so that it creates
# its own `Room` objects from a list of names, 
# implement `room_names()`.

# Note: the House must build the Room objects itself, inside __init__. If Room
# objects are created outside and passed in, the lifetimes are no longer tied together and it isn't composition.

# Evaluate the time and space complexity of `House.__init__()`. Define your
# variables and provide a rationale for why you believe your solution has the
# stated time and space complexity.
# =============================================================================
 

# class house -> has its own data, rooms
# class House():
#     def __init__(self, rooms:list[str]):
#         self.rooms = rooms 


# # class room -> has its own data names
# class Room():
#     def __init__(self, House):
#         self.list = []
#         self.house = House
    
#     def add_rooms_to_list(self):
#         for room in self.house.rooms:
#             self.list.append(room)
            
        
#         print(self.list) 
                        
                        
    
            
 
# # Complexity of House.__init__():
# # Time:
# # Space:
# # Variables:
# # Rationale:
 
 
# h = House(["Kitchen", "Bedroom", "Bathroom"])
# r = Room(h)
# r.add_rooms_to_list() 
 
 
# Example Output:
# ['Kitchen', 'Bedroom', 'Bathroom']
# Room




class House:
    def __init__(self, names: list[str]):
        self.names = names
        
        self.Room = Room
        self.rooms = []

    def room_names(self):
        for room in self.names:
            self.rooms.append(self.Room(room))

        result = []
        for room in self.rooms:
            result.append(room.name)
        return result


class Room:
    def __init__(self, name: str):
        self.name = name
        
        
    
h = House(["Kitchen", "Bedroom", "Bathroom"])
x = h.room_names()
print(x)
