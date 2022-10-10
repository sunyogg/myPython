import os
'''
# os.getcwd(), where cwd stands for current working directory
# so this function prints the path of current working directory 
print(f" -> {os.getcwd()}")


# os.chdir(), where chdir stands for change directory
# this function changes the current working directory to the desired directory.
os.chdir('/Users/sunyoglodhi/Desktop/python/my_work/my_practice/modules')
print("->",os.getcwd())'''


# os.listdir()
# this function print the list of items inside a directory
print(f"-> {os.listdir('/Users/sunyoglodhi/Desktop/python/my_work/my_practice/modules')}")