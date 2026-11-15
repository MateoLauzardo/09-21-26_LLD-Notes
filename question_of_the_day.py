

class BrowserHistory():
    def __init__(self, homepage):
        self.page = homepage
        self.__back_stack = []
        self.__forward_stack = []
    
    
    def visit(self, url):
             
        self.__back_stack.append(self.page)
        self.page = url
        self.__forward_stack.clear()   # new visit wipes forward history
    
    def back(self):
        
        if len(self.__back_stack) == 0:
            return None 
        
        else:
            self.__forward_stack.append(self.page)
            self.page = self.__back_stack.pop()
            return self.page
        

    def forward(self):
        
        if len(self.__forward_stack) == 0:
            return None 
        
        else:
            self.__back_stack.append(self.page)
            self.page = self.__forward_stack.pop()
            return self.page
    
    
    def current(self):
        return self.page 
    
    

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


#NOTE: Example Output 
# a.com
# home.com
# None
# a.com
# None
# c.com