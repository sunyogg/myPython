'''class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

print(emp1)
print(emp2)

# See how we are creating data of each employ manually.
emp1.first = 'corey'
emp1.last = 'bryan'
emp1.pay  = 50000
emp1.email = 'coreybryan@company.com'

emp2.first = 'terry'
emp2.last = 'stuart'
emp2.pay  = 70000
    def __init__(self,first,last,age,pay,experience,location):
        """Initializ the attributes that every employes has."""
        self.first = first.title()
        self.last = last.title()
        self.age = age
        self.pay = pay
        self.experience = experience
        self.location = location.title()
        self.fullname = self.first + " " + self.last
    

    def describe_emp(self):
        """This method will describe the employee."""
        print(f"\nHere are the details of employee {self.first} : ")
        print(f"Full name = {self.fullname}")
        print(f"Age  = {self.age}")
        print(f"Pay = {self.pay}$")
        print(f"Experience = {self.experience} year(s)")
        print(f"Location = {self.location}")


    def eligibility(self):
        """This method will check if the employee is eligible to vote."""
        if self.age >= 22:
            print(f"\n{self.fullname} is eligible to vote in the office affairs.")
        else:
            print(f"\n{self.fullname} is not eligible to vote in the office affairs.")


    def check_level(self):
        """This method will check the level of an employee."""
        if 1 <= self.experience <= 3:
            print(f"\n{self.first} is a Bronze member!")
        if 4 <= self.experience <= 6:
            print(f"\n{self.first} is a Silver member!")
        if 7 <= self.experience <= 10:
            print(f"\n{self.first} is a Gold member!")
        if 11 <= self.experience <= 15:
            print(f"\n{self.first} is a Diamond member!")
        if 16 <= self.experience <= 20:
            print(f"\n{self.first} is a Platinum member!")
        if self.experience > 20:
            print(f"\n{self.first} is a Rhodium member!")



# creating instances/objects emp1 and emp2 and emp3 and emp4
emp1 = Employee('larry','branson',38,60000,8,'california')
emp2 = Employee('rich','bryan',45,120000,11,'silicon valley')
emp3 = Employee('terry','brown',19,30000,1,'texas')
emp4 = Employee('hudson','stell',78,300000,30,'new york')


# see how all the instances are unique and stored at different locations. 
print(emp1) 
print(emp2)
print(emp3)
print(emp4)

# accessing attributes of certain instance
print(emp1.fullname)
print(emp2.age)
print(emp3.experience)
print(emp4.pay)

# calling a method for a particular instance or object
emp1.describe_emp()
emp2.describe_emp()
emp3.describe_emp()
emp4.describe_emp()

emp1.eligibility()
emp2.eligibility()
emp3.eligibility()
emp4.eligibility()

emp1.check_level()
emp2.check_level()
emp3.check_level()
emp4.check_level()

# --------------------------------------------------------------------------------------------------

class Car:
    """This class will create cars of different attributes."""

    def __init__(self,make,model,type,year,color):
        """Initialize attributes to describe car."""
        self.make = make.title()
        self.model = model.title()
        self.type = type.title()
        self.odometer = 0
        self.year = year
        self.color = color.title()

    
    def describe_car(self):
        """This method will describe the car."""
        print(f"\nFollowing are the details of the {self.make} {self.model}: ")
        print(f'Manufacturer: {self.make}')
        print(f"Model: {self.model}")
        print(f"Type: {self.type}")
        print(f"Odometer reading: {self.odometer}")
        print(f"Year of Launch: {self.year}")
        print(f"Color: {self.color}")

    
    def read_odometer(self):
        """This method will read the odometer reading"""
        print(f"\nThe cars has {self.odometer} miles on it.")


    def increment_odometer(self,miles):
        """This method will increment the reading of odometer."""
        self.miles = miles
        if self.miles >= 0:
            self.odometer += self.miles
            print(f"\nThe car now has {self.odometer} miles on it.")
        else:
            print("You can't decrease the odometer reading of the car.")


    def update_odometer(self,miles):
        """This method will update the reading of odometer."""
        self.miles = miles
        if self.miles >= self.odometer:
            self.odometer = self.miles
            print(f"\nThe car now has {self.odometer} miles on it.")
        else:
            print("You can't decrease the odometer reading of the car.")


    def fill_gastank(self,litres):
        """This method will fill fuel in the car after checking its type."""
        types = ['diesel','petrol']
        if self.type.lower() in types:
            print(f"Filled {litres} litres of fuel in the tank ")
        if self.type.lower() == "electric":
            print(f"You can't fill gas on an electric vehicle.")

    
# creating instances
vec1 = Car('audi','r8','diesel',2018,'black')
vec2 = Car('tesla','model s','electric',2019,'red')


# accessing attributes
print(vec1.type)
print(vec2.type)


# calling methods
vec1.describe_car()
vec2.describe_car()

vec1.read_odometer()
vec1.increment_odometer(10)
vec1.update_odometer(400)
vec1.increment_odometer(-10)
vec1.update_odometer(300)

vec1.fill_gastank(5)
vec2.fill_gastank(5)


# modifying attributes of an instance
vec2.type = 'diesel'
print(vec2.type)
vec2.fill_gastank(20)
vec2.type = 'electric'
print(vec2.type)
vec2.fill_gastank(20)

# --------------------------------------------------------------------------------------------------
class Battery:
    def __init__(self,battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"It has {self.battery_size} kwh battery. ")


# 1
batt = Battery()
batt.describe_battery()

#2
Battery().describe_battery()

# Both case 1 and case 2 are same written in a different manner.

#-----------------------------------------------------------------------------------------------------

# creating parent class

class Car:
    """Attempt to make a car."""


    def __init__(self,make,model,year,typee,color):
        """Initialize the attributes of the car"""
        self.make =  make.title()
        self.model = model.title()
        self.year = year
        self.typee = typee.title()
        self.color = color.title()
        self.odometer = 0


    def describe_car(self):
        """This method will describe the car"""
        print(f"\nFollowing are the deatails of the {self.make} {self.model}: ")
        print(f"-> Manufacturer: {self.make}")
        print(f"-> Model: {self.model}")
        print(f"-> Type: {self.typee}")
        print(f"-> Year of launch: {self.year}")
        print(f"-> Color: {self.color}")


    def read_odometer(self):
        """This method will read the odometer reading"""
        print(f"The car has {self.odometer} miles on it.")


    def increment_odometer(self,miles):
        """This method will increment the odometer reading"""
        if miles < 0:
            print("You can't roll back the odometer reading.")
        else:
            self.odometer += miles

    
    def update_odometer(self,miles):
        if miles < self.odometer:
            print("You can't roll back the odometer reading.")
        else:
            self.odometer = miles

    
    def fill_gastank(self,litres):
        """This method will fill fuel in the car after checking its type."""
        print(f"Filled {litres} litres of fuel in the tank. ")


# making child class

class Electric_car(Car):
    """A child class out of Car for electric car."""
    

    def __init__(self,make,model,year,typee,color,charging_time):
        super().__init__(make,model,year,typee,color)             
        self.charging_time = charging_time

        self.battery_size = 75                   

# see how charging_time is not in super method but only __init__() method of 
# Electric_car class and hence describe method will have one more parameter
# 'charging_time' in describe_car() method for electric car but not in normal Car


# if you want to specify 'charging_time' manually you can put charging_time as an
# argument in __init__() method, or if you want to specify the default value you
# and you don't type it's 'charging_time' everytime you create a new instance
# then you can write charging time inside the __init__() like we did with
# self.battery_size.

# error: TypeError: Car.__init__() takes 5 positional arguments but 6 were given
# soln:  You don't need to pass self in the super method


    def describe_car(self):
        super().describe_car()
        print(f"-> Charging Time: {self.charging_time} hrs")

# remember the use of super function is to copy all the attributes of a method of 
# a parent class to child class, therefore we can only use super()in __init__ but 
# also in any other function, if it needed to be changed just a little bit.


    def describe_battery(self):
        """This method will describe the battery of an electric car"""
        print(f"This car has {self.battery_size} kwh battery on it.")


    def fill_gastank():
        print("You can't fill gas on an electric car. Please charge it.")



car1 = Car('audi','r8',2018,'diesel','black')
electric1 = Electric_car('tesla','model s',2019,'electric','white',6)


car1.describe_car()
electric1.describe_car()

#-----------------------------------------------------------------------------------------------------

class Car:

    def __init__(self,make,model,year):
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.odometer = 0


    def describe_car(self):
        print(f"\nManufacturer: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year of Launch: {self.year}\n")


    def read_odometer(self):
        print(f"The car has {self.odometer} miles on it.")


    def increment_odometer(self,miles):
        if miles < 0:
            print("You can't roll back the reading of an odometer.")
        else:
            self.odometer += miles


    def update_odometer(self,miles):
        if miles < self.odometer():
            print("You can't roll back the reading of an odometer.")
        else:
            self.odometer = miles


    def fill_gas(self):
        print("Okay we'll now fill the gas tank, please mention the amount.")
    


class Battery:


    def __init__(self,battery_size = 75):
        self.battery_size = battery_size


    def describe_battery(self):
        print(f"The car has {self.battery_size} kwh battery on it.")


    def charge_battery(self):
        print("Charging! We'll let you know when it's fully charged.")


    def get_range(self):
        if 50 < self.battery_size < 80:
            rangee = 200
        if 80 < self.battery_size < 150:
            rangee = 300
        if 150 < self.battery_size < 250:
            rangee = 500
        if 150 < self.battery_size < 250:
            rangee = 1000
        print(f"The range of car is {rangee}km.")

        



class Electric_car(Car):

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery(95)


    def fill_gas(self):
        print("You can't fill gas on an electric car. Please charge it.")


electric1 = Electric_car('tesla','model l',2020)

electric1.describe_car()


electric1.battery.describe_battery()
electric1.battery.get_range()
electric1.battery.charge_battery()

# This line tells Python to look at the instance electric1, find its battery 
# attribute, and call the method describe_battery() that's associated with the 
# Battery instance stored in the attribute.


#-----------------------------------------------------------------------------------------------------
# IMPORTING CLASSES

# proggram 1.0.1

# importing a single class
from carclassmodule import Car

car1 = Car('audi','r8',2019)

car1.describe_car()
car1.read_odometer()
car1.fill_gas()



# importing a single class and giving them an alias
from electricclassmodule import Electric_car as ec

electric1 = ec('tesla','model l',2020)
electric1.describe_car()
electric1.battery.describe_battery()
electric1.battery.get_range()


# importing multiple classes from a module
from carclassmodule import Car
from electricclassmodule import Electric_car

car2 = Car('bmw','gallardo',2017)
electric2 = Electric_car('tesla','model a',2015)

car2.describe_car()
electric2.describe_car()
car2.fill_gas()
electric2.fill_gas()
electric2.battery.describe_battery()


# Importing an entire module
import carclassmodule as cm
import electricclassmodule as ec

car3 = cm.Car('tata','nano',2012)
electric3 = ec.Electric_car('ola','qube',2021)

car3.describe_car()
electric3.describe_car()
electric3.battery.get_range()


# importing an entire module

from carclassmodule import *
from electricclassmodule import *

car4 = Car('audi','r7',2012)
electric4 = Electric_car('tesla','model n',2013)

car4.describe_car()
electric4.battery.describe_battery()

#--------------------------------------------------------------------------------------------------
'''
# Python standart library
# using randint and choice from random module
from random import randint,choice

def random(int1,int2):
    for i in range(10):
        x = randint(int1,int2)
        print("->",x)


names = ('tom','yuvone','jerry','stuart','linus','stephen','smith')

print(choice(names))

random(1,2)

#--------------------------------------------------------------------------------------------------
from random import randint
class RollDice:

    def __init__(self,side = 6):
        self.side = side


    def roll_dice(self,time):
            for i in range(time):
                x = randint(1,self.side)
                print(f"-> {x}")


dice610 = RollDice(6)
dice610.roll_dice(15)


    







