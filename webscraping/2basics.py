
from bs4 import BeautifulSoup

import requests

source = requests.get('https://coreyms.com').text
# this will return the html file of the site coreyms.com

# soup = BeautifulSoup(source, 'lxml')

# summary = soup.find('div', class_ = 'entry-content')
# sumtext = summary.p.text

# heading = soup.find('header', class_='entry-header')
# headtext = heading.h2.a.text

# print('->',headtext)
# print('->',sumtext)
# print()



soup = BeautifulSoup(source, 'lxml')

summary = soup.find_all('div', class_ = 'entry-content')
for x in summary:
    sumtext = x.p.text
    heading = soup.find_all('header', class_='entry-header')
    for s in heading:
        headtext = s.h2.a.text

        print(sumtext)
        print(headtext)
        print()

# continued in 3rd

# -------------------------------------------------------------

# print(soup.article.header.h2.a.text)
# print()
# print(soup.header.h2.a.text)

# heading = soup.find('header', class_='entry-header')
# print(heading.h2.a.text)


# -------------------------------------------------------------