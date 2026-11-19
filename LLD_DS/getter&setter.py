


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
    
