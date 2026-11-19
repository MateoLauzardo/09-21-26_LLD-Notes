


class Thermostat():
    
    def __init__(self, temperature):
        self.__temperature = temperature
        
    
    # NOTE: getters make the method read only 
    # GETTERS returns an attributes value 
    @property
    def temperature(self):
        
        return self.__temperature
    
    
    # NOTE: updatates value based of certain conditions.
    # SETTERS accepts a new value and updates 
    @temperature.setter
    def temperature(self, value):
        
        if 50 < value and value > 90:
            raise ValueError
                
        else:
            self.__temperature = value  
    
    
    # NOTE: getters make the method read only 
    # turn the temp into celsius and return 
    @property
    def celsius(self):
        num = (self.__temperature - 32) * 5/9
        rounded_num = round(num, 1)
        
        return rounded_num
        
        

t = Thermostat(70)
print(t.temperature)
t.temperature = 75
print(t.temperature)
print(t.celsius)
try:
    t.temperature = 120
except ValueError:
    print("Out of range")
print(t.temperature)
try:
    t.celsius = 30
except AttributeError:
    print("celsius is read-only")
    

# example output: 
# 70
# 75
# 23.9
# Out of range
# 75
# celsius is read-only