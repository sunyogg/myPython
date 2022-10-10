import requests

from bs4 import BeautifulSoup

import csv


url = 'https://www.timeout.com/music/best-pop-songs-of-all-time'

source = requests.get(url)

soup = BeautifulSoup(source.text, 'lxml')



songnames = []
singers = []
summaries = []


main_body = soup.find('div', class_="_zoneItems_4w5ul_1 zoneItems")

for article in main_body.find_all('article', class_="tile _article_tpquo_1"):

    artcle = article.find('div', class_="articleContent _articleContent_tpquo_229")
    names = (artcle.div.h3.text)

    # print(names)
    x = names.split("by")
    singer = (x[1])
    singers.append(singer)

    song = x[0]
    u = (song.split('.'))
    song_name = (((u[1].replace("’", "")).replace("‘", "")).replace(u'\xa0', u'')).strip()
    songnames.append(song_name)

    summary = artcle.find('div', class_="summaryCollapsed _summary_tpquo_21")
    for s in  summary.find_all('p')[1:2]:
        summAry = ((s.text))
        summaries.append(summAry)

head = ['Songnames', 'Singer', 'Summary']

with open('most_pop_song.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(head)
    csv_writer.writerows(zip(songnames, singers, summaries))



    # s = article.find('div', class_="_title_tpquo_9")
    # print(s)d



