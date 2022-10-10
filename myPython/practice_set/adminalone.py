
from usersalone import Users

class Privileges:

    def __init__(self):
        self.privilege = [
            'can add post',
            'can delete post',
            'can add user',
            'can ban user',
            'can call a meeting',
            'can edit information',
            'can change UI'
        ]
    
    def show_privileges(self):
        for privilege in self.privilege:
            print(f"-> {privilege.title()} ")


# creating a child class called Admin which inherits from parent class Users
class Admin(Users):
    
    # calling all the attributes of parent class to child class
    def __init__(self,fname,lname,locality,nationality):
        super().__init__(fname,lname,locality,nationality)

        self.privilege = Privileges()