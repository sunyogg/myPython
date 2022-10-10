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
        
        # Attributes can be defined without being passed in as parameters. These 
        # attributes can be defined in the __**init__**() method, where they are 
        # assigned a default value. And hence the value of that attribute for 
        # every instances will be same i.e. odometer reading of every car will 
        # be zero. If you want to specify different odometer reading for different 
        # car then you have to pass odometer as a parameter in the __init__() 
        # method.
    

    # This method will describe attributes of the car
    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name'''
        long_name = (f"{self.year} {self.manufacturer} {self.model}")
        print(long_name.title())
    

    # This method will read the reading of odometer
    def read_odometer(self):
        print(f"The car has {self.odometer} miles on it.")


    # This method will update the reading of odometer
    def update_odometer(self,mileage):
        if mileage < self.odometer:
            print(("You can't roll back an odometer."))

        else:
            self.odometer = mileage

    # This method will increment the existing value of odometer
    def increment_odometer(self,mileage):
        """add the given amount to the odometer"""
        if mileage < 0:
            print("You can't roll back an odometer.")
        else:
            self.odometer += mileage


# creating an instance of Car
my_car = Car('audi','r8',2019)
my_car.get_descriptive_name()


# modifying an attribute value directly
my_car.odometer = 500
my_car.read_odometer()

# modifying an attribute value using a method
my_car.update_odometer(800)
my_car.read_odometer()

# incrementing an attribute value using a method
my_car.increment_odometer(200)
my_car.read_odometer()




