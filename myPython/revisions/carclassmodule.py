
# for program 1.0.1
class Car:
    """Attempt to make a car"""

    def __init__(self,make,model,year):
        """Initialize the atttributes"""
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.odometer = 0


    def describe_car(self):
        """This method will describe the car."""
        print(f"\nManufacturer: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year of Launch: {self.year}\n")


    def read_odometer(self):
        """This method will read the odometer reading."""
        print(f"The car has {self.odometer} miles on it.")


    def increment_odometer(self,miles):
        """This method will increment the odometer reading"""
        if miles < 0:
            print("You can't roll back the reading of an odometer.")
        else:
            self.odometer += miles


    def update_odometer(self,miles):
        """This method will update the odometer reading."""
        if miles < self.odometer():
            print("You can't roll back the reading of an odometer.")
        else:
            self.odometer = miles


    def fill_gas(self):
        """This method will fill the gas tank."""
        print("Okay we'll now fill the gas tank, please mention the amount.")