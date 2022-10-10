import requests

from bs4 import BeautifulSoup

import csv

from matplotlib import pyplot as plt

# print(source.status_code)



url = 'https://www.scrapethissite.com/pages/forms/?per_page=100'


source = requests.get(url)

soup = BeautifulSoup(source.text, 'lxml')

head = ['teamname', 'years', 'wins', 'losses', 'win%', 'goals_for',
        'goal_against' ]

csv_file = open('team_data.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(head)


team_n = []
year = []
wins = []
losses = []
win_pct = []
goals_for = []
goals_against = []

teamname = soup.find('table', class_='table')

for tr in teamname.find_all('tr', class_="team"):
    for td in tr.find_all('td', class_='name'):
        team_n.append(td.text.strip())

    for td in tr.find_all('td', class_='year'):
        year.append(int(td.text.strip()))

    for td in tr.find_all('td', class_='wins'):
        wins.append(int(td.text.strip()))

    for td in tr.find_all('td', class_='losses'):
        losses.append(int(td.text.strip()))

    for td in tr.find_all('td', class_='pct text-success'):
        win_pct.append(float(td.text.strip()))

    for td in tr.find_all('td', class_='pct text-danger'):
        win_pct.append(float(td.text.strip()))

    for td in tr.find_all('td', class_='gf'):
        goals_for.append(int(td.text.strip()))

    for td in tr.find_all('td', class_='ga'):
        goals_against.append(int(td.text.strip()))

# appending data to csv, i thougt it was easier but it is hella difficult
# zip function just made my day.

csv_writer.writerows(zip(team_n, year, wins, losses ,win_pct ,goals_for, 
        goals_against)) 


csv_file.close()

teamnamee = []
winss = []

with open('team_data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        teamnamee.append(line['teamname'])
        winss.append(int(line['wins']))
        


plt.bar(teamnamee[:10], winss[:10])

plt.xlabel('Teams')
plt.ylabel('No. of Wins')
plt.title("Wins by teams")

plt.show()

        




























# IF we had same tags with same classes.
# for tr in teamname.find_all('tr', class_="team"):
#     print(teamname.td.text.strip())
#     print(teamname.td[1].text.strip())
#     print(teamname.td[2].text.strip())
#     print(teamname.td[3].text.strip())
#     print(teamname.td[4].text.strip())