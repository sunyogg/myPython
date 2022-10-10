# This module only contains Car class


# a class Car in  module caralone.py to represent any car

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
