# Write a class Node that stores a value and a next pointer.
# Then write a class LinkedList with:
# append(value) adds a new node to the end of the list.
# to_list() returns the values as a Python list, from head to tail.
# __len__() returns the number of nodes.


# Then write a subclass SortedLinkedList 
# that overrides only append() so that values are inserted in ascending order. 
# It must reuse to_list() and __len__() from the parent 
# without redefining them


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

    # sets the next value to the parameter value and updates the current 
    # status to the value just added 
    def append(self, value):
        
        # composition 
        new_node = Node(value)
        
        current = self.head
        
        # if we dont have head right now than make it head 
        if self.head is None:
            self.head = new_node
            return
                        
        while current.next is not None:
            current = current.next
        current.next = new_node


    # we need to than convert the link list a list 
    # i assume loop through the entire thing and add to an array 
    def to_list(self):
        
        result = [] 
        current = self.head 
        
     
        while current is not None:
            result.append(current.value)
            current = current.next 
            
        return result 
            
        
        
    def __len__(self):
        
        count = 0
        current = self.head
        
        while current is not None:
            count += 1
            current = current.next
        return count
    


#NOTE: review 
class SortedLinkedList(LinkedList):
    def append(self, value):
        
        new_node = Node(value)
        
        if self.head is None or value < self.head.value:
            new_node.next = self.head
            self.head = new_node
            return
        
        # walk to the node just before the insert spot
        current = self.head
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


# output 
# [3, 1, 2]
# [1, 2, 3]
# 3
# True