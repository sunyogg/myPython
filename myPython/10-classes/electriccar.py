
# This module contains ElectricCar and Battery class

''' a set of classes that can be used to represent an electric car'''

from caralone import Car

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
