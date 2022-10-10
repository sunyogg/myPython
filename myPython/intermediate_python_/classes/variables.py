class Student:

    # class variable
    school_name = 'St. Augustine school'

    def __init__(self, first, last, grade):
        self.first = first
        self.last = last
        self.grade = grade

    
    def describe(self):
        fullname = '{} {}'.format(self.first.title(), self.last.title())
        print(fullname)
        print(self.grade)
        print(Student.school_name)
        #print(self.school_name)



student_a = Student('sanyog', 'lodhi', 12)
student_b = Student('pusha', 'patel', 11)

print(Student.school_name)
print(student_a.school_name)
print(student_b.school_name,'\n')

Student.school_name = 'Little World'

print(Student.school_name)
print(student_a.school_name)
print(student_b.school_name,'\n')

student_a.school_name = 'Christ Church'

print(Student.school_name)
print(student_a.school_name)
print(student_b.school_name,'\n')

#student_a.describe()