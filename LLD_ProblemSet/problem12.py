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

