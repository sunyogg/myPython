# Method overloading
# It is not supported is python, but let's just look at it's working
# and try to imagine if it was ever supported, how it would look.

# So function overloading means when there are two function of same name
# in same class but both of them take different argument, it is known
# function overloading. But since this is not supported then how does python
# work out of this kind of situation? So if there are more than one method
# of same name in a same class then python will only consider the last method
# with that name. for example:
# class Student:
#     def show(a):
#         pass
#     def show(x, y):
#         pass 
#     def show(p, q, r):
#         pass

# As you can see that class Student contains three method with same name, 
# but all of them take different argument, so what python will do is it'll
# only consider the last method i.e. show(p, q, r) and ignore all the methods
# of same name that came before it.



class Student:

    def __init__(self, first, last, grade):
        self.first = first
        self.last = last
        self.grade = grade

    def show(self, x, y, z):
        print(x, y, z)

    def show(self, a, b):
        print(a, b)


s1 = Student('sunyog', 'lodhi', 8)
s1.show(2,3)
s1.show(5, 6, 7) # error

# -----------------------------------------------------------------------------------

# a method that can take any number of argument but will always perform the same
# task on them.
def sum(*args):
    result = 0
    for arg in args:
        result += arg
    print(result)

sum(1, 2, 4)

# -----------------------------------------------------------------------------------