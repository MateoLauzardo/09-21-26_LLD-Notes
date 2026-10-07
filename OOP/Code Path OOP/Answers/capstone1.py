

# PROBLEM 1  (Enum) (✅)
# ---------
# A traffic light cycles RED -> GREEN -> YELLOW -> RED. 
# Use an Enum for the colors and implement `next_light()` so it returns the next color in the cycle.

# Note: do not use strings like "red" anywhere. The point of an Enum is that a typo like "rde" becomes impossible.

# Evaluate the time and space complexity of `next_light()`. Define your variables
# and provide a rationale for why you believe your solution has the stated time
# and space complexity.
 
from enum import Enum 

class Light(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3
 
def next_light(light):
    
    
    if light == Light.RED:
        return Light.GREEN 
    
    if light == Light.GREEN:
        return Light.YELLOW 
    
    if light == Light.YELLOW:
        return Light.RED


    # return something 
 
# Complexity of next_light():
# Time:
# Space:
# Variables:
# Rationale:
 
 
def example_problem_1():
    print(next_light(Light.RED))
    print(next_light(Light.GREEN))
    print(next_light(Light.YELLOW))
 
 
# answer1 = example_problem_1()

# Example Output:
# Light.GREEN
# Light.YELLOW
# Light.RED





#___________________________________________________________________________________


# PROBLEM 2  (Interface) / (abstraction) (✅)
# ---------
# Every shape must be able to report its area, but each shape calculates it
# differently. 
 

# Make `Shape` an interface so that it cannot be created directly

# implement `Rectangle` and `Square` so that each provides its own `area()`.

# Note: if `Shape` can be instantiated, it isn't an interface yet. Check what
# `ABC` and `@abstractmethod` actually enforce.

# Evaluate the time and space complexity of `area()`. Define your variables and
# provide a rationale for why you believe your solution has the stated time and
# space complexity.


from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod    
    def area(self):
        pass
 
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
        
 
class Square(Shape):
    def __init__(self, side):
        self.side = side 
        
    def area(self):
        return self.side ** 2 
    
 
# Complexity of area():
# Time:
# Space:
# Variables:
# Rationale:
 
 
def example_problem_2():
    shapes = [Rectangle(2, 3), Square(4)]
    print([s.area() for s in shapes])
 
    try:
        Shape()
    except TypeError:
        print("Cannot create a Shape directly")
 
 
answer2 = example_problem_2()

# Example Output:
# [6, 16]
# Cannot create a Shape directly


#___________________________________________________________________________________

# PROBLEM 3  (Composition) (✅)
# ---------

# A house is made of rooms. A room has no meaning outside its house, and when the
# house is demolished, its rooms go with it. 

# Implement `House` so that it creates its own `Room` objects from a list of names, and implement `room_names()`.
# Note: the House must build the Room objects itself, inside __init__. If Room objects are created outside and passed in, the lifetimes are no longer tied
# together and it isn't composition.

# Evaluate the time and space complexity of `House.__init__()`. Define your
# variables and provide a rationale for why you believe your solution has the
# stated time and space complexity.

 
class Room:
    def __init__(self, name):
        self.name = name
 
class House:
    def __init__(self, room_names: list[str]):
        self.rooms = []
        
        for names in room_names:
            self.room = Room(names) # creating our object
            self.rooms.append(self.room) # this is adding it into our list 
        
 
    def room_names(self):
        
        answer = []
        
        for x in self.rooms:
            answer.append((x.name))
        
        return answer 
 
# Complexity of House.__init__():
# Time:
# Space:
# Variables:
# Rationale:
 
 
def example_problem_3():
    h = House(["Kitchen", "Bedroom", "Bathroom"])
    print(h.room_names())
    print(type(h.rooms[0]).__name__)
    
# answer = example_problem_3()
 
# Example Output:
# ['Kitchen', 'Bedroom', 'Bathroom']
# Room
 
 
#___________________________________________________________________________________


# PROBLEM 4  (Aggregation) (✅)
# ---------
# A team has players, but players exist before they join a team and keep existing after they leave. 

# Implement `add_player()` and `remove_player()` so that removing a player from the team does not destroy the player.

# Note: compare this with Problem 3. Here the Player objects are created OUTSIDE the Team and handed in. That one difference is what makes this aggregation
# instead of composition.

# Evaluate the time and space complexity of `remove_player()`. Define your
# variables and provide a rationale for why you believe your solution has the
# stated time and space complexity.

 
class Player:
    def __init__(self, name):
        self.name = name
 
class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []
 
    def add_player(self, player):
        self.players.append(player)
 
    def remove_player(self, player):
        for key, value in enumerate(self.players):
            if player == value:
                del self.players[key]
 
# Complexity of remove_player():
# Time:
# Space:
# Variables:
# Rationale:
 
 
def example_problem_4():
    mia = Player("Mia")
    leo = Player("Leo")
    
    t = Team("Hawks")
    t.add_player(mia)
    t.add_player(leo)
    
    t.remove_player(mia)
    print([p.name for p in t.players])
    print(mia.name)
 
 
# answer2 = example_problem_4()
 
# Example Output:
# ['Leo']
# Mia
 
 
#___________________________________________________________________________________


# PROBLEM 5  (Injected Dependency) (✅)
# ---------
# A store notifies customers when an order is placed. Some stores send emails and
# others send texts. 

# Implement `Store` so that the notifier is passed into its constructor, letting the same Store class work with either kind of notifier.

# Note: Store must never create an EmailNotifier or TextNotifier itself.

# If you see `EmailNotifier()` inside the Store class, the dependency isn't injected.

# Evaluate the time and space complexity of `place_order()`. Define your
# variables and provide a rationale for why you believe your solution has the
# stated time and space complexity.
 
class Notifier(ABC):
    
    @abstractmethod
    def send(self, message):
        pass
 
 
class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Email: Order Placed: {message}")
 
class TextNotifier(Notifier):
    def send(self, message):
        print(f"Text: Order Placed: {message}")
 
 
 
class Store:
    def __init__(self, notifier):
        self.notifier = notifier
 
    def place_order(self, item):
        
        if self.notifier == EmailNotifier():
            self.notifier.send(item)
            
        else:
            self.notifier.send(item)

        
              
# Complexity of place_order():
# Time:
# Space:
# Variables:
# Rationale:
 
 
def example_problem_5():
    s1 = Store(EmailNotifier())
    s2 = Store(TextNotifier())
    s1.place_order("book")
    s2.place_order("pen")
 
answer5 = example_problem_5()

# Example Output:
# Email: Order placed: book
# Text: Order placed: pen

 
#___________________________________________________________________________________

