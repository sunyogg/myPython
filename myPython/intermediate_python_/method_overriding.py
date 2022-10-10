
class A:

    def show(self):
        print("In A show.")

class B(A):

    def show(self):
        # first comment the print statement and use the pass statement and then
        # try to run the program and then try again by uncommenting the print
        # statement and removing the pass statement.
        print("In B show.")


a1 = A()
a1.show()

a2 = B()
a2.show()

# So when there was no show() method in child class B, when we try to call 
# show() method from the instance of B, it'll use the show() method from the
# parent class A, but when we created a show() method in child class, it started
# using it's own show() method rather than using the show() method from parent 
# class this is what method overriding is it first uses the method from the 
# parent class when it does not have the method of that name, but as soon as 
# there created a method of that same in the child class, the child class will
# start calling the method of its own.

#-------------------------------------------------------------------------------------------------

# Overriding built-in functions.

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