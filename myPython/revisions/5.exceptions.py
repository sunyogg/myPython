

print(5/0)

print("DIVISION")
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

try:
    z = (x/y)

except ZeroDivisionError:
    print("You can't divide a number by 0, It's not defined.")

else:
    print("Result: ",z)

# Now we will print 'hello world' to make sure that program continues running 
# even after the some part of the program fails or shows an error.

print("HELLO WORLD")

# ----------------------------------------------------------------------------------
# Using a nested try and except block when more than one type of error can occur
# from a single input value.


print('DIVISION')
print("Enter 'q' to stop the program.")

while True:

    try:
        x = (input("Enter a number: "))
        if x == 'q':
            print("Program stopped.")
            break
        
        y = (input("Enter another number: "))
        if y == 'q':
            print("Program stopped.")
            break

        try:
            print('Result->',int(x)/int(y))

        except ZeroDivisionError:
            print("You cannot divide a number by 0, it's not defined.")

    except ValueError:
        print("You can only input integer value, Please input an integer.")

    # ----------------------------------------------------------------------------------
import os


os.chdir('/Users/sunyoglodhi/Desktop/python/resources-pcc/chapter_10')
     

# Handeling file not found error.

filename = ['alice.txt','moby_dick.txt','siddhartha.txt','think_like_a_monk.txt']




def count_words(bookname):

    try:
        with open(bookname) as file_object:
            content = file_object.read()

    except FileNotFoundError:
        print("The file you want to read does not exist in the current working directory.")
        

    else:
        words = content.split()
        length = len(words)
        thenumber = content.lower().count('the ')
        print(f"The file {bookname} has approximately {length} words in it.")
        print(f"The file {bookname} contains {thenumber} 'the' in it.")

#---------------------------------------------------------------------------------------------------------

for file in filename:
    count_words(file)

# stoing user's input in a file without using json

filename = 'quote.txt'
with open(filename,'w') as f:
    quote = input("Enter something: ")
    f.write(quote)


# storing user's data using json

import json
filename = 'quote.json'
with open(filename,'w') as f:
    quote = input("Enter something: ")
    json.dump(quote,f)

# ----------------------------------------------------------------------------------
'''
# STORING DATA, USING JSON

from json import JSONDecodeError
import os
os.chdir('/Users/sunyoglodhi/Desktop/python/my_work/my_practice/revisions')
'''
import json

filename = 'numbers.json'

numbers = [1,2,3,4,5,6,7]
stringg = "hello how you doing?"

with open(filename,'w') as f:
    json.dump(numbers,f)

with open(filename,'r') as f:
    number = (json.load(f))

print(number)


import json

filename = 'information.json'
information = input("Enter Something: ")

with open(filename,'w') as f:
    json.dump(information,f)

with open(filename,'r') as f:
    info = json.load(f)

print(info)


# refactoring

def greet_user():
    import json

    filename = 'remember_me.json'
    try:
        with open(filename) as f:
            name = json.load(f)

    except FileNotFoundError:
        name = input("Enter your username: ")
        print(f"We will remember you {name.title()}")
        with open(filename,'w') as f:
            json.dump(name,f)

    else:
        print(f"Welcome back! {name.title()}.")

# ----------------------------------------------------------------------------------------------------------------

# greet_user()
# refactoring a bit more and making each function to perform a single task.

import json

def get_stored_username():
    """Get stored username if available."""
    import json

    try:

        try:
            filename = 'rememberme.json'
            with open(filename) as f:
                name = json.load(f)

        except FileNotFoundError:
            return None

        else:
            return name

    except JSONDecodeError:
        return None

# JSONDecodeError
# This error occurs when you delete the name stored in rememberme.json and try
# to run the program.
        


def register_username():
    """prompt the user for new username."""
    import json
    filename = 'rememberme.json'
    name = input("Enter your username: ")

    with open(filename,'w') as f:
        json.dump(name,f)

    print(f"Thanks for registering {name.title()}. We will remember you next time.")


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back! {username.title()}.")

    else:
        register_username()



greet_user()  

#---------------------------------------------------------------------------------------------------



