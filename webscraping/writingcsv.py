import csv

# -----------------------------------------------------------------------

head = ['first', 'second', 'third', 'fourth', 'fifth']

with open('writingcsv.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=';')

    csv_writer.writerow(head)

# ----------------------------------------------------------------------- 

head = ['first', 'second', 'third', 'fourth', 'fifth']

csv_file = open('csv_file.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(head)

csv_file.close()

# -----------------------------------------------------------------------