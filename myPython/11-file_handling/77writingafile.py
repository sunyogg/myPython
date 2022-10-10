# writing a file
filename = 'writehere.txt'
with open(filename,'w') as file:
    file.write('I love python')

# ------------------------------------------------------------------------------------
# writing multiple lines
filename = 'writehere.txt'
with open(filename,'w') as file:
    file.write('\tI love python.\n')
    file.write('I love programming.\n')

    #  The second argument, 'w', tells Python that we want to open 
    #  the file in write mode.

# ------------------------------------------------------------------------------------
# appending to a file

filename = 'writehere.txt'
with open(filename,'a') as file:
    file.write('I love finding meaning in large data sets\n')
    file.write('I love creating apps that can run on browser.\n') 

# ------------------------------------------------------------------------------------