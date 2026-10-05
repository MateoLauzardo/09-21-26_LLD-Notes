#class methods - allow operations related to the class itself. 
#                take cls as first parameter which represents the class itself 

# class method is a method that belongs to the class itself, not to any one object. It gets the class (cls) as its first argument instead of an instance (self).



#___________________________________________________________________________________


class Student():
    
    count = 0
    total_gpa = 0 
    
    def __init__(self, name, gpa):
        self.name = name 
        self.gpa = gpa
        Student.count += 1 #! when you make Object you can grab any varaible from it, this allows us to keep count of how many students are created.
        Student.total_gpa += gpa
        
    # instance method (due to using values passed through the constructor)
    def get_info(self):
        return f"student name is {self.name} and their GPA is {self.gpa}"

    
    
    
    #! this is your class method to grab the variable before the constructor
    @classmethod
    def get_count(cls):
        return f"the count is {cls.count}"
    
    @classmethod 
    def get_average(cls):
        # if there are 0 students
        if cls.count == 0:
            return 0 
        else:
            return f"{cls.total_gpa/ cls.count}"
    
    @classmethod
    def total_gpa_number(cls):
            return f"total number is {cls.total_gpa}"
    

# objects
student1 = Student("mateo", 4.0)
student2 = Student("x", 3.0)
student3 = Student("y", 2.0)
student4 = Student("z", 1.0)


# print(Student.get_count())
print(Student.get_average())
print(Student.total_gpa_number())


#___________________________________________________________________________________
