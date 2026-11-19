
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
        


class CheckingAccount(Account):
    
    def __init__(self, balance, overdraft_limit):
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    # not goingto call super cuz this is overriding 
    def withdraw(self, amount):
        
        updated_balance = self.balance - amount 
        

        if updated_balance < -self.overdraft_limit:
            return False 
        
        else:
            self.balance = updated_balance
            return True
    
    
s = SavingsAccount(100)
print(s.withdraw(10))
s.withdraw(10)
s.withdraw(10)
print(s.withdraw(10))
print(s.balance)

c = CheckingAccount(100, overdraft_limit=50)
print(c.withdraw(140))
print(c.balance)
print(c.withdraw(20))


#output 
# True
# False
# 70

# True
# -40
# False