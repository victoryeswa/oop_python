#constructor
#create a method withon a class
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last+'@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'
emp_1 = Employee('Carey', 'Schufer', 5000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.pay, 'pay')
print(emp_2.email, 'email')

print(emp_2.fullname())

print(Employee.fullname(emp_1))



