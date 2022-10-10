# 9.6

# Parent class
class Restaurant:
    # created a class called restaurant

    #initializing attribues of the restraurant
    def __init__(self,name,cuisine):
        self.name = name.title()
        self.cuisine = cuisine.title()
        self.customer_served = 0


    # This method will describe the restaurant
    def describe_restaurant(self):
        print(f"\nThe name of restaurant is {self.name}. It's cuisine type is {self.cuisine}")
        print(f"It is a family and friends restauarnat.")
    

    # This method will tell the timing of restaurant
    def open_restaurant(self):
        print("The restaurant is open everyday from 9am to 10am.")
  

    # This method will read the amount of customer served
    def read_customer(self):
        print("customer served:",self.customer_served)


    # This method will let us set the number of customer served
    def set_number_served(self,served):
        if served < 0:
            print("Number of customer served can't be negative")
        else:
            self.customer_served = served


    # this method will increment the number of customer served
    def increment_customer_served(self,incremented):
        if incremented < 0:
            print("You can't decrease the number of customer served")
        else:
            self.customer_served += incremented



# creating child class

class IceCreamStand(Restaurant):

    # calling all the attributes of parent class to child class using super() method
    def __init__(self,name,cuisine):
        super().__init__(name,cuisine)

        #attribute specific to child class
        self.flavors = ['vanilla','strawberry','chocolate','elaichi','black forest']

    # instance specific to child class
    def list_icecream_flavors(self):
        for flavor in self.flavors:
            print(f"-> {flavor.title()}")
    

icee = IceCreamStand('IceCream parlor','Indian')

icee.list_icecream_flavors()

#----------------------------------------------------------------------------------------------------------------
# 9.7
class Users:
        '''creating a class called user'''


        '''initializing attributes'''
        def __init__(self,fname,lname,locality,nationality):
            self.first = fname.title()
            self.last = lname.title()
            self.locality = locality.title()
            self.nationality = nationality.title()
            self.login_attempts = 0


        # this method will describe the user
        def describe_user(self):
            print(f"\nfirst: {self.first}")
            print(f"last: {self.last}")
            print(f"locality: {self.locality}")
            print(f"nationality: {self.nationality}")

        
        # this method will greet user
        def greet_user(self):
            print(f"\nHello {self.first} {self.last}. How are you?")


        # this method will read number of login attempts
        def read_login_attempts(self):
            print(f"login_attempts: {self.login_attempts}")


        # this method will increment number login attempts by 1
        def increment_login_attempts(self):
            self.login_attempts += 1


        # this method will reset the number of login attempts
        def reset_login_attempts(self):
            self.login_attempts = 0

# creating a child class called Admin which inherits from parent class Users
class Admin(Users):
    
    # calling all the attributes of parent class to child class
    def __init__(self,fname,lname,locality,nationality):
        super().__init__(fname,lname,locality,nationality)

        # creating an attribute specific to child class
        self.privileges = [
            'can add post',
            'can delete post',
            'can add user',
            'can ban user',
            'can call a meeting',
            'can edit information',
            'can change UI'
        ]

        # defining a method specific to child class
    def show_privileges(self):
        for privilege in self.privileges:
            print(f"-> {privilege.title()}")


admin = Admin('sanyog','lodhi','jabalpur','indian')

admin.show_privileges()

#----------------------------------------------------------------------------------------------------------------

# 9.8
    
class Users:
        '''creating a class called user'''


        '''initializing attributes'''
        def __init__(self,fname,lname,locality,nationality):
            self.first = fname.title()
            self.last = lname.title()
            self.locality = locality.title()
            self.nationality = nationality.title()
            self.login_attempts = 0


        # this method will describe the user
        def describe_user(self):
            print(f"\nfirst: {self.first}")
            print(f"last: {self.last}")
            print(f"locality: {self.locality}")
            print(f"nationality: {self.nationality}")

        
        # this method will greet user
        def greet_user(self):
            print(f"\nHello {self.first} {self.last}. How are you?")


        # this method will read number of login attempts
        def read_login_attempts(self):
            print(f"login_attempts: {self.login_attempts}")


        # this method will increment number login attempts by 1
        def increment_login_attempts(self):
            self.login_attempts += 1


        # this method will reset the number of login attempts
        def reset_login_attempts(self):
            self.login_attempts = 0


# creating a separate class called privileges to keep all the privileges

class Privileges:

    def __init__(self):
        self.privilege = [
            'can add post',
            'can delete post',
            'can add user',
            'can ban user',
            'can call a meeting',
            'can edit information',
            'can change UI'
        ]
    
    def show_privileges(self):
        for privilege in self.privilege:
            print(f"-> {privilege.title()} ")


# creating a child class called Admin which inherits from parent class Users
class Admin(Users):
    
    # calling all the attributes of parent class to child class
    def __init__(self,fname,lname,locality,nationality):
        super().__init__(fname,lname,locality,nationality)

        self.privilege = Privileges()



admin1 = Admin('sanyog','lodhi','jabalpur','indian')

admin1.privilege.show_privileges()

#----------------------------------------------------------------------------------------------------------------

#9.9

# creating Parent class
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




# creating a separate class for battery
class Battery:
    def __init__(self,battery_size):
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


    # defining a method specific to child class
    def describe_battery(self):
        print(f"The size of battery of {self.manufacturer} {self.model} is {self.battery} KWH.")


    # overiding method from parent class
    def fill_gas_tank(self):
        print("You can't fill gas in an electric car. It runs on battery.")


my_electric = ElectricCar('tesla','model s',2019)

#before upgrading the battery
my_electric.battery.describe_battery()
my_electric.battery.get_range()

# afer upgrading the battery
my_electric.battery.upgrade_battery()
my_electric.battery.describe_battery()
my_electric.battery.get_range()

#----------------------------------------------------------------------------------------------------------------