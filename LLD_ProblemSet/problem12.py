<<<<<<< HEAD

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
=======
#NOTE problem 1


# Encapsulation + Stack
class BrowserHistory:
    def __init__(self, homepage):
        self.__current = homepage # data type is a string
        self.__back_stack = []
        self.__forward_stack = []
        
    def visit(self, url):
        self.__back_stack.append(self.__current)
        self.__current = url
        self.__forward_stack = []
        
    def back(self):
        
        if len(self.__back_stack) == 0:
            return None
        
        else:
            self.__forward_stack.append(self.__current)
            self.__current = self.__back_stack[-1] # read the top
            self.__back_stack.pop() # remove the top
            return self.__current
        

    def forward(self):
        
        if len(self.__forward_stack) == 0:
                return None
        
        else:
            self.__back_stack.append(self.__current)
            self.__current = self.__forward_stack[-1]
            self.__forward_stack.pop()
            return self.__current
    

    def current(self):
        return self.__current
    


h = BrowserHistory("home.com")
h.visit("a.com")
h.visit("b.com")
print(h.back())
print(h.back())
print(h.back())
print(h.forward())
h.visit("c.com")
print(h.forward())
print(h.current())


#output 
# a.com
# home.com
# None
# a.com
# None
# c.com

# ------------------------------

#NOTE Question 2: Abstraction + Stack and Queue

>>>>>>> 7133be6596ddde61af3325db31b590fc2b408077
