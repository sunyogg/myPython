
import os
os.chdir('/Users/sunyoglodhi/Desktop/python/my_work/my_practice/intermediate_python_topics/csv')

# ----------------------------------------------------------------------------------------------------------------------------------------

'''
filename = 'hell.txt'

with open(filename) as file:
    content = file.read()

print(content)
'''
# ----------------------------------------------------------------------------------------------------------------------------------------




'''
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
# (most likely due to a circular import)
# print(csv_reader) maybe it behaves like a generator
    for line in csv_reader:
        print(line)
'''



'''
import csv

with open('names.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    # csv_reader are list of of all those values separated by commas
    # one line equals one list.
    
    next(csv_reader)
    # to skip the first line  while iterating through the csv file. 

    for value_list in csv_reader:
        print(value_list)

# ----------------------------------------------------------------------------------------------------------------------------------------
import csv

# with open('new_names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='-')
#     for line in csv_reader:
#         print(line)


with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_csv_file:
        csv_writer = csv.writer(new_csv_file, delimiter='-')

        next(csv_reader)

        for line in csv_reader:
            csv_writer.writerow(line)

# ----------------------------------------------------------------------------------------------------------------------------------------

import csv

with open('names.csv', 'r') as csv_file:

    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)
'''
# ----------------------------------------------------------------------------------------------------------------------------------------

# csv.reader -> line is a list
# csv.DictReader -> line is a Dictionary

# DictReader will create a dictionary with KEYS being the values of first line
# of csv file separated by commas and VALUES being all the values of the csv
# file separated by commas after the first line.

# If we pass fieldnames  as argument inside DictWriter, then it'll create
# a header of all those values inside that fieldname list but we will also
# need to call a function writeheader() to create those header in the csv
# file or else it won't create any header. We wil also need to make sure
# that the number of values(header) inside fieldname list are equal to the 
# number of delimiter separated values.

import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    fieldname = ['first_name', 'last_name']

    with open('new_names.csv', 'w') as new_csv_file:
        csv_writer = csv.DictWriter(new_csv_file, fieldnames=fieldname, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)

# ----------------------------------------------------------------------------------------------------------------------------------------






