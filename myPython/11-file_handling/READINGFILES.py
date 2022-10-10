
import os

print(os.listdir()) 
# this method returns the list of files in the current working directory

print("->",os.getcwd()) 
# this method returns the address of directory we are in currently '''

os.chdir('/Users/sunyoglodhi/Desktop/python/my_work/my_practice/11-filesandexceptions') 
# this functon changes the current working directory to the address we gave

print("->",os.getcwd()) 
# now check the address of the directory again

with open('greet.txt') as file:
    content = file. read()
print (content)

# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# but if you this method you'll have to manually close the file that you opened to 
# access contents of it.

f = open('greet.txt','r')

print(f.name) # printing the name of the file we are opening 
print(f.mode) # printing the mode with which we are opening the file
print(f.read())

f.close()

# ------------------------------------------------------------------------------------------------------------------------------------

# let's use the function that will not require us to manually close the file and 
# instead closes the file automatically.

with open('greet.txt') as file:
    content  = file.read()
print(content)

with open('greet.txt') as file:
     content1 = file.readlines()
print(content1)


with open('greet.txt') as file:
    content2 = file.readline()
    print(content2)

    content2 = file.readline()
    print(content2)

    content2 = file.readline()
    print(content2)

    content2 = file.readline()
    print(content2)


# ------------------------------------------------------------------------------------------------------------------------------------

with open('greet.txt') as file:
    for line in file:
        print(line, end = '') 
# The end parameter in the print function is used to add any string. At the end of 
# the output of the print statement in python. By default, the print function ends 
# with a newline. Passing the whitespace to the end parameter (end=' ') indicates 
# that the end character has to be identified by whitespace and not a newline.

# ------------------------------------------------------------------------------------------------------------------------------------