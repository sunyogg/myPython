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
        print("The restaurant is open everyday from 9am to 10pm.")
  

    # This method will read the amount of customer served
    def read_customer(self):
        print("customer served:",self.customer_served)


    # This method will let us set the number of customer served
    def set_customer_served(self,served):
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