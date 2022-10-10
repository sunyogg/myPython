# dunder method
# magic method
# method having double underscore on both side.
# 'a  +b' will call __add__(a, b) 
# You can define a dunder method inside a class to alter their functionality
# or to make them behave accordingly.


class Employee:

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first+'.'+self.last+'@company.com'
        self.pay = pay

    def fullname(self):
        return ('{} {}'.format(self.first.title(), self.last.title()))

    def __add__(self, other):
        # self -> left side of the addition
        # other -> right side of the addition
        # print(emp1.pay + emp2.pay)
        return (self.pay + other.pay)

    def __len__(self):
        # print(len(emp1.fullname()))
        x = self.fullname()
        return len(x)


    def apply_raise(self):
        self.pay = (self.pay * Employee.raise_amt)
        

emp1 = Employee('corey', 'schafer', 60000)
emp2 = Employee('test', 'user', 40000)


print(emp1 + emp2)
#print(emp2 + emp1) 
# emp1.apply_raise()
# print(emp1 + emp2)

print(len(emp1))
# ------------------------------------------------------------------------------------------