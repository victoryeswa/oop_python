#object oriented programming
def hello():
    print('hello')

x = 1
print(type(x))
print(type(hello))

#cooomon errors
x = 1
y = 'hello'
#print(x+y) cannot add diferent variables

x = 1
y = 2
z = x+y
print(z)
# same int type

string = 'hello'
print(string.upper())

#example1
class Dog:

    def __init__(self):
        pass

    def add_one(self, x):
        return x + 1

    def bark(self):
        print('bark')

d = Dog()
d.bark()
print(d.add_one(5))
print(type(d))

#example 2

class Dog:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

d = Dog('Tim',25) #to practise, fix this issue
print(d.get_name())
d2 = Dog('Bill',36)
print(d2.get_name())
print(d.name,d.age)
# also
class Dog:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
d = Dog('Tim')    
print(d.get_name())  
d2 = Dog('Bill')
print(d2.get_name())  

#setting age
class Dog:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age

d = Dog('Tim',25) #to practise, fix this issue
d.set_age(23)
print(d.age,d.name)

























