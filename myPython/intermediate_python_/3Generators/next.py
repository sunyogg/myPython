'''
class Car:

    def init(self, name, color):
        #car1 = Car('suzuki gt', 'red')
        #TypeError: Car() takes no arguments
        # when init: python does not know that the instance we created by
        # passing the attributes need to be attached to the car class.
        # so can we say 
        # class Car(name, color) == def __init__(self, name, color)
        self.name = name
        self.color = color

    def describe_car(self):
        print(self.name.title(), self.color.title())

print("")

car1 = Car('suzuki gt', 'red')
car2 = Car('audi r8', 'black')

car2.describe_car()


def count_string(string):
    ans = 0
    stripped = string
    for i in stripped:
        if i == 'e':
            ans += 1

    yield ans

count_string('geeksforgeek')'''

fruits = ['mango', 'apple', 'banana']
x, y, z = fruits

print(x)
print(y)
print(z)


p = q = r = s = 'SonOfGun'

print(p)
print(q)
print(r)
print(s)


print("We are so called \"vikings\' from the north.")