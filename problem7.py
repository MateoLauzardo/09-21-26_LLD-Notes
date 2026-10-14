# Write a class TemperatureConverter with three static methods. 
# c_to_f(celsius) returns the temperature in Fahrenheit, f_to_c(fahrenheit) returns the temperature in Celsius, and is_valid_celsius(celsius) returns True if the value is at or above absolute zero (-273.15), otherwise False. 
# The methods should be callable without creating an instance of the class.



class TemperatureConverter():
    def __init__(self):
        pass
    
    @staticmethod
    def c_to_f(celsius):
        return (celsius * 1.8) + 32 
    
    @staticmethod
    def f_to_c(fahrenheit):
        return ((fahrenheit - 32) * 5) / 9
    
    @staticmethod
    def is_valid_celsius(celsius):
        if celsius > -273.15:
            return True 
        else:
            return False 
        
    
print(TemperatureConverter.c_to_f(100))
print(TemperatureConverter.f_to_c(32))
print(TemperatureConverter.is_valid_celsius(-300))
    
# 212.0
# 0.0
# False