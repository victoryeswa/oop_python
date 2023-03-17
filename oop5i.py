class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_1)

emp_1.first = 'Corey'
emp_1.last = 'Schofer'
emp_1.email = 'carey.schafer@company.com'
emp_1.pay = 60000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'test.user@company.com'
emp_2.pay = 50000



print(emp_1.email)
print(emp_2.email)