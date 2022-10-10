
# Changing the current working directory to the directory 
# where the .txt file is present.

# - - - - - - - - - - - - - - - - - - - - - 

# Giving relative file path
with open('revisions/files1_pie.txt') as file_object:
    content = file_object.read()
    
print("-->", content.strip())

# - - - - - - - - - - - - - - - - - - - - - 
# Giving Absolute file path
with open('/Users/sunyoglodhi/Desktop/python/my_work/my_practice/revisions/files1_pie.txt') as file_object:
    content = file_object.read()

print("-->",content)

# - - - - - - - - - - - - - - - - - - - - - 

import os
#print("->",os.getcwd())
os.chdir('/Users/sunyoglodhi/Desktop/python/my_work/my_practice/revisions')
#print("->",os.getcwd())

# - - - - - - - - - - - - - - - - - - - - - 

with open('files1_pie.txt') as file_object:
    content = file_object.read()
    
print("-->", content.strip())

# - - - - - - - - - - - - - - - - - - - - - 
# example of ValueError: I/O operation on closed file.
with open('files1_pie.txt') as file_object:
    print(file_object.read())
for numbers in file_object:
    print(numbers)


filename = 'files2_greeting.txt'
with open(filename) as file_object:
    content = file_object
for line in content:
    print(line)

#---------------------------------------------------------------------------------------------------------------------------
filename = 'files2_greeting.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

#---------------------------------------------------------------------------------------------------------------------------

filename = 'files2_greeting.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

print(lines)

#---------------------------------------------------------------------------------------------------------------------------


filename = 'files2_greeting.txt'
with open(filename) as file_object:
    content = file_object.readlines() # all the lines of .txt are now stored
                                      # as an element in a list

for line in content:
    print(line.strip())

#---------------------------------------------------------------------------------------------------------------------------


with open('files1_pie.txt') as file_object:
    content = file_object.readlines()

pie_string = ""
for line in content:
    line = (line.strip()) # you don't need to put str() here since Python 
    pie_string = pie_string+line            # interprets all text in the file as a string.


print(len(pie_string))
print(content)

#---------------------------------------------------------------------------------------------------------------------------
# Large Files: One Million Digits

filename = '/Users/sunyoglodhi/Desktop/python/resources-pcc/chapter_10/pi_million_digits.txt'

with open(filename) as file_object:
    content = file_object.readlines()

stringg = ''

for line in content:
    stringg = stringg + line.strip()

print(stringg[0:10])
print(len(stringg))

dob = (input("Enter your Date of Birth in mmddyy form: "))

if dob in stringg:
    print(f"{dob} is in first 1 milliion iteration of pie." )
else:
    print(f"{dob} is not in 1 million digits of pie.")

print(stringg[0:10])
print(len(stringg))

#print(content)

#---------------------------------------------------------------------------------------------------------------------------

"""
# weird case !!!!

with open('files3_write.txt','r+') as file_object:

    
    print(file_object.read())
    file_object.write('Hello sunyog, how are you?')
    print(file_object.read())
"""
#---------------------------------------------------------------------------------------------------------------------------
# writing on a file

with open('files3_write.txt','w') as file_object:

    file_object.write("HELLO WORLD, I Love Programming\n")
    file_object.write(str(12345) +'\n')
    file_object.write("I Love Creating New Programs that helps people\n")


with open('files3_write.txt','a') as file_object:
    
    file_object.write("And I am really interested in AIML.\n")
    file_object.write("What can be the future of AI?")

#---------------------------------------------------------------------------------------------------------------------------

# Saving the user's info by using file handling

info = input("Enter something: ")

filename = 'userinfo.txt'
with open(filename,'w') as f:
    f.write(info)

#---------------------------------------------------------------------------------------------------------------------------