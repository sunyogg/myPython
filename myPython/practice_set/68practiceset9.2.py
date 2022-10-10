
# 9.4
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



#created an instance
restron = Restaurant('jubali','south indian')

# calling methods
restron.describe_restaurant()

restron.open_restaurant()

restron.read_customer()

restron.set_number_served(20)
restron.read_customer()

restron.increment_customer_served(8)
restron.read_customer()

#-----------------------------------------------------------------------------------------------------------

#9.5 
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

user1 = Users('sunyog','lodhi','jabalpur','indian')

# calling methods
user1.describe_user()

user1.greet_user()

user1.read_login_attempts()

user1.increment_login_attempts()
user1.read_login_attempts()

user1.reset_login_attempts()
user1.read_login_attempts()

#-----------------------------------------------------------------------------------------------------------
