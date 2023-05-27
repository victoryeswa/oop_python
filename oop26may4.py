class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity=0):
        #Run validations to the received arguments
        assert price >= 0, f'Price {price} is nt greater than or equal to zero!'
        assert quantity >= 0, f'quantity {quantity} is not greater or equal to zero!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item('Phone', 100, 1)
item1.apply_discount()
print(item1.price)

item2 = Item('LAptop', 400, 3)
item2.pay_rate = 0.5
item2.apply_discount()
print(item2.price)
