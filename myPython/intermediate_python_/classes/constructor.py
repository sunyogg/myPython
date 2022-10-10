
# In python Constructor in nothing but __init__() method, it's helps
# to create and initialize an object.
# parametrized constructor
class Student:

    def __init__(self, name, age, grade=10):
        # a contructor
        self.name = name
        self.age = age
        self.grade = grade
        return True


    def show(self):
        print('{} {} {}'.format(self.name.title(), self.age, self.grade))


s1 = Student('emma', 16)
s1.show()





# -----------------------------------------------------------------------------------

# Defaul Constructor
# When no constructor is used inside the class
# If there is contructor used inside a class python will not use the 
# default contructor.

class Student:

    def show(self):
        print("Hello Students.")


s1 = Student()
s1.show()


# This is how a default constructor might looks like, it does not take any
# argument.
class Student:

    def __init__(self):
        pass

    def show(self):
        print("Hello Students.")


s1 = Student()
s1.show()

# -----------------------------------------------------------------------------------

# Non parametrized constructor
class Individual:

    def __init__(self):
        self.first = 'sunyog'
        self.last = 'lodhi'
        self.age = 20
        self.blood_group = 'AB+'
        self.eye_color = 'brown'
        self.hair_color = 'black'
        self.ethinicity = 'asian'
        self.mother_tongue = 'hindi'
        

    def show_detail(self):
        print(self.first.title())
        print(self.last.title())
        print(self.age)
        print(self.blood_group)
        print(self.eye_color)
        print(self.hair_color)
        print(self.ethinicity.title())
        print(self.mother_tongue.title())


sunyog = Individual()
sunyog.show_detail()

# -----------------------------------------------------------------------------------
# Constructor chaining
# Calling the constructor from another constructor.
class Car:

    def __init__(self, manufacturer, model, mileage):
        self.manufacturer = manufacturer
        self.model = model
        self.mileage = mileage


    def show(self):
        print(self.manufacturer, self.model)
        print(self.mileage)



class Electric(Car):

    def __init__(self, manufacturer, model, battery, charging_time, mileage):
        super().__init__(manufacturer, model, mileage)
        self.battery = battery
        self.charging_time = charging_time
        self.manufacturer = manufacturer
        self.model = model


    def tell(self):
        print(self.battery)
        print(self.charging_time)


ele = Electric('tesla', 'model s', '2000', '2hr', '60km')
ele.tell()

# -----------------------------------------------------------------------------------









