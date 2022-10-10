from matplotlib import pyplot as plt

import matplotlib

from bs4 import BeautifulSoup

import requests

import csv


# accessing the html_object of the website
source = requests.get('https://www.scrapethissite.com/pages/simple/').text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify)

countries = []
pops = []

# scrapping the countres name data
for element in soup.find_all('h3', class_='country-name'):
    countries.append((element.text.strip()))
    
# scrapping the population data
for element in soup.find_all('span', class_='country-population'):
    pops_str = (element.text.strip())
    pops_int = int(pops_str)
    pops.append(pops_int)


# print(len(countries))
# print(len(pops))

# creating a csv file to store the data that we scrapped.
head = ['country', 'population']
csv_file = open('countries_pop_data.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(head)


# storing the scrapped data in csv file. 
for i in range(len(countries)):
    csv_writer.writerow([countries[i], pops[i]])

csv_file.close()

x = []
y = []


# accessing only those values of csv file that i want to plot on the
# graph.
with open('countries_pop_data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    countries = ['Australia','Canada','China','United Kingdom','India',
    'New Zealand','United States','Philippines','Pakistan']
    for line in csv_reader:
        if line['country'] in countries:
            x.append(line['country'])
            y.append(int(line['population']))
        else:
            continue


fig, ax = plt.subplots()

ax.bar(x, y, width=0.5, edgecolor='red')
ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
ax.set_xlabel('Countries', size=15)
ax.set_ylabel('Population', size=15)

ax.set_title("Bar graph on population of countries.", size=15)
ax.grid(axis='y')
plt.show()



































# getting the values of particular countries that i want to plot the graph of.

# found the index of particular country by using the enumerate method.
# index = [12, 37, 47, 76, 104, 170, 232, 176, 177]
# for  count in x:
#     if x.index(count) in index:
#         quanty.append(count)

# for count in y:
#     if y.index(count) in index:
#         indes.append(count)



"""
12 Australia
37 Canada
47 China
76 United Kingdom
104 India
170 New Zealand
232 United States
176 Philippines
177 Pakistan
"""
