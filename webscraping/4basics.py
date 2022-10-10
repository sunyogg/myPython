import requests

from bs4 import BeautifulSoup

import csv






head = ['title', 'summary', 'yt_link']

with open('corey_web_data.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=';')
    csv_writer.writerow(head)


    source = requests.get('https://coreyms.com').text

    soup = BeautifulSoup(source, 'lxml')


    for article in soup.find_all('article'):
        
        main = []

        """This is for title."""
        title = (article.header.h2.a.text)

        """This is for summary."""
        summary = article.div.p.text

        """This is for the video link"""

        yt_link = soup.find('iframe', class_='youtube-player')['src']
        yt_link = yt_link.split('/')
        yt_link = yt_link[4]
        yt_link = yt_link.split('?')
        yt_id = yt_link[0]

        yt_address = f'https//youtube.com/watch?v={yt_id}'

        main.append((title))
        main.append((summary))
        main.append((yt_address))

        csv_writer.writerow(main)