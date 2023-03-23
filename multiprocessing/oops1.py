class Item:
    pass
    #def calculate_total_price(self, name, price, quantity):
     #   self.name = name
     #   self.price = price
     #   self.quantity = quantity

#instances of the above class
item1= Item()
item1.name = 'Laptop'
item1.price = 1000
item1.quantity = 3

print(type(item1)) #item
print(type(item1.name)) #str
print(type(item1.price)) #int
print(type(item1.quantity)) #int
item1.calculate_total_price()

#random_str = 'aaa'
#print(random_str.upper())
