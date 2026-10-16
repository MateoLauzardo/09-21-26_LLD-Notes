# Design a small vehicle rental system.
# Write an abstract class Vehicle that takes a plate and a daily_rate and has an abstract method rental_cost(days)
# Write two subclasses that use super().__init__(): Car, which also takes an insurance_fee and costs daily_rate * days + insurance_fee, and Truck, which also takes load_tons and costs daily_rate * days + load_tons * 20.
# Then write a class RentalAgency that contains a list of vehicles (composition) with methods add_vehicle(vehicle), total_revenue(days), which returns the sum of every vehicle’s rental cost for that many days, and most_expensive(days), which returns the plate of the vehicle with the highest rental cost for that many days.

from abc import ABC, abstractmethod

class Vechile(ABC):
    def __init__(self, plate, daily_rate):
        self.plate = plate 
        self.daily_rate = daily_rate
        
    @abstractmethod
    def rental_cost(self, days):
        pass
    

class Car(Vechile):
    def __init__(self, plate, daily_rate, insurance_fee):
        super().__init__(plate, daily_rate)
        self.insurance_fee = insurance_fee
        
    
    def rental_cost(self, days):
        return (self.daily_rate * days) + self.insurance_fee
    
# which also takes load_tons and 
# costs daily_rate * days + load_tons * 20.
class Truck(Vechile):
    def __init__(self, plate, daily_rate, load_tons):
        super().__init__(plate, daily_rate)
        self.load_tons = load_tons
        
    def rental_cost(self, days):
        return (self.daily_rate * days) + (self.load_tons * 20)
        

#! where everything interconnects   
class RentalAgency:
    
    def __init__(self):
        self.list = [] 
        
    def add_vehicle(self, vehicle):
        self.list.append(vehicle)
    
    # math is wrong in sub classes 
    def total_revenue(self, days):
    
        cost = 0
        
        for x in self.list:
            cost += x.rental_cost(days) 
            
        return cost 
        
    # reuturn name of car for highest day 
    def most_expensive(self, days):
        highest_day = 0
        highest_car = ""
        
        for x in self.list:
            if highest_day < x.rental_cost(days):
                highest_day = x.rental_cost(days)
                highest_car = x.plate
                        
        return highest_car 
            


agency = RentalAgency()
agency.add_vehicle(Car("ABC123", 50, insurance_fee=30))
agency.add_vehicle(Truck("XYZ789", 80, load_tons=5))
print(agency.total_revenue(3))
print(agency.most_expensive(3))
    
# output:    
# 520
# XYZ789