
class Employee:
	"""A class that will manage general data of an employee."""
	# making a class variable.
	raise_amount = 1.04
	num_of_emps = 0
	

	def __init__(self, first, last, pay):
		"""Initialize the attributes for class Employee."""
		self.first = first
		self.last = last
		self.pay = pay
		self.email = self.first + self.last + "@company.com"
		# a defalt instance variable
		self.behaviour = 'Good'
		Employee.num_of_emps += 1


	def fullname(self):
		"""This method will print fullname of an empoyee"""
		x = '{} {}'.format(self.first, self.last)
		return x

	def increment_pay(self):
		"""This method will increase the pay of employs"""
		self.pay = int(self.pay * Employee.raise_amount)


# creating an instance emp_1 of class Employee = Instantiating
emp_1 = Employee('corey','schafer',50000)
emp_2 = Employee('dan','houser', 80000)

print(Employee.__dict__)
print(emp_1.__dict__)

emp_1.raise_amount = 1.08

print(Employee.__dict__)
print(emp_1.__dict__)

print(emp_2.raise_amount)
# When we try to access an attribute on an instance it will first
# check if the instance contains that attribute and if it doesn't 
# then it will see if the class or any class that it inherits from
# contains that attributes.
# so here when we want to access the attribute raise_amount for an
# instance emp_2, it first checks if the instance contain that 
# attribute and if not then it will check in class Employee.
# so when we access raise_amount from our instances here, they 
# don't actually have attribute for themselves, they are accessing
# the classes raise_amount attribute.

(emp_2.num_of_emps) = 3










'''
#print(emp_1.fullname())
#Employee.fullname(emp_1)

print(Employee.__dict__)
print('')
print(emp_1.__dict__)
print('')
# You can see how the value of variable raise_pay is same for every
# instance of a class. 
print(emp_1.raise_pay)
print(emp_2.raise_pay)
print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.__dict__)

# This will change the value of raise_pay for each and every 
# instance of a class
Employee.raise_pay = 1.06
print(Employee.raise_pay)
print(emp_1.raise_pay)
print(emp_2.raise_pay)

# You can modify a class variable for a particular instance by:
emp_1.raise_pay = 1.05
print(Employee.raise_pay)
print(emp_1.raise_pay)
print(emp_2.raise_pay)

print('---------------------------------------------------------')
# see how class variable is only stored in dictionary of
# class Employee
print(Employee.__dict__)
print('')
# There is no variable as raise_pay in emp_1 or emp_2
print(emp_1.__dict__)
print(emp_2.__dict__)
print('')
# see how to class variable differs as we have changed the value 
# of class variable for emp_1
print(emp_1.raise_pay)
print(emp_2.raise_pay)

# Everything insde a __init__() method is a instance variable.
# and class variable are variable that are made when we store a 
# variable inside  a class, but not inside any method. Class variable
# are same to every instance or we can say every instace of a class
# shares the value of a class variable. We use the the __dict__ 
# function to check where each variable are stored, are they 
# stored inside a class? or are they stored inside an instance. 

print(emp_2.pay)
emp_2.increment_pay()
print(emp_2.pay)'''












# what will happen when you forget to use self in parameter of a
# function? Since we know that wheneven we call a method from 
# a class, it's instance is passed automatically as the first
# argument. So let's take example of method fullname, it does not 
# require any additional information to print the full name of an
# employee, so we don't need to use any parameter except self while
# defining that method. But let's say we forget to type self as the
# parameter. Now when we call method fullname on emp_1 instance
# the instance will be automatically passed as the first argument
# while calling that mehtod. But there are no parameter defined for
# the method and we are unknowingly passing instance as the first
# argument it's like:
# def fullname():
#   __snip__
# emp_1.fullname(emp_1)
# surely we are going to get an error saying: fullname takes 0
# argument but one was given.


# for class Employee:
# Instance emp_1 is passed automatically as argument whenever we 
# call a method so thats why we have to pass self as parameter in 
# every method. Each method within a class automatically take the 
# instance as the first argument So let's try to match parameter 
# with argument: self=emp_1, first=corey, last=schafer, pay=50000
# keep in mind we are not required to use self only, we can name
# that parameter anything but since the instance itself is
# passed as argument so for understanding we generally use self. 
# also words after self don't need to name of parameter they can
# be anything as well. Ex- self.fname = first
# When we create an instance the __init__ method runs automatically
# and it will set the values of attributes that we passed as 
# argument. so for example when we create an instance emp_1 from
# the class Employee, the __init__() method will run automatically
# value of parameter self will be passed as argument  emp_1, then
#  all other attirbutes will be set as follows:
# emp_1.first = 'corey'
# emp_1.last = 'schafer'
# emp_1.pay = 50000
# emp_1.email = corey + schafer + @company.com 


# for method fullname():
# Notice how in method full name we only passed as self as 
# parameter, because we don't need any additional info to run
# this method, when we call any method for a instance, that method
# will always have the access to the attributes of that instance.
# for example method full name will always have access to attributes
# of instance emp_1 like first, last, pay, email, you can check that
# by passing emp_1 in place of self.
# In the method fullname we are using self.first and self.last
# instead of emp_1.first and emp_1.last because we want the 
# method fullname to work with any instance and not only with 
# emp_1 instance.


# for calling a method:
# There are two ways to access a class's method for an instance
# the one above in which we don't pass any argument in the method
# call, because we have already specified that we want to call
# the method fullname() for emp_1 and the instance is automatically
# passed as argument in the method call, but on the other method 
# below we use class and then method separated by a dot, but now 
# since here we have not specified for what instance we want to 
# run that method for so we have to pass the instance as argument 
# inside the parenthesis. So that python will now know that we 
# want to call fullname method for emp_1 instance. We can also
# when we use the first method to call a method, it get's tranformed
# into something thats written below.

#print(emp_1.first)

#print('{} {}'.format(emp_1.first, emp_1.last))








'''
# Creating instances
emp_1 = Employee()
emp_2 = Employee()

emp_1.first = 'Corey'
emp_1.last = 'schafer'
emp_1.pay = 50000
emp_1.email = 'coreyschafer@company.com'

emp_2.first = 'test'
emp_2.last = 'user'
emp_2.pay = 60000
emp_2.email = 'testuser@company.com'

print(emp_1)
print(emp_2)

print(emp_1.first)
print(emp_2.last)'''


# Each method within a class automatically takes the instance as the argument.
# Everytime we call a method it automatically takes the instance as the argument.