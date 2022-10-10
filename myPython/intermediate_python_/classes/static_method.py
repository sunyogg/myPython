# static method
# So whenever we call a method for an individual instance, a different instance
# method is created for so even if we call same method for two different instance
# then two different method will be created for those two different instance, 
# Whereas when we call static method only one copy is created for all the
# different instance that call that static method.  


class Student:

    school_name = 'Little World'

    def __init__(self, first, last, grade):
        self.first = first
        self.last = last
        self.grade = grade
        self.email = self.first + '.' + self.last + '@school.com'


    def describe(self):
        print('{} {}'.format(self.first.title(), self.last.title()))
        print(self.grade)
        print(Student.school_name)


    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school 
        # calling a static method insdie a class method
        cls.hello()


    @staticmethod
    def hello():
        print("Hello world")


    @staticmethod
    def course_name(course):
        print(course, 'is a great course.')
        # calling a static method inside a static method.
        Student.hello()


    def greet(self):
        print("Hello student how are you")
        # calling a static method inside an instance method.
        Student.hello()


stu1 = Student('davey', 'cruiser', 10)
stu2 = Student('harvey', 'land', 8)



# See how for instance method different copy is created for different instances.
# is checks the id of the function
print(stu1.describe is stu2.describe)
# See how only one copy is created when calling the static method for all the 
# instances of the class.
print(stu1.hello is stu2.hello)

# see the location of the instance method
print(stu1.describe)
print(stu2.describe)

# see the location of the static method
print((stu1.hello))
print((stu2.hello))
print((Student.hello))

print((Student.change_school))

print('\n\n')

stu1.greet()
Student.change_school('Joy')
stu2.course_name('python')

# -----------------------------------------------------------------------------------------------------------