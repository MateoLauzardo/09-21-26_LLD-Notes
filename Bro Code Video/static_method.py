# static method - a method that belongs to a class rather than an object 

# instance methods - best for operations on instance of the class (object)
# static methods - best for utility functiosn that do not need access to class data 



#___________________________________________________________________________________

class Employee():
    
    def __init__(self, name, position):
        self.name = name 
        self.position = position 
        
    # this is an instance method. Using info that is passed     
    def get_info(self):
        return f"the name is {self.name} and position is {self.position}"
    
    #! does not rely on u creating object for class 
    #! to use this method (STATICMETHOD)
    @staticmethod
    def is_valid_position(position):
        
        valid_positions = ["Manager", "Editor", "artist"]
        
        return position in valid_positions




employee1 = Employee("MTZ", "Editor")
employee2 = Employee("x", "Manager")
employee3 = Employee("y", "artist")
employee4 = Employee("z", "idk")


           
#! this is an instance of staic method we are not 
#! creating an object like above. We just call class 
#! and method 
print(Employee.is_valid_position("Manager"))


#NOTE: this is an instance method we need to create object and use object to call method 
print(employee1.get_info())

#___________________________________________________________________________________
