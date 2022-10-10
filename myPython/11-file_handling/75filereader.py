
# just by the file name

with open('pi_digits.txt') as file:
    contents = file.read()

    # The open() function returns an object representing the file.
    # here open() method is used to open the file, so that we can accesss the 
    # content of the file

    # once the file has been opened, we then use the read() method to read the 
    # contents of the file, then the content of the file are stored in variable,
    # called contents, later we print contents to read the contents of the file.

    # with() method closes the contents of the file  once the access is no longer needed.
    # Python will close it automatically when the with() block finishes execution.

print('\n',contents)

# ------------------------------------------------------------------------------------------------------
# providing relative path

# with open('greet.txt') as file: see how the program produces an error.
with open('greetf/greet.txt') as file:
    content = file.read()
    # a relative file path is useful when the .txt file is stored in another folder
    # inside the parent dictionary. It'll produce an error if .txt file is stored outside
    # the parent dictionary and you are providing a realtive file path. On that case
    # you have to provie the full path of the file.

print(content)

# ------------------------------------------------------------------------------------------------------
# providing absolute path

path = '/Users/sunyoglodhi/Desktop/python/my_work/my_practice/hell/hell.txt'

with open(path) as file:
    content = file.read()

print(content)

# ------------------------------------------------------------------------------------------------------
# reading line by line

file_name = 'pi_digits.txt'
with open(file_name) as file:
    for line in file:
        print(line.rstrip())

# ------------------------------------------------------------------------------------------------------
# making a list of lines from a file

path = 'greetf/greet.txt'
with open(path) as file_object:
    lines = file_object.readlines()

for line in lines: 
    print(line.rstrip())

# ------------------------------------------------------------------------------------------------------
# working with a file's content 

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

lane = ''
for line in lines: 
    lane += line.strip()

print(lane)

# ------------------------------------------------------------------------------------------------------
# Large Files: One Million Digits

filename = '/Users/sunyoglodhi/Desktop/python/resources-pcc/chapter_10/pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

lane = ''
for line in lines: 
    lane += line.strip()

print(lane[0:10])
print(len(lane))

birthday = input("Enter your birthdate in form ddmmyy: ") 
if birthday in lane:
    print("Your birthday is in first 1000000 numbers of pie")
else:
    print("your birthday is not in first 1000000 numbers of pie")

# ------------------------------------------------------------------------------------------------------

