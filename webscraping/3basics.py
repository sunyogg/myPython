
from bs4 import BeautifulSoup

import requests


source = requests.get('https://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

article = soup.find('article')

"""This is for the heading"""
heading = article.header.h2.a.text
# print()

"""This is for the summary"""
summary = article.div.p.text

"""This is for the link"""
# you can access attributes like a dictionary
yt_link = (article.div.span.iframe)['src']
# or we could have used
#yt_link = soup.find('iframe', class_="youtube-player")['src']

yt_link = yt_link.split('/')[4]
vid_id = yt_link.split('?')[0]


real_yt_link = f'https://youtube.com/watch?v={vid_id}'

print(heading)
print(summary)
print(real_yt_link)









