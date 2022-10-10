
# 10.6 and 10.7
print("Enter two numbers below to add them:")
print("You can also enter 'q' to quit the program")

while True:

    x = (input('-> '))
    if x == 'q':
        break
    y = (input('-> '))
    if y == 'q':
        break

    try:
        sum = (int(x)+int(y))

    except ValueError:
        print('Sorry! You can only enter value that are in numeric form')

    else:
        print(sum)

# -------------------------------------------------------------------------------------------

# 10.8
import os
os.chdir('/Users/sunyoglodhi/Desktop/python/my_work/my_practice/12-exceptions/practiceset')



def tell_name(filename):
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Oops! The file {filename} does not exist. ")
    else:
        print(content.strip())

filename = ['dogs.txt','cats.txt']
# we have stored dogs.txt in parent directory but cats.txt is not in parent directory
for files in filename:
    tell_name(files)

# -------------------------------------------------------------------------------------------

# 10.9

import os
os.chdir('/Users/sunyoglodhi/Desktop/python/my_work/my_practice/12-exceptions/practiceset')


def tell_name(filename):
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        pass
    else:
        print(content.strip())


filename = ['dogs.txt','cats.txt']
# we have stored dogs.txt in parent directory but cats.txt is not in parent directory
for files in filename:
    tell_name(files)
    
# -------------------------------------------------------------------------------------------
# 10.10
filename = '/Users/sunyoglodhi/Desktop/python/resources-pcc/chapter_10/alice.txt'

try:
    with open(filename) as f:
        content = f.read()

except FileNotFoundError:
    print("The filename or filepath you entered does not exist")

else:
    print(content.count('the'))
    print(content.lower().count('the'))
    print(content.count('the '))
    print(content.lower().count('the '))

# -------------------------------------------------------------------------------------------