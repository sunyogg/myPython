
# to call class method use the name of the class and name of the class method
# separated by a dot. Used to access or modify the class state. In method 
# implementation, if we use only class variables, then such type of methods 
# we should declare as a class method. The class method has a cls parameter 
# which refers to the class. A class method is bound to the class and not the 
# object of the class. It can access only class variables.


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = self.first +'.'+ self.last +'@company.com'


    def fullname(self):
        x = '{} {}'.format(self.first, self.last)
        return x 


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        """This method is working on class."""
        cls.raise_amt = amount


    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)



emp_1 = Employee('corey', 'schafer', 50000)
emp_2 = Employee('dan', 'houser', 60000)


Employee.set_raise_amt(1.07)
#Employee.raise_amt = 1.07
#emp_1.set_raise_amt(1.07)

#print(Employee.raise_amt)
#print(emp_1.raise_amt)
#print(emp_2.raise_amt)


emp_1_str = 'john-doh-70000'
emp_2_str = 'david-curtfield-50000'
emp_3_str = 'elon-houser-30000'


#first, last, pay = emp_1_str.split('-')


#emp1_new = Employee(first, last, pay)

#print(emp1_new.email)
#print(emp1_new.pay)

new_emp_1 = Employee.from_string('elon-houser-30000')

# -----------------------------------------------------------------------------------------------

class Student:
    """Class that represents a general student."""

    # Class variable
    school_name = 'Little World'

    def __init__(self, fname, lname, grade):
        """Initialize the attributes of student class."""
        self.first = fname 
        self.last = lname
        self.grade = grade
        


    def describe(self):
        """Describe the attributes of a student."""
        print('{0} {1} \n{2}\n{3}'.format(self.first.title(), self.last.title(), self.grade, Student.school_name))


    # factory class method 
    # Class methods are used when we are dealing with factory methods. Factory 
    # methods are those methods that return a class object for different use cases.
    @classmethod
    def student_string(cls, string):
        f, l, g = string.split('-')
        return cls(f, l, g)

    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school

# method outside the class
def excercise(cls):
            print(f"Below excercises for {cls.school_name}")

# defining the method outside the class as classmethod
Student.excercise = classmethod(excercise)


stu1 = Student('david', 'john', 9)

stu1.describe()
Student.excercise()


stustring = 'alex-martin-10'

stu2 = Student.student_string(stustring)
stu2.describe()


Student.change_school('St. Augustine school')

# -----------------------------------------------------------------------------------------------

class Course(Student):

    def course_available(self):
        print("Below are the courses available:")
        print('\tStatistics\n\tAlgebra\n\tMachine learning\n\tPython\n\tWeb development')


stu3 = Course('Alexa', 'Stropper', 11)
stu3.course_available()



stu4 = Student.student_string('john-stolley-7')

stu4.describe()
# -----------------------------------------------------------------------------------------------

class Student:

    num_of_emp = 0

    def __init__(self, first, last, grades, residence):
        self.first = first
        self.last = last
        self.grades = grades
        self.residence = residence
        Student.num_of_emp += 1


    # factory method: since it's returning an instance  
    @classmethod
    def _alt_constructor(cls, emp_string):
        first, last, grade, residence = emp_string.split('-')
        grades = int(grade)
        return cls(first, last, grades, residence )
        

s1 = Student._alt_constructor('prasoon-lodhi-12-jabalpur')
print(Student.num_of_emp)

# -----------------------------------------------------------------------------------------------