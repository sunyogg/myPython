
a = 5
b = 6

print(a + b)
print(int.__add__(a, b))

#-----------------------------------------------------------------------------
# a + b -> __add__(a, b)
# a - b -> __sub__(a, b)
# a * b -> __mul__(a, b)
# You can see operators are calling their magic method.

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1 
        self.m2 = m2

    # 
    def __add__(first_operand, second_operand):
        print("You are trying to add two instances using the + operator.")
        r1 = first_operand.m1 + first_operand.m2
        r2 = second_operand.m1 + second_operand.m2
        r3 = r1 + r2
        return r3

    def __gt__(first_operand, second_operand):
        r1 = first_operand.m1 + first_operand.m2
        r2 = second_operand.m1 + second_operand.m2
        if r1 > r2:
            return True
        else:
            return False
        


s1 = Student(44, 46)
s2 = Student(69, 34)

print(s1 + s2)
# a + b -> __add__(a, b)
# if we have performed this operation without defining the __add__() method
# then python would have thrown an error telling unsupported operands to 
# perform this operation(+) as we were trying to add to objects. But since
# we have overidden the + operaton by defining the __add__() so now when
# we add two objects using + operator python won't throw any error, and will
# perform action being told inside that [__add__()] function.
# s1.m1 + s1.m2 + s2.m1 + s2.m2

# Since we have overwritten greater than operator [__gt__()], you can see 
# how it now has ability to compare to instance and check which one is bigger.
if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')

#------------------------------------------------------------------------------------------------

class Working_days:

    def __init__(self, name, working_days):
        self.name = name
        self.working_days = working_days

    def __mul__(self, other):
        x = self.working_days * other.salary
        return x

class Salary:

    def __init__(self, name, salary_of_day):
        self.name = name
        self.salary = salary_of_day


jes = Working_days('Jess', 30)
salary = Salary('Jess', 9000)


print(jes * salary)
print(salary * jes)

# a * b -> __mul__(a, b) : explanation of concern written below.

# does it like only checks the type of first argument or both the argument,
# if both then why does the print statement below throwing an error.
# if __mul__() is defined in Salary then salary has to come first and if 
# __mul__() is defined in Working_days then working_days has to come first.

#------------------------------------------------------------------------------------------------



class Ferrari:
    def fuel_type(self):
        print("Petrol")

    def max_speed(self):
        print("Max speed 350")

class BMW:
    def fuel_type(self):
        print("Diesel")

    def max_speed(self):
        print("Max speed is 240")

ferrari = Ferrari()
bmw = BMW()

for objs in (ferrari, bmw):
    objs.fuel_type()
    objs.max_speed()

#------------------------------------------------------------------------------------------------

