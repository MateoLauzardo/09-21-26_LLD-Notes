import heapq 



class Patient():

    def __init__(self, name):
        self.name = name 

    def priority(self):
        raise NotImplementedError  



class CriticalPatient(Patient):

    def priority(self):
        return 1 

class UrgentPatient(Patient):

    def priority(self):
        return 2 

class RoutinePatient(Patient):

    def priority(self):
        return 3 


class ERQueue():

    def __init__(self):
        self.heap = []
        self.count = 0 

    def admit(self, patient):

        # patient is an object 
        # so patient.priority
        # need to compare priorities
        # if patient.priority() < other_patient.priority():
        # add to heap
        self.count += 1


        #NOTE: this is how you add a patient to the heap, with their priority, a count to break ties, and their name
        heapq.heappush(self.heap, (patient.priority(), self.count, patient.name)) 



    def next_patient(self):
        #NOTE if the heap is not empty, pop the patient with the highest priority (lowest number) and return their name
        if self.heap:
            return heapq.heappop(self.heap)[2]
        else:
            return None 

     



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


#NOTE: example output 
# Ben
# Dee
# Cal
# Ava
# None