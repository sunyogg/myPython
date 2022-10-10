
# 10.11

import json

filename = 'fav_number.json'
with open(filename,'w') as fw:
    fav = int(input("Enter your favorite number: "))
    json.dump(fav,fw)

filename = 'fav_number.json'
with open(filename,'r') as fw:
    favnumber = json.load(fw) 
    print(f"I know your favorite number! It's {favnumber}")   
'''
#--------------------------------------------------------------------------------------
'''# 10.12
import json
filename = 'fav_number.json'


try:
    with open(filename,'r') as fr:
        favn = json.load(fr)


except FileNotFoundError:
    with open(filename,'w') as fw:
        fav = int(input("Enter your favorite number: "))
        json.dump(fav,fw)
        print(f"I know your favorite number! It's {fav}")

else:
    print(f"I know your favorite number! It's {favn}")
    

#--------------------------------------------------------------------------------------

# refactoring 10.12

import json
from urllib.request import ftpwrapper

def check_fav_number():
    """This function will check if there is any fav_number stored in the file"""
    try:
        with open('fav_number.json','r') as fr:
            favn = json.load(fr)

    except:
        return None

    else:
        return favn

def ask_fav_number():
    """This function will ask the user for the favorite number if the file is empty"""

    with open('fav_number.json','w') as fw:
        askn = int(input("Enter your favorite number: "))
        json.dump(askn,fw)
        print(f"I know your favorite number! It's {askn}")

def tell_fav_number():
    """This function will return the fav_number of the user."""
    fav_no = check_fav_number()
    if fav_no:
        print(f"I know your favorite number! It's {fav_no}")
    else:
        ask_fav_number()



tell_fav_number()

#--------------------------------------------------------------------------------------

# 10.13
# modifying username program


import json
def check_username():
    """This funtion will check the existence of the username in the file."""
    try:
        filename = 'username.json'
        with open(filename,'r') as fr:
            name = json.load(fr)
    except FileNotFoundError:
        pass

    else:
        return (f"Welcome back {name}!")

def create_new_user():
    """This function will store new username if there is not any in file."""
    filename = 'username.json'
    with open(filename,'w') as fw:
        name = input("Enter your username: ")
        json.dump(name,fw)
        print(f"We will remember you next time {name}")

def greet_user():
    """This function will greet the user accordingly with different message."""
    usern = check_username()
    if usern:
        print(usern)
        # What if there's a new user trying to enter his name? so we add another
        # block of code to ask the user if they are new or existing
        x = input("Is this your correct username y/n : ")
        if x == 'y':
            pass
        else:
            create_new_user()

    else:
        create_new_user()

greet_user()


#--------------------------------------------------------------------------------------










    