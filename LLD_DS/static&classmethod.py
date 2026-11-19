
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
    
