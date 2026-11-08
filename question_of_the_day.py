# Question 1: Encapsulation + Stack



# ["homepage", "a.com", "b.com"] 
class BrowserHistory():
    def __init__(self, homepage):
        
        self.current = homepage        
        self.forward_stack = [] 
        self.back_stack = []
    
    
    def visit(self, url):
        # update back with last value we were on 
        self.back_stack.append(self.current)
        # change current to the url
        self.current = url 
        # clear foward 
        self.forward_stack.clear()
    
    
    def back(self):
        
        if len(self.back_stack) == 0:
            return None
        
        self.forward_stack.append(self.current)
        self.current = self.back_stack.pop()
        return self.current
        
    
    def forward(self):
        
        if len(self.forward_stack) == 0:
            return None 
        
        self.back_stack.append(self.current)
        self.current = self.forward_stack.pop()
        return self.current
    
    
    def current(self):
        return self.current
    
    
h = BrowserHistory("home.com")
h.visit("a.com")
h.visit("b.com")
print(h.back())
print(h.back())
print(h.back())
print(h.forward())
h.visit("c.com")
print(h.forward())
print(h.current)


# example output: 
# a.com
# home.com
# None
# a.com
# None
# c.com