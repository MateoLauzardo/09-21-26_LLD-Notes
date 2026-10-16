# Write a class Pizza that takes a topping and a size. The class should keep a class-level counter total_created that increases by 1 every time a Pizza is made. 
# Add a class method from_string(order) that takes a string in the format "topping:size" and returns a new Pizza object. 
# Pizzas made through from_string() must also count toward total_created.



class Pizza():    
    
    total_created = 0 
    
    def __init__(self, topping, size):
        self.topping = topping
        self.size = size
         
        Pizza.total_created += 1    
        
        
    @classmethod
    def from_string(cls, string):
        pass
        
        # break up string 
        split_array = string.split(":") 
        topping = split_array[0]
        size = split_array[1]

        # pass in values using cls 
        return Pizza(topping, size)
        
        
        
        
        
p1 = Pizza("cheese", "small")
p2 = Pizza.from_string("pepperoni:large")
print(p2.topping, p2.size)
print(Pizza.total_created)

# pepperoni large
# 2