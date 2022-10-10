
# 9.1
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name.title()
        self.cuisine = cuisine_type.title()

    def describe_restaurant(self):
        print(f"\nHere are some of the details regarding {self.name}")
        print(f"{self.name.title()} is a family and friends restaurant.")
        print("Veg and non-veg both are available here.")
        print(f"The cuisine type is {self.cuisine.title()}")

    def open_restaurant(self):
        print(f"{self.name.title()} is open from 9am to 12 am.")

# creating instance
restaurant1 = Restaurant('chinese palace','chinese')
# an instance has been created which is stored in restarant1 
# accessing attributes
print(restaurant1.name)
print(restaurant1.cuisine)
print(f"\nHave you heard of {restaurant1.name}. It's cuisine type is {restaurant1.cuisine}")

restaurant1.open_restaurant()
restaurant1.describe_restaurant()

#----------------------------------------------------------------------------------------------------------

# 9.2

class Restron:

    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name.title()
        self.cuisine = cuisine_type.title()

    def describe_restron(self):
        print(f"Here are some of the details regarding {self.name.title()}")
        print(f"{self.name.title()} is a {self.cuisine.title()} restaurant.")
        print(f"Both veg and non_veg are available.")
        print(f"It is open from 9am to 12am.")

    def open_restron(self):
        print(f"{self.name.title()} is open now.")


rest1 = Restron('korean point','korean')
print('\n',rest1.name)
print(rest1.cuisine)
rest1.describe_restron()

rest2 = Restron('punjabi tadka','punjabi')
print('\n',rest2.name)
print(rest2.cuisine)
rest2.describe_restron()

rest3 = Restron('biryani and curry point','indian')
print('\n',rest3.name)
print(rest3.cuisine)
rest3.describe_restron()

#----------------------------------------------------------------------------------------------------------

# 9.3
class User:
    
    def __init__(self,fname,lname,dob,locality):
        self.first = fname.title()
        self.last = lname.title()
        self.birth = dob.title()
        self.locality = locality.title()
    
    def describe_user(self):
        print(f"first name: {self.first}")
        print(f"last name: {self.last}")
        print(f"birth date: {self.birth}")
        print(f"locality: {self.locality}")

    def greet_user(self):
        print(f"Hello {self.first} {self.last} ! How are you?")



user1 = User('sanyog','lodhi','20 november','jabalpur')
user1.describe_user()
user1.greet_user()
print("")
user2 = User('arun','lodhi','22 april','bahoripar')
user2.describe_user()
user2.greet_user()
print("")

user3 = User('saurabh','patel','1 november', 'lakhnadawn')
user3.describe_user()
user3.greet_user()

#----------------------------------------------------------------------------------------------------------        





