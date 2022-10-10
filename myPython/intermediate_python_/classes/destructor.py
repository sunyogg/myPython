class Student:

    def __init__(self, name, age, grade=10):
        # a contructor
        #print("Inside constructor.")
        self.name = name
        self.age = age
        self.grade = grade
        #print("Object Initialized.")


    def show(self):
        print('{} {} {}'.format(self.name.title(), self.age, self.grade))

    def __del__(self):
        # You can see how calling del runs __del__() method and deletes the object
        print("Inside destructor.")
        print("Object destroyed.")

print(dir(Student))
print('n\n')
s1 = Student('emma', 16)
print('s1 created')
# s1 is the reference to the instance created from class Student containing
# string 'emma' and integer 16.
#s1.show()
#del s1
#s1.show() # See how s1 won't be defined anymore.
s1.show()
del s1
s1.show()

# -----------------------------------------------------------------------------------------------------

# Exception occured in __init__() method
class Vehicle:
    def __init__(self, speed):
        if speed > 240:
            raise Exception('Not Allowed')
        self.speed = speed

    def __del__(self):
        print('Release resources')

# creating an object
car = Vehicle(350)
# to delete the object explicitly
del car

# -----------------------------------------------------------------------------------------------------