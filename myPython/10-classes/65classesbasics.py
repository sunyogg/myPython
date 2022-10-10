
class Dog:
    '''a simple attempt to model a dog'''

    def __init__(self,name,age):
        '''initialize name and age attribute'''
        self.name = name # self nahi lagayenge to ye attributes sabhi instances
        self.age = age   # ke liye available nahi rahinge, ye sabhi instances ke
                         # liye available hai hi self ki madad se.
    
    def sit(self):
        '''simulate a dog sitting in response to a command'''
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        '''simulate rolling over in response to a command'''
        print(f"{self.name} rolled over!")



# creating instances -> instantiation
my_dog = Dog('Kaalu',6) 
# we are telling python to create an instance and we assign that instance to vairable my_dog, which is know as instance variable.
# #idhar pe self bhi pass ho raha hai jo hume nahi dikh raha.
# object ya instance banate waqt __init__ funciton apne aap hi run ho jata hai

#An object (instance) consists of : 

#State: It is represented by the attributes of an object. 
#       It also reflects the properties of an object.
#Behavior: It is represented by the methods of an object. 
#          It also reflects the response of an object to other objects.
#Identity: It gives a unique name to an object and enables one object to interact 
#          with other objects.


my_dog2 = Dog('Tommy',12)
# yaha pe humne python se bola ki ek instance(dog) banao jiska naam tommy hona chaiye
# or age 12 honi chaiye, python ne jabb ye line read kari, to usne __init__ method
# run kiya(automatically), __init__ method me parameter self ki jagah argument self
# pass hua jisse calling method me likhne ki zarurat nahi hoti, or name parameter me
# tommy pass hua, waise hi age parameter me 12 pass hua or fir __init__ method ne
# ek instance banaya uska name or age attributes me wo dala jo humne pass kiya tha
# fir python ne uss instance ko return kiya jisko ki humne my_dog1 me store kiya.



#accessing attributes of an instance
print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")
print(f"My another dog name is {my_dog2.name} and his age is {my_dog2.age}")


# calling methods
my_dog.sit()
my_dog2.roll_over()



#-------------------------------------------------------------------------------------------------------

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def rollover(self):
        print(f"{self.name} rolled over.")

my_dog = Dog('kaalu',6)
your_dog = Dog('lucy',5)

# accessing attributes
print(my_dog.name)
print(your_dog.age)

#accessing methods
my_dog.sit()
your_dog.rollover()

#-------------------------------------------------------------------------------------------------------


class Employee:
    """This class will create data of employees"""


    def __init__(self,first,last,age,pay,experience,location):
        self.first = first.title()
        self.last = last.title()
        self.age = age
        self.pay = pay
        self.experience = experience
        self.location = location.title()
        self.fullname = self.first + " " + self.last
    

    def describe_emp(self):
        """This method will describe the employee."""
        print(f"\nHere are the details of employee {self.first} : ")
        print(f"Full name = {self.fullname}")
        print(f"Age  = {self.age}")
        print(f"Pay = {self.pay}$")
        print(f"Experience = {self.experience} year(s)")
        print(f"Location = {self.location}")


    def eligibility(self):
        """This method will check if the employee is eligible to vote."""
        if self.age >= 22:
            print(f"\n{self.fullname} is eligible to vote in the office affairs.")
        else:
            print(f"\n{self.fullname} is not eligible to vote in the office affairs.")


    def check_level(self):
        """This method will check the level of an employee."""
        if 1 <= self.experience <= 3:
            print(f"\n{self.first} is a Bronze member!")
        if 4 <= self.experience <= 6:
            print(f"\n{self.first} is a Silver member!")
        if 7 <= self.experience <= 10:
            print(f"\n{self.first} is a Gold member!")
        if 11 <= self.experience <= 15:
            print(f"\n{self.first} is a Diamond member!")
        if 16 <= self.experience <= 20:
            print(f"\n{self.first} is a Platinum member!")
        if self.experience > 20:
            print(f"\n{self.first} is a Rhodium member!")



# creating instances/objects emp1 and emp2 and emp3 and emp4
emp1 = Employee('larry','branson',38,60000,8,'california')
emp2 = Employee('rich','bryan',45,120000,11,'silicon valley')
emp3 = Employee('terry','brown',19,30000,1,'texas')
emp4 = Employee('hudson','stell',78,300000,30,'new york')


# see how all the instances are unique and stored at different locations. 
print(emp1) 
print(emp2)
print(emp3)
print(emp4)

# accessing attributes of certain instance
print(emp1.fullname)
print(emp2.age)
print(emp3.experience)
print(emp4.pay)

# calling a method for a particular instance or object
emp1.describe_emp()
emp2.describe_emp()
emp3.describe_emp()
emp4.describe_emp()

emp1.eligibility()
emp2.eligibility()
emp3.eligibility()
emp4.eligibility()

emp1.check_level()
emp2.check_level()
emp3.check_level()
emp4.check_level()

#-------------------------------------------------------------------------------------------------------



