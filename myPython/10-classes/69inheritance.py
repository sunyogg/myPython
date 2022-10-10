# 1) 

# creating Parent class
class Car:
    '''A simple attempt to represent a car'''
    

    def __init__(self,manufacturer,model,year):
        '''Initialize attributes to describe a car'''
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer = 0
    

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

# - - - - - - - - - - - - - - - - - - - - - - - - -

# creating a Child class

class ElectricCar(Car):

    def __init__(self,manufacturer,model,year):
        super().__init__(manufacturer,model,year)

        '''Here we defined an __init__() function for the child class and using super()
           function we tell python to call __init__() method from the parent class,
           which will  give an ElectricCar instance all the attributes defined in that
           __init__() method. After doing all this we can now initialize attributes
           that are specific to child class. '''

        #an attribute specific to child class
        self.battery = 60 # using instance of different class as attributes
                          # for another class


    # defining a method specific to child class
    def describe_battery(self):
        print(f"The size of battery of {self.manufacturer} {self.model} is {self.battery} KWH.")

    # overiding method from parent class
    def fill_gas_tank(self):
        print("You can't fill gas in an electric car. It runs on battery.")

# creating an instance using the child class
mytesla = ElectricCar('Tesla','model s',2019)

#using a method defined for parent class in child class
mytesla.get_descriptive_name()
mytesla.describe_battery()
mytesla.fill_gas_tank()

#------------------------------------------------------------------------------------------------------

# 2)

#Instances as attributes

# creating Parent class
class Car:
    '''A simple attempt to represent a car'''
    

    def __init__(self,manufacturer,model,year):
        '''Initialize attributes to describe a car'''
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer = 0
    

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

#- - - - - - - - - - - - - - - - - - - - - - - -

# creating a separate class for battery
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

# - - - - - - - - - - - - - - - - - - - - - - - - -

# creating a Child class

class ElectricCar(Car):

    def __init__(self,manufacturer,model,year):
        super().__init__(manufacturer,model,year)

        #an attribute specific to child class
        self.battery = Battery() # using instance of different class as attributes for another class
                                 # so here we created an instance from Battery() and 
                                 # stored it in self.battery, now whenever we wil call
                                 # self.battery, we will need to specify the method
                                 # we want to call from Battery() class, separated by
                                 # a dot. electrictesla.battery.describe_battery()


    # overiding method from parent class
    def fill_gas_tank(self):
        print("You can't fill gas in an electric car. It runs on battery.")

# creating an instance using the child class
electrictesla = ElectricCar('Tesla','model s',2019)

electrictesla.battery.describe_battery()
electrictesla.battery.get_range()

#------------------------------------------------------------------------------------------------------

class Battery:
    def __init__(self,battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"It has {self.battery_size} kwh battery. ")


# 1
batt = Battery(95)
batt.describe_battery()

#2
Battery().describe_battery()

# Both case 1 and case 2 are same written in a different manner.

#------------------------------------------------------------------------------------------------------






