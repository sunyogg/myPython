# Public member:
# Public member can be accessed from anywhere, as the name suggest they are
# public. They can be accessed inside  and outside of a class and also inside
# any base class.

# Protected member: 
# Protected member can be accessed inside of a class or inside of any subclass 
# however they can also be accessed outside of the class but it is 
# customary to not access the protected member outside of the class.
# So can we say protected member are nothing but public member in python?

# Private member:
# Private member can only be accessed inside of the class, if we try to access
# private members outside of the class or inside any base class, then it'll
# throw an error telling that member is not defined.

# Python doesn't really have data hiding or private member aren't actually
# private read more about them in your bookmarks in stackoverflow.

class Employee:

    def __init__(self, name ,salary, project):
        self.name = name # public member - anywhere
        self._project = project # protected member - class and subclass
        self.__salary = salary # private member - within class

    def show(self):
        print('{} {} {}'.format(self.name, self._project, self.__salary))
'''


emp = Employee('john', 60000, 'Backend') 

print(emp.name)
print('\n\n')
#print(emp._project)
#print('\n\n')
# See how we cannot access salary attribute since it can only be accessed
# inside a class

print(emp.__salary)
# Using name mangling
print(emp._Employee__salary)
# instance._Class__private

# private member can be accessed using method.
#emp.show()
'''
# -----------------------------------------------------------------------------------------------
# Getters and Setters.

class Employee:

    def __init__(self, name ,salary, project):
        self.name = name # public member - anywhere
        self._project = project # protected member - class and subclass
        self.__salary = salary # private member - within class

    def show(self):
        print('{} {} {}'.format(self.name, self._project, self.__salary))

    def get_salary(self):
        """The getter method will access the value of private memeber."""
        print(self.__salary)

    def set_salary(self, salary):
        """This setter method will modify the value of private member."""
        self.__salary = salary
        print("Value of private member modified.")


emp = Employee('john', 60000, 'Backend')

# retrieving private member using getter.
emp.get_salary()
# modifying private variable using setter.
emp.set_salary(80000)
emp.get_salary()
print(emp.__salary)

# -----------------------------------------------------------------------------------------------




