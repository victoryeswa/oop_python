class Item:
    pay_rate = 0.8

    def __init__(self, name:str, price: float, quantity=0):
        #run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater than or equal to zero.'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero'

        #assign to self
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
print(Item.all)
