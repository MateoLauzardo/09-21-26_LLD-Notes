
from abc import ABC, abstractmethod
from collections import deque

class Container(ABC):
    
    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def remove():
        pass

    @abstractmethod
    def is_empty():
        pass


class Stack(Container):
    
    def __init__(self):
        self.stack = []
    
    def add(self, item):
        self.stack.append(item)
    
    def remove(self):
        if not self.stack:
            return None
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0 
    
     

class Queue(Container):
    
    def __init__(self):
        self.queue = deque()
    
    def add(self, item):
        self.queue.append(item)
    
    def remove(self):
        if not self.queue:
            return None
        return self.queue.popleft() # removes first first value added 
    
    def is_empty():
        return len(self.queue) == 0 




def drain(container):
    
    if isinstance(container, Stack):
        
        new_stack = []
        stack = container.stack
        new_stack.append(stack[::-1])
        container.stack = []
        return new_stack[0]
        
        
    
    if isinstance(container, Queue):
        
        old_container = container.queue
            
        # reset
        container.queue = []
            
            
        return old_container
        
    
   
    

s = Stack()
q = Queue()
for x in [1, 2, 3]:
    s.add(x)
    q.add(x)
print(drain(s))
print(drain(q))
print(s.is_empty())
# print(s.stack)
# print(q.queue)
print(q.remove())


# output
# [3, 2, 1]
# [1, 2, 3]
# True
# None