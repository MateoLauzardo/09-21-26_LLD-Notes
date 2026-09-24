# Composition means one class is built out of other objects, and those 
# objects are usually created right inside __init__ and stored as attributes.

# Composition -> is a design princible where comp[elx systems or objects
# are built by combining similar, simpler, reusable peices of code. 

# Examples: Car (object) and a car has a engine, wheels, and so on

# ------------------------------------------------------------------------------------

#NOTE: PROBLEM 1
# A parking floor owns its spots. Nobody hands spots to a floor and no spot moves
# between floors. Implement `ParkingFloor` so that it takes a count and a spot
# type, BUILDS its own spots, and never exposes the raw list.

# The only way to get at a spot is through `find_available_spot(vehicle_type)`, which returns the first empty spot that fits or `None`.
# Note: composition is more than a list of parts - specifically, the whole creates
# the parts and no external caller can reach in and mutate the collection.

# Evaluate the time and space complexity of `find_available_spot()`. Define your
# variables and provide a rationale for why you believe your solution has the
# stated time and space complexity.


from enum import Enum


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
        
        
        


# -----------------

#NOTE: Example Usage:
# passees in values to class Parking Floor
floor = ParkingFloor(1, {VehicleType.CAR: 2, VehicleType.TRUCK: 1})
# calls the object you create and finds avaliabke spots for the CAR constent
spot = floor.find_available_spot(VehicleType.CAR)
print(spot.spot_id)


# spot is changing value 
spot.occupied = True
print(floor.find_available_spot(VehicleType.CAR).spot_id)


print(floor.occupancy())


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