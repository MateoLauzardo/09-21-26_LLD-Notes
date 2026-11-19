
class Account():
    
    def __init__(self, balance):
        self.balance = balance
        
    def withdraw(self, amount):
        
        if amount < self.balance:
            self.balance -= amount 
            return True
        else:
            return False 
        


class CheckingAccount(Account):
    
    def __init__(self, balance, overdraft_limit):
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    # not goingto call super cuz this is overriding 
    def withdraw(self, amount):
        
        updated_balance = self.balance - amount 
        
            # -40                # 
        if updated_balance < -self.overdraft_limit:
            return False 
        
        else:
            self.balance = updated_balance
            return True


c = CheckingAccount(100, overdraft_limit=50)


print(c.withdraw(140))
print(c.balance)
print(c.withdraw(20))

