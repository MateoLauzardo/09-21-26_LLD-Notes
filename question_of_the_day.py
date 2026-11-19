
class Account():
    
    def __init__(self, balance):
        self.balance = balance
        
    def withdraw(self, amount):
        
        if amount < self.balance:
            self.balance -= amount 
            return True
        else:
            return False 
        
        
class SavingsAccount(Account):
    def __init__(self, balance):
        self.balance = balance
        self.count = 0 
    
    
    def withdraw(self, amount):
        
        if self.count >= 3:
            return False 
        
        else:
            answer = super().withdraw(amount)
            
            if answer == True:
                self.count += 1
                
        return answer 
        

