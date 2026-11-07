# Question 4: Polymorphism + Heap

import heapq
from abc import ABC, abstractmethod


class Patient(ABC):
    def __init__(self, name):
        self.name = name  
    
    @abstractmethod
    def prority(self):
        pass 
    
    
class CriticalPatient(Patient):
    
    def prority(self):
        return 1

class UrgentPatient(Patient):
    
    def prority(self):
        return 2

class RoutinePatient(Patient):
    
    def prority(self):
        return 3
    
    
class ERQueue:
    def __init__(self):
        self.heap = [] 
        self.counter = 0 

                         #object 
    # generates:  (3, 0, Ava)
                # (1, 1, Ben)
                # (2, 2, Cal)
                # (1, 3, Dee)
    def admit(self, patient):
        heapq.heappush(self.heap, (patient.prority(), self.counter, patient))
        self.counter += 1

    #NOTE which paitent we should see, smallest is most urgent 
    # so when we pop that is the most urgent 
    def next_patient(self):
        if len(self.heap) == 0:
            return None 
        
        # Pop the smallest tuple -> at index 0 
        priority, count, patient = heapq.heappop(self.heap)
        
        return patient.name
    
    
    
er = ERQueue()
er.admit(RoutinePatient("Ava"))
er.admit(CriticalPatient("Ben"))
er.admit(UrgentPatient("Cal"))
er.admit(CriticalPatient("Dee"))
print(er.next_patient())
print(er.next_patient())
print(er.next_patient())
print(er.next_patient())
print(er.next_patient())


# example output 
# Ben
# Dee
# Cal
# Ava
# None