

# Question 4: Polymorphism Through Inheritance and Duck Typing

from abc import ABC, abstractclassmethod


class Employee(ABC):
    
    def __init__(self, name):
        self.name = name 
    
    @abstractclassmethod
    def monthlyPay(self):
        pass 
    
    @abstractclassmethod
    def pay_stub(self):
        pass
    

# needs to override monthly pay
class FullTime(Employee):
    
    def __init__(self, name, salary):
        # super().__init__(name)
        self.name = name
        self.salary = salary
        
    # return salary // 12 
    def monthlyPay(self):
        return self.salary // 12  
    
    def pay_stub(self):
        return f"{self.name}: {FullTime.monthlyPay(self)}"

# needs to override monthly pay
class Hourly(Employee):
    
    def __init__(self, name, rate, hours):
        # super().__init__(name)
        self.name = name
        self.rate = rate 
        self.hours = hours 
        
    def monthlyPay(self):
            return self.rate * self.hours  
    
    def pay_stub(self):
            return f"{self.name}: {Hourly.monthlyPay(self)}"
        

#NOTE does not inherit
class Contractor():
    
    def __init__(self, name, pay):
        self.name = name 
        self.pay = pay 
        
    # own function, same name 
    def monthlyPay(self):
        return self.pay
    
    def pay_stub(self):
        return f"{self.name}: {Contractor.monthlyPay(self)}"


# function -> workers is a list full of objects 
def payroll(workers):
    
    total = 0 
    
    for w in workers:
        total += w.monthlyPay()
        
    return total
        
    
         
         
workers = [FullTime("Ana", 60000), Hourly("Ben", 20, 80), Contractor("Cy", 3000)]
for w in workers:
    print(w.pay_stub())
print(payroll(workers))
print(isinstance(workers[2], Employee))


#example output 
# Ana: 5000
# Ben: 1600
# Cy: 3000
# 9600
# False