from abc import ABC, abstractmethod
from collections import deque

class Container(ABC):
    
    @abstractmethod
    def add(self, item):
        pass
    
    def remove(self):
        pass
    
    def isempty(self):
        pass
    
    
class Stack(Container):
    
    def __init__(self):
        # this super refers to the item that is being inherited from the parent class 
        super().__init__()
        self.stack = []
        
    def add(self, item):
        self.stack.append(item)
        
    def remove(self):
        if not self.isempty():
            return self.stack.pop() 
        
    
    def isempty(self):
        
        if len(self.stack) == 0:
            return True 
        else:
            return False 
        

class Queue(Container):
    
    def __init__(self):
        super().__init__()
        self.queue = []
        
    def add(self, item):
        self.queue.append(item)
        
    def remove(self):
        if len(self.queue)!= 0:
            return self.queue.pop(0)
            
    def isempty(self):
        return len(self.queue) == 0 


# container is an object of class Queue or Stack, so can use its remove method 
def drain(Container):
    
    drained_items = []
    
    while Container.isempty() != True:
        removed_item = Container.remove()
        drained_items.append(removed_item)
        
    return drained_items



s = Stack()
q = Queue()
for x in [1, 2, 3]:
    s.add(x)
    q.add(x)
print(drain(s))
print(drain(q))
print(s.isempty())
print(q.remove())


# # output 
# [3, 2, 1]
# [1, 2, 3]
# True
# None