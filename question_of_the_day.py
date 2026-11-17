



from abc import ABC, abstractmethod 

# remembers the exact order in which 
# key-value pairs are inserted
from collections import OrderedDict 



class Cache(ABC):
    
    def __init__(self, capacity):
        self.capacity = capacity
    
    @abstractmethod
    def get(self, key):
        pass 
    
    @abstractmethod
    def put(self, key, value):
        pass 
    
    @abstractmethod
    def keys(self):
        pass 


# count as a “use.” When the cache is full 
# and a new key is added, evict the key that was 
# inserted first.
class LRUCache(Cache):
    
    def __init__(self, capacity):
        self.capacity = capacity
    
        self.hashmap = OrderedDict()
    
    def get(self, keys):
        
        # if key not in hashmap     
        if keys not in self.hashmap:
            return -1
        
        # returns value MUST push to back
        self.hashmap.move_to_end(keys)
        return self.hashmap[keys]    
        
    
    def put(self, key, value):
        
        # repalces key values 
        if key in self.hashmap:
            self.hashmap[key] = value 
            self.hashmap.move_to_end(key) # updates the position.
            return 
        
        # if capacity is full remove first 
        if len(self.hashmap) >= self.capacity:
            self.hashmap.popitem(last=False)
        
         
        # adds the new every time 
        self.hashmap[key] = value 
        

    
    def keys(self):
        key_box = []
        
        for key, value in self.hashmap.items():
            key_box.append(key)
            
        return key_box
             
    
    

# (First In, First Out). Only inserting a new key 
# affects order. When the cache is full, 
# evict the key that was inserted first.
class FIFOCache(Cache):
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = OrderedDict()
    
    
    def get(self, keys):
        
        if keys not in self.hashmap:
            return -1 
        
        return self.hashmap[keys] 
    
    
    def put(self, key, value):
        
        # repalces key values (do not need to send any value to the back of the line)
        if key in self.hashmap:
            self.hashmap[key] = value 
            return
        
        # if capacity is full remove first 
        if len(self.hashmap) >= self.capacity:
            self.hashmap.popitem(last=False)
                
                 
        # adds the new every time 
        self.hashmap[key] = value 


    def keys(self):
        key_box = []
                
        for key, value in self.hashmap.items():
            key_box.append(key)
                    
        return key_box 





lru = LRUCache(2)
lru.put("a", 1)
lru.put("b", 2)
print(lru.get("a"))
lru.put("c", 3)
print(lru.get("b"))
print(lru.keys())

fifo = FIFOCache(2)
fifo.put("a", 1)
fifo.put("b", 2)
fifo.get("a")
fifo.put("c", 3)
print(fifo.get("a"))
print(fifo.keys())


#NOTE example output 
# 1
# -1
# ['a', 'c']
# -1
# ['b', 'c']
    
    