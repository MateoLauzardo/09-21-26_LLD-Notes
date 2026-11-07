
# Write an abstract class Container 
# with the abstract methods add(item), remove(), and is_empty().
# Then write two concrete subclasses:




from abc import ABC, abstractmethod
from collections import deque

class Container(ABC):
    
    @abstractmethod
    def add(self, item):
        pass
    
    @abstractmethod
    def remove(self):
        pass
    
    @abstractmethod
    def is_empty(self):
        pass


# stack -> first in last out 
class Stack(Container):
    
    def __init__(self):
        # just an array we are turning into a stack
        self.list = []
    
    def add(self, item):
        self.list.append(item)
        
    def remove(self):
        
        if len(self.list) == 0:
            return None 
        
        # removes the last element
        return self.list.pop()
        
        
    def is_empty(self):
        if len(self.list) == 0:
            return True 
        else:
            return False 



class Queue(Container):
    
    def __init__(self):
        # just an array we are turning into a queue
        self.list = []
    
        
    def add(self, item):
        self.list.append(item)
            
    def remove(self):
            
        if len(self.list) == 0:
            return None 
            
        else:
            # returns the first element
            return self.list.pop(0)


    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False 
    

def drain(container):
    list_answer = []
    while not container.is_empty():
        list_answer.append(container.remove())
    return list_answer




s = Stack()
q = Queue()
for x in [1, 2, 3]:
    s.add(x)
    q.add(x)
print(drain(s))
print(drain(q))
print(s.is_empty())
print(q.remove())


# example output 
# [3, 2, 1]
# [1, 2, 3]
# True
# None