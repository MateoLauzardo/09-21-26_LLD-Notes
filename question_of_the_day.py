
#NOTE -> review linked list

class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None
    
        
class LinkedList:
    
    def __init__(self):
        self.head = None 
        
        
    def append(self, value):
        
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node 
        
        else:
            current = self.head 
           
            while current.next is not None:
               current = current.next 
               
            current.next = new_node
                    
    
    def to_list(self):
        to_list = []
        
        current = self.head 
        
        while current:
            to_list.append(current.value)
            current = current.next
           
        return to_list
        
             
    
    def __len__(self):
        count = 0 
        
        
        current = self.head 
        
        while current:
            count += 1 
            current = current.next
           
        return count
    
    
    
class SortedLinkedList(LinkedList):
    def append(self, value):
        
        new_node = Node(value)
        
        
        # Case 1: empty list, or new value belongs before the head
        if self.head is None or value < self.head.value:
            new_node.next = self.head
            self.head = new_node
            return
        
        
        # Case 3: walk to the node just before the insertion spot
        current = self.head
        while current.next is not None and current.next.value < value:
            current = current.next
            
            
        # Insert between current and current.next   
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