
# Basic Histograms

# from matplotlib import pyplot as plt

# import csv

# ages = [18, 19, 20, 21, 22 ,23, 25, 28, 34, 45, 48, 36, 42, 46, 29, 55, 54, 51, 58]
# bins = [10, 20, 40, 50, 60]


# plt.hist(ages, bins=bins, edgecolor='red')

# plt.xlabel('Ages')
# plt.ylabel('No. of respondents')

# plt.show()

# ----------------------------------------------------------------------------------------------------------------------

from matplotlib import pyplot as plt

import csv

with open('data7.csv') as csv_file:

    csv_reader = csv.DictReader(csv_file)

# csv_reader = {'Responder_id': '1', 'Age': '14'}

    responder_id = []
    age = []

    for line in csv_reader:
        responder_id.append(int(line['Responder_id']))
        age.append(int(line['Age']))
    
bin = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(age, bins=bin, edgecolor='red', log=True, color='pink')

median_age = 29

plt.axvline(median_age, c='black', lw=2, label='Median age')

plt.legend()

plt.xlabel('Age')
plt.ylabel('No. of Respondent')

plt.grid(axis='y')

plt.show()

# ----------------------------------------------------------------------------------------------------------------------