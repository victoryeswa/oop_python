class Item:
    pay_rate = 0.8 # the pay rate after 20% discount
    def __init__(self, name, price, quantity=0):
        assert price >= 0, f'Price {price} is not greater than or equal to zero'
        assert quantity >=0, f'Quantity {quantity} i not greater than or equal to zero'

        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate




item1 = Item('Phone', 800, 5)
item2 = Item('laptop', 1000, 3)

#print(Item.pay_rate)
#print(item1.pay_rate)
print(item2.pay_rate)

print(Item.__dict__)
print(item1.__dict__)
print(item1.calculate_total_price())
print(item2.calculate_total_price())
#item2.has_numpad = False
item1.apply_discount()
print(item1.price)


# incase you want to asssign a specific pay rate
item2 = Item('Laptop', 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

#print(item2.name, item2.price, item2.quantity)
#print(item1.name, item2.price, item1.quantity)




    
        

    
#hardcoding
#item1 = Item()
#item1.name = 'Phone'
#item1.price = 100
#item1.quantity = 5

#item2 = Item()
#item2.name = 'Laptop'
#tem2.price = 1000
#item2.quantity = 3

