

# Question 6: Composition and Aggregation in One Class



# going to use comp and aggregation 



class CPU:
    def __init__(self, model):
        self.model = model


class RAM:
    def __init__(self, size_gb):
        self.size_gb = size_gb 


class Peripheral:
    def __init__(self, name):
        self.name = name  



class Computer():
    
    def __init__(self, cpu_model=None, ram_gb=None):
        self.cpu_model = cpu_model
        self.ram_gb = ram_gb
        
        self.spec_list = []
        self.device_list = []

    
    def specs(self):
        
        #NOTE comp ('owns a')
        if self.cpu_model is not None:
            self.cpu = CPU(self.cpu_model)
            self.spec_list.append(f"{self.cpu.model} CPU")
        
        if self.ram_gb is not None:
            self.ram = RAM(self.ram_gb) 
            self.spec_list.append(f"{self.ram.size_gb}GB RAM")
            
        return ", ".join(self.spec_list)
    
    
    
    
    # NOTE - DONE
    
    # device is an object, we get this from aggregation NOT comp so if we loose computer still will work 
    def plug_in(self, device):
        
        # if string not in list, add string into list 
        if device not in self.device_list:
            self.device_list.append(device.name) 
        
        # if device already plugged in 
        else:
            return False 
    
    def unplug(self, device):
    
        # if device is not plugged in 
        if device.name not in self.device_list:
            return False 
        
        # remove device string from device list 
        else:            
            self.device_list.remove(device.name)
            return True
            
    # just return the device list array 
    def devices(self):
        return self.device_list 
    
    

    
pc = Computer("i7", 16)
mouse = Peripheral("Mouse")
kb = Peripheral("Keyboard")
print(pc.specs())
pc.plug_in(mouse)
pc.plug_in(kb)
print(pc.devices())
print(pc.unplug(mouse))
print(pc.unplug(mouse))
print(pc.devices())
del pc
print(kb.name)


# output 
# i7 CPU, 16GB RAM
# ['Mouse', 'Keyboard']
# True
# False
# ['Keyboard']
# Keyboard