
import requests

from bs4 import BeautifulSoup

import csv

url = 'https://dontrepeatyourself.org/post/10-best-python-books-for-beginners-and-advanced-programmers/'

source = requests.get(url)

soup = BeautifulSoup(source.text, 'lxml')

# print(soup.prettify())


csv_file = open('top_python_books.csv', 'w')
header = ['Title', 'Level', 'Rating', 'Price', 'Link']
csv_writer = csv.writer(csv_file)
csv_writer.writerow(header)


titles = []
links = []
prices = []
ratings = []
levels = []


card_body = soup.find('div', class_='card-text mt-5')


for mains in  card_body.find_all('h2')[:-1]:
    title = (mains.u.a.text)
    titles.append(title)
    link = (mains.u.a['href'])
    links.append(link)

for p in card_body.find_all('p'):
    try:
        if (p.strong.text) == 'Price':
            # print(card_body.index(p))
            price = (p.text).split(':')[1].strip()
            prices.append(price)

        if (p.strong.text) == 'Amazon Stars':
            rating = p.text
            rating = (rating.split(':')[1].strip())
            ratings.append(rating)

        if p.strong.text == 'Difficulty Level':
            level = p.text
            level = (level.split(':')[1].strip())
            levels.append(level)
 
    except:
        pass

csv_writer.writerows(zip(titles, levels, ratings, prices, links))


csv_file.close()