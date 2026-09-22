#NOTE: Enum = short for enumeration. defines a fixed restrcited set of constant values.

# enum allows you to do .item and .value -> item being your key and obv .value being your value.
# you are able to loop through this class and whatever x is is allowed to call methods 











# ------------------------------------------------------

from enum import Enum

#NOTE problem 1
# takes in straing, no matter if its messed up and reutrn the  matching VehicleType member
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

    

# print(VehicleType("car")) # VehicleType.CAR
# print(VehicleType["CAR"]) # VehicleType.CAR


# Example Usage:
# print(parse_vehicle_type("  Car "))
# print(parse_vehicle_type("TRUCK"))
# print(parse_vehicle_type("boat"))

# Example Output:
# VehicleType.CAR 
# VehicleType.TRUCK
# ValueError: 'boat' is not a valid VehicleType

# ------------------------------------------------------

#NOTE: Problem 2
# Given a list of `Order` objects, write a function `count_by_status()` that
# returns a dictionary mapping every member of `OrderStatus` to the number of
# orders in that state. Statuses with zero orders must still appear with a count
# of 0.
# Note: do not hardcode the list of statuses - derive it from the enum itself.
# Evaluate the time and space complexity of your solution. Define your variables
# and provide a rationale for why you believe your solution has the stated time
# and space complexity.


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


#NOTE: debugging 
# for member in OrderStatus:
#     print(member, "|", member.name, "|", member.value)


# Example Output:
# ```
# {<OrderStatus.PLACED: 'placed'>: 2, 
# <OrderStatus.SHIPPED: 'shipped'>: 1, 
# <OrderStatus.DELIVERED: 'delivered'>: 0, 
# <OrderStatus.CANCELLED: 'cancelled'>: 0}
# ```