

class OrderLine():

    def __init__(self, name, price, quanity):
        self.name = name 
        self.price = price 
        self.quanity = quanity 


    def subtotal(self):
        return self.price * self.quanity



class Order():
    def __init__(self):
        self.lines = {}

    def add_item(self, name, price, quanity):

        if name not in self.lines:
            # name : object
            self.lines[name] = OrderLine(name, price, quanity)

        else:
            self.lines[name].quanity += quanity



    def item_count(self):
        return len(self.lines) 



    def total(self):

        total = 0 

        # items are objects
        for name, line in self.lines.items():
            total += line.subtotal()


        return total 




o = Order()
o.add_item("pen", 1.5, 2)
o.add_item("book", 10, 1)
o.add_item("pen", 1.5, 3)
print(o.item_count())
print(o.lines["pen"].quanity)
print(o.total())


# 2
# 5
# 17.5