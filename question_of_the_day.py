
# Question 5: Abstract Base Classes as Contracts

from abc import ABC, abstractclassmethod




# NOTE - DONE
class PaymentMethod(ABC):
    
    @abstractclassmethod
    def name(self):
        pass
    
    @abstractclassmethod
    def pay(self, amount):
        pass 
    
    @abstractclassmethod
    def checkout(self, amount):
        pass 
    
    
    
# NOTE - DONE    
class CreditCard(PaymentMethod):
    
    def __init__(self, limit):
        self.limit = limit 
        self.money_spent = 0
         
    def name(self):
        return "Credit Card" 
    
    def pay(self, amount):
        
        self.money_spent += amount 
        
        if self.money_spent > self.limit:
            return False 
        else: 
            return True 
    
    def checkout(self, amount):
        
        if self.pay(amount) == False:
            return f"Payment failed"
        else:
            return f"Paid {amount} with {self.name()}"    
    
    
# NOTE - DONE 
class GiftCard(PaymentMethod):
    
    def __init__(self, balance):
        self.balance = balance
        self.total_money_spent = 0
        
    def name(self):
        return "GiftCard" 
        
    def pay(self, amount):
        
        self.total_money_spent += amount
        
        if self.total_money_spent < self.balance:
            return True 
        else:
            return False 
        
    def checkout(self, amount):
        
        if self.pay(amount) == False:
            return f"Payment failed"
        else:
            return f"Paid {amount} with {self.name()}"
    
    


cc = CreditCard(500)
gc = GiftCard(50)
print(cc.checkout(200))
print(cc.checkout(400))
print(gc.checkout(30))
print(gc.checkout(30))

class Broken(PaymentMethod):
    def name(self):
        return "Broken"

try:
    b = Broken()
except TypeError:
    print("Cannot create Broken")
    
    
    
# output 
# Paid 200 with Credit Card
# Payment failed
# Paid 30 with Gift Card
# Payment failed
# Cannot create Broken