 
'''
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first.lower() + '.' + self.last.lower() + '@company.com'
        self.pay = pay


    def fullname(self):
        print('{} {}'.format(self.first.title(), self.last.title()))


    def raise_pay(self):
        self.pay = (self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10


dev1 = Developer('sunyog', 'lodhi', 60000)
# the method resolution order
#    - child
#    - parent
#    - builtins
emp1 = Employee('sheero', 'korosuke', 40000)
    
print(dev1.pay)
dev1.raise_pay()
print(dev1.pay)

print('\n\n')

print(emp1.pay)
emp1.raise_pay()
print(emp1.pay)
'''
# ------------------------------------------------------------------------------------------------------------
# We should never pass mutable data types like list, dictionaries
# as default arguments.
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first.lower() + '.' + self.last.lower() + '@company.com'
        self.pay = pay


    def fullname(self):
        return ('{} {}'.format(self.first.title(), self.last.title()))


    def raise_pay(self):
        self.pay = (self.pay * self.raise_amt)


class Developer(Employee):
    
    def __init__(self, first, last, pay , programming_lang):
        super().__init__(first, last, pay)
        self.programming_lang = programming_lang
    #   Employee.__init__(self, first, last, pay)


class Manager(Employee):

    def __init__(self, first, last, pay ,employees=None):
        # Don't know why but i am having difficulty understanding this code.
        super().__init__(first, last, pay)
        if employees == None :
            self.employees = []
        else:
            self.employees = (employees) # do you think i should enclose employees with list()


    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp) 

    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp) 


    def print_emps(self):
        print('Employees under supervision: ')
        for emp in self.employees:
            print('-->', emp.fullname())


dev1 = Developer('corey', 'schafer', 70000, 'python')
dev2 = Developer('steven', 'murphy', 60000, 'java')



mgr1 = Manager('sue', 'smith', 120000, [dev1])
mgr1.add_emp(dev2)

(mgr1.print_emps())

# ------------------------------------------------------------------------------------------------------------







'''
print(dev1.programming_lang)
print(dev1.email)

'''























# print(help(Developer)) 