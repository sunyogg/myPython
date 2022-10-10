class Student:

    def __init__(self, fname, lname, grade):
        self.first = fname 
        self.last = lname 
        self.grade = grade

    def _greet_(self):
        # This is a helper function and it is generally created using a 
        # underscore in front of a function name. 
        # We don't need to call helper function from the object.
        # and can be called from another function using self keyword.
        # it helps to organize a class.
        print(f'hello! {self.first}')

    def describe(self):
        print('{} {}'.format(self.first.title(), self.last.title()))
        print(f"{self.grade}")

        # helper function is called using the self keyword.
        self._greet_()


a = Student('sunyog', 'lodhi', 12)

a.describe()

# -----------------------------------------------------------------------------------