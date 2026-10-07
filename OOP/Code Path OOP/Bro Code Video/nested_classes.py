# nested class - a class that is defined within another class.

# benifits - allows you to logically group classes that r closely related. 
#            helps reduce possibility of naming conflicts. ]


#!SECTION -> 


#___________________________________________________________________________________


class Company():
    
    
    #NOTE: this is a whole other class (this class does its own thing)
    class Employee():
        
        def __init__(self, name, position):
            self.name = name 
            self.position = position
    
        def get_details(self):
            return f"name is: {self.name} and position is: {self.position}"
        
        
    #NOTE: constructor for company (everything here is inside company)
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []
    
    
    #! this is an instance of nested class, we are calling the class inside to get a certain output    
    def add_employee(self, name, position):
        #NOTE: you use self cuz it allows u to see from class company which when you do self.classname can get anything
        new_employee = self.Employee(name, position)
        
        
        self.employees.append(new_employee)
    
    
    def list_employees(self):
        for employee in self.employees:
            print(employee.get_details())
    

    
company = Company("MTZ-editz")

company.add_employee("mateo", "editor")
company.add_employee("x", "idk1")
company.add_employee("y", "idk2")

# company.list_employees()

        
#___________________________________________________________________________________

#! Implementing nested classes and class methods 

class Github():
        
    class Contributors():
        
        list_of_people = []
        
        def __init__(self, name, perms):
            self.name = name 
            self.perms = perms
            Github.Contributors.list_of_people.append(self.name)
        
        
            
        @classmethod 
        def list_contributors(cls):
            # for names in Github.Contributors.list_of_people:
            #     print(names)
            return cls.list_of_people
            
            
                
    def __init__(self, organization):
        self.organization = organization
        # self.contributors = []

        
    def add_contributor(self, name, perms):
        self.Contributors(name, perms)
        
    
    def get_list_contributors(self):
            return self.Contributors.list_contributors()
    
  
  
github = Github("MTZ")
github.add_contributor("mateo","owner")
github.add_contributor("x","normal")
print(github.get_list_contributors())


#___________________________________________________________________________________  
    
    

