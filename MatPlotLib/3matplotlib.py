
# bar graph from csv data file.


import csv
import numpy as np 
from collections import Counter
from matplotlib import pyplot as plt

with open('data3.csv', 'r') as csv_file:

    csv_reader = csv.DictReader(csv_file)
  # csv_reader = {'Responder_id': '1', 'LanguagesWorkedWith': 'HTML/CSS;Java;JavaScript;Python'}

    language_counter = Counter()
    language = []
    user = []
    
    # This loop will count the number of time languages have appereared in
    for file in csv_reader:
        # looping through all the lines in csv_reader
        language_counter.update((file['LanguagesWorkedWith'].split(';')))
        # language_counter.update will update the counter of language_counter
        # everytime the loop is restarted.
        # (file['LanguagesWorkedWith'].split(';')) will return the elments
        # of dictionary having key LanguagesWorkedWith and split those elements
        # from ;

    
    for item in language_counter.most_common(15):
        language.append(item[0])
        user.append(item[1])

    language.reverse()
    user.reverse()



plt.barh(language, user, color='orange', height=0.69)


plt.title("Languages by User Graph" )


plt.xlabel('Users')
plt.ylabel('Languages')


plt.legend()

plt.grid(axis='x', color='black', ls='--')

plt.tight_layout()

plt.show()
# ----------------------------------------------------------------------------------------------