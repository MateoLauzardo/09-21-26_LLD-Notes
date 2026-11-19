
class Ticket():
    
    _next_id = 0 
    
    def __init__(self, holder):
        self.holder = holder 
        Ticket._next_id += 1 
        self.id = self._next_id
    
    # returns how many tickets have been created
    @classmethod
    def total_issued(cls):
        return cls._next_id 
    

    #! does not rely on u creating object for class 
    @staticmethod
    def is_valid_id(value):
        if value > 0:
            return True 
        else:
            return False 
        
        
t1 = Ticket("Ana")
t2 = Ticket("Ben")
t3 = Ticket("Cy")
print(t1.id, t1.holder)
print(t3.id, t3.holder)
print(Ticket.total_issued())
print(Ticket.is_valid_id(5))
print(Ticket.is_valid_id(-2))

#output 
# 1 Ana
# 3 Cy
# 3
# True
# False