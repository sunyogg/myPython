

class Users:
        '''creating a class called user'''


        '''initializing attributes'''
        def __init__(self,fname,lname,locality,nationality):
            self.first = fname.title()
            self.last = lname.title()
            self.locality = locality.title()
            self.nationality = nationality.title()
            self.login_attempts = 0


        # this method will describe the user
        def describe_user(self):
            print(f"\nfirst: {self.first}")
            print(f"last: {self.last}")
            print(f"locality: {self.locality}")
            print(f"nationality: {self.nationality}")

        
        # this method will greet user
        def greet_user(self):
            print(f"\nHello {self.first} {self.last}. How are you?")


        # this method will read number of login attempts
        def read_login_attempts(self):
            print(f"login_attempts: {self.login_attempts}")


        # this method will increment number login attempts by 1
        def increment_login_attempts(self):
            self.login_attempts += 1


        # this method will reset the number of login attempts
        def reset_login_attempts(self):
            self.login_attempts = 0




