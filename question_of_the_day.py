

class Node():
    def __init__(self, value):
        self.value = value 
        self.next = None
       
       
        
class LinkedList:
    
    def __init__(self):
        self.current = None
    
     
    def append(self, value):
        # composition
        node = Node(value)
        
        if self.current == None:
            self.current = node
            
        else:
            runner = self.current 
            
            # we keep on moving to the right till we get all the way to the end. which will be the latest value. THAN we go below and do the .next 
            while runner.next is not None:
                runner = runner.next   
                
            runner.next = node  
         
            
     
    def to_list(self):
        
        self.container = []
        
        runner = self.current 
        
        while runner:
            self.container.append(runner.value)
            runner = runner.next
            
        
        return self.container
              
    
    
    def __len__(self):
        
        counter = 0 
        
        runner = self.current 
        
        while runner:
            counter += 1
            runner = runner.next 
    
    
        return counter 
    
    

class SortedLinkedList(LinkedList):
    
    def append(self, value):
        new_node = Node(value)
                
        if self.current is None or value < self.current.value:
            new_node.next = self.current
            self.current = new_node
            return
                
        # walk to the node just before the insert spot
        current = self.current
        while current.next is not None and current.next.value < value:
                current = current.next
                    
                
        # splice in
        new_node.next = current.next
        current.next = new_node
        
    
        
        
           



ll = LinkedList()
sl = SortedLinkedList()
for x in [3, 1, 2]:
    ll.append(x)
    sl.append(x)
print(ll.to_list())
print(sl.to_list())
print(len(sl))
print(isinstance(sl, LinkedList))