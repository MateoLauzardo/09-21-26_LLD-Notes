#NOTE: Enum = short for enumeration. defines a fixed restrcited set of constant values.

# enum allows you to do .item and .value -> item being your key and obv .value being your value.
# you are able to loop through this class and whatever x is is allowed to call methods 






# ------------------------------------------------------


# #NOTE problem 1
# # takes in straing, no matter if its messed up and reutrn the  matching VehicleType member

from enum import Enum


class VehicleType(Enum):
    
    MOTORCYCLE = "motorcycle"
    CAR = "car"
    TRUCK = "truck"

def parse_vehicle_type(raw):
    
    raw = raw.strip()
    new_raw = raw.upper()
    
    try:
        # because we made it all caps like its key,  we need to have in brackets 
        return (VehicleType[new_raw])
    
    except KeyError:
        print("ValueError:" ,raw,"is not a valid VehicleType")




print(VehicleType("car")) # VehicleType.CAR
print(VehicleType["CAR"]) # VehicleType.CAR


# # Example Usage:
# print(parse_vehicle_type("  Car "))
# print(parse_vehicle_type("TRUCK"))
# print(parse_vehicle_type("boat"))

# # Example Output:
# # VehicleType.CAR 
# # VehicleType.TRUCK
# # ValueError: 'boat' is not a valid VehicleType

# # ------------------------------------------------------

# #NOTE: Problem 2
# # Given a list of `Order` objects, write a function `count_by_status()` that
# # returns a dictionary mapping every member of `OrderStatus` to the number of
# # orders in that state. Statuses with zero orders must still appear with a count
# # of 0.
# # Note: do not hardcode the list of statuses - derive it from the enum itself.
# # Evaluate the time and space complexity of your solution. Define your variables
# # and provide a rationale for why you believe your solution has the stated time
# # and space complexity.

from enum import Enum

class OrderStatus(Enum):
    # .name -> .value
    PLACED = "placed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class Order:
    def __init__(self, order_id, status):
        self.order_id = order_id
        self.status = status

def count_by_status(orders):

    hashmap = {}
    
    # the first thing i would do is update hashmap already SO it has every value from class and value is 0 
    # the member represents "OrderStatus.X"
    for member in OrderStatus:
        hashmap[member] = 0
    
    # need to loop through every value in orders 
    # # this is good but wants to return values that have 0 that may not even been in the array orders
    for order in orders:
        
        # updates hashmap -> {}
        if order.status in hashmap:
            hashmap[order.status] += 1
        else:
            hashmap[order.status] = 1
        
    
    return hashmap 
  
    
    


orders = [
    # because the class are values, when we loop through this array we get access to methods of class for every instance of x 
    Order(1, OrderStatus.PLACED),
    Order(2, OrderStatus.SHIPPED),
    Order(3, OrderStatus.PLACED),
]


print(count_by_status(orders))


# #NOTE: debugging 
# # for member in OrderStatus:
# #     print(member, "|", member.name, "|", member.value)


# # Example Output:
# # {<OrderStatus.PLACED: 'placed'>: 2, 
# # <OrderStatus.SHIPPED: 'shipped'>: 1, 
# # <OrderStatus.DELIVERED: 'delivered'>: 0, 
# # <OrderStatus.CANCELLED: 'cancelled'>: 0}


# ------------------------------------------------------


# NOTE: PROBLEM 3
# An enum member can carry more than one piece of data. Define `VehicleType` so
# that each member knows both a human-readable label and the number of parking
# spots that vehicle consumes. Then write `spots_required()`, which takes a list
# of `VehicleType` members and returns the total spots needed.
# Note: give each member a tuple value and unpack it in `__init__`. `self._value_`
# controls what `.value` returns.
# Evaluate the time and space complexity of `spots_required()`. Define your
# variables and provide a rationale for why you believe your solution has the
# stated time and space complexity.


from enum import Enum

class VehicleType(Enum):
    # .name       # value 
    MOTORCYCLE = ("Motorcycle", 1)
    CAR = ("Car", 1)
    TRUCK = ("Truck", 2)
    
    # to initialize an objects attributes -> in this instance vechile types 
    def __init__(self, label: str, spots: int):
        self.label = label
        self.spots = spots
        


# takes in an array
def spots_required(vehicles: list):
    
    total = 0 
    
    for vechile in vehicles:
        car_number = vechile.value[1] 
        
        total += car_number
        
    return total   
        
    


# Example Usage:
print(VehicleType.TRUCK.label)
print(VehicleType.TRUCK.spots)
print(spots_required([VehicleType.CAR, VehicleType.TRUCK, VehicleType.MOTORCYCLE]))


#SECTION Example Output:
# Truck
# 2
# 4


#NOTE: Debuging area:
# print(VehicleType.TRUCK) # -> VehicleType.TRUCK
# print(VehicleType.TRUCK.value) # -> ('Truck', 2)
# print(VehicleType.TRUCK.name) # -> TRUCK
# value = VehicleType.CAR.value # -> ("Car", 1)
# car_number = VehicleType.CAR.value[1]
# print("debug ",car_number)


# ------------------------------------------------------

#NOTE PROBLEM 4
# Enums can have methods. Add a method `is_terminal()` to `TicketStatus` that
# returns `True` only for states no further transition can leave. Then write a
# function `active_tickets()` that filters a list of tickets down to the
# non-terminal ones.
# Note: the method lives on the enum class itself and `self` is the member.
# Evaluate the time and space complexity of `active_tickets()`. Define your
# variables and provide a rationale for why you believe your solution has the
# stated time and space complexity.


from enum import Enum

class TicketStatus(Enum):
    # name    # value
    ISSUED = "issued"
    ACTIVE = "active"
    PAID = "paid"
    LOST = "lost"
    
    #  returns `True` only for "paid" no further transition can leave
    def is_terminal(self):
        
        if self.value != "paid":
            return False

        else:
            return True



class Ticket:
    def __init__(self, ticket_id, status):
        self.ticket_id = ticket_id
        self.status = status


# filters a list of tickets down to the non-terminal ones.
# non terminal is anything BESIDES 'paid'
def active_tickets(tickets):

    count = [] 
    
    for ticket in tickets:
        
        status = ticket.status # TicketStatus.ACTIVE
        
        if status.value == "paid": # TicketStatus.ACTIVE.value 
            continue 
        else:
            count.append(ticket)
            
    return count
    


#NOTE: Example Usage:
print(TicketStatus.PAID.is_terminal())
print(TicketStatus.ACTIVE.is_terminal())
tickets = [Ticket("T1", TicketStatus.ACTIVE), Ticket("T2", TicketStatus.PAID)]
print([t.ticket_id for t in active_tickets(tickets)])


#NOTE: Example Output:
# True
# False
# ['T1']


#NOTE: debug lines
# for ticket in tickets:
#     print(ticket.ticket_id, ticket.status)
# returns: T1 TicketStatus.ACTIVE -> T2 TicketStatus.PAID

# print(TicketStatus.PAID.value == "paid") 
# returns: True 