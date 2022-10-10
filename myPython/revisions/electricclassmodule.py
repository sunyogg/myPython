
from carclassmodule import Car

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
