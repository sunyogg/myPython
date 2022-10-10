   
# This module contains Car, ElectricCar, and Battery class

# a class Car in  module car.py to represent any car

class Car: 
    '''A simple attempt to represent a car'''
    

    def __init__(self,manufacturer,model,year):
        '''Initialize attributes to describe a car'''
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer = 0  # Defaul odometer reading
        # this attribute is not passed as parameter in __init__.
        # maybe because it's common for all instances.
    

    # method return descriptive name
    def get_descriptive_name(self):
        '''This method will describe attributes of the car'''
        '''Return a neatly formatted descriptive name'''
        long_name = (f"{self.year} {self.manufacturer} {self.model}")
        print(long_name.title())
    

    # method read odometer reading
    def read_odometer(self):
        '''This method will read the reading of odometer'''
        print(f"The car has {self.odometer} miles on it.")


    # method update odometer reading
    def update_odometer(self,mileage):
        '''This method will update the reading of odometer'''
        if mileage < self.odometer:
            print(("You can't roll back an odometer."))
        else:
            self.odometer = mileage


    # method increment odometer reading
    def increment_odometer(self,mileage):
        '''This method will increment the existing value of odometer'''
        if mileage < 0:
            print("You can't roll back an odometer.")
        else:
            self.odometer += mileage

    # method to fill gas tank
    def fill_gas_tank(self):
        print("Okay how much gas you wanna fill in the tank?")



class Battery:
    def __init__(self,battery_size = 100):
        # used default value in parameter of __init__ method
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}KWH battery")

    def get_range(self):
        if self.battery_size == 75:
            range = 250
        
        if self.battery_size == 100:
            range = 350
        print("This car can go upto",range,"on full charge. ")

    
    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100

        elif self.battery_size >= 100:
            print("No need to upgrade battery.")



class ElectricCar(Car):

    def __init__(self,manufacturer,model,year):
        super().__init__(manufacturer,model,year)

        #an attribute specific to child class
        self.battery = Battery(75)


    # overiding method from parent class
    def fill_gas_tank(self):
        print("You can't fill gas in an electric car. It runs on battery.")