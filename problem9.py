# Design a small payroll system. 
# Write an abstract class Employee that takes a name and a base_salary and has an abstract method calculate_pay().
# Write two subclasses that use super().__init__(): Manager, which also takes a bonus and is paid base_salary + bonus, and Engineer, which also takes overtime_hours and is paid base_salary + overtime_hours * 50. 
# Then write a class Company that contains a list of employees (composition) with methods add_employee(employee) and total_payroll(), which returns the sum of everyone’s pay.

#! What we Learned:
# 1.) When you make an ABC you can NOT call that class individually 
# 2.) when using super().__init__() you need to make sure the parameters fit ALL of the values that are from the class we r inherting from.



from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, base_salary):
        self.base_salary = base_salary
        self.name = name
        
    @abstractmethod
    def calculate_pay(self):
        pass 
    


class Manager(Employee):
    
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus 
    
    
    def calculate_pay(self):
        return self.base_salary + self.bonus


# takes overtime_hours and is paid base_salary + overtime_hours * 50. 
class Engineer(Employee):
    
    def __init__(self, name, base_salary, overtime_hours):
        super().__init__(name, base_salary)
        self.overtime_hours = overtime_hours
        
    
    def calculate_pay(self):
        return self.base_salary + (self.overtime_hours * 50)
        
        
        
# Then write a class Company that contains a list of employees (composition) with methods add_employee(employee) and total_payroll(), which returns the sum of everyone’s pay.     
class Company():
    def __init__(self):
        self.list = []
        self.total = 0 
    
    # person -> object / instance of class 
    def add_employee(self, person):
        self.list.append(person)
        
    
    def total_payroll(self):
        for character in self.list:
            self.total += character.calculate_pay()
        
        
        return self.total



company = Company()
company.add_employee(Manager("Ana", 5000, bonus=1000))
company.add_employee(Engineer("Leo", 4000, overtime_hours=10))
print(company.total_payroll())


# 10500