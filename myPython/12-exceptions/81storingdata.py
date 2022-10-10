# storing data in a file

import json

numbers = [1,2,3,4,5,6]

with open('numbers.json','w') as f:
    json.dump(numbers,f)


with open('numbers.json','r') as f:
    numbers = json.load(f)

print(numbers)

#----------------------------------------------------------------------------------------------
# storing data given by user in a file

import json

user = input("Enter your username: ")

with open('usernames.json','w') as f:
    json.dump(user,f)

with open('usernames.json','r') as f:
    user_ = json.load(f)

print("Hey",user_,"Welcome back!")

#----------------------------------------------------------------------------------------------

# checking whether a user has visited before or not if he had then
# then we will print a message of welcoming back the user, if he
# had not then we will prompt user to enter his username and tell
# that we will remember him next time.

import json

filename = 'usernames.json'

try:
    with open(filename,'r') as fr:
        user = json.load(fr)

except FileNotFoundError:
    tell_username = input("Enter your username: ")
    with open(filename,'w') as fw:
        json.dump(tell_username,fw)
        print(f"{tell_username}, we will remember you. ")

else:
    print(f"{user}! welcome back.")

#----------------------------------------------------------------------------------------------

# refactoring the above program
# wrapping the program above inside a function

def greet_user():
    """ greet user by their name"""
    import json

    filename = 'usernames.json'

    try:
        with open(filename,'r') as fr:
            user = json.load(fr)

    except FileNotFoundError:
        tell_username = input("Enter your username: ")
        with open(filename,'w') as fw:
            json.dump(tell_username,fw)
            print(f"{tell_username}, we will remember you. ")

    else:
        print(f"{user}! welcome back.")

greet_user()

#----------------------------------------------------------------------------------------------

# refactoring the above the program

import json

def get_stored_username():
    try:
        filename = 'username.json'
        with open(filename,'r') as fr:
            username = json.load(fr)
    except FileNotFoundError:
        return None
    else:
        return  username

def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back {username}")
    else:
        user = input("Enter your name: ")
        filename = 'username.json'
        with open(filename,'w') as fw:
            json.dump(user,fw)
        print(f"We will remember you next time, {user}")
            
greet_user()

#----------------------------------------------------------------------------------------------

# refactoring the above program a bit more

import json

def find_user():
    """This function will check the existence of the user."""
    filename = 'username.json'
    try:
        with open(filename,'r') as fr:
            name = json.load(fr)
    
    except FileNotFoundError:
        return None
    else:
        return name


def prompt_new_user():
    """This fucntion will make new user."""
    filename = 'username.json'
    with open(filename,'w') as fw:
        usern = input("Enter your name: ")
        json.dump(usern,fw)
        print(f"We will remember you next time {usern}")


def greet_user():
    """This fucntion will greet the user"""
    if find_user():
        username = find_user()
        print(f"Welcome {username}")
    else:
        prompt_new_user()

#----------------------------------------------------------------------------------------------    


