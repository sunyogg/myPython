from bs4 import BeautifulSoup

with open('data/simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    # inside parenthesis(file_object, parser_you_wanna_use)
# print(soup.prettify())
# soup returned the html file of the site, and we can work on those html
# file usinng BeautifulSoup, like when we want to access the text of certain
# site of anything like that

# match = soup.title.text

# match = soup.div

# but what if we want to find div tag that has class footer in it.
# match = soup.find('div')
# With the method above we will only get the first div tag of the page.
# we will also need to specify the class of that tag, to find that particular
# tag.
article = soup.find('div', class_='article')
# article is everything inside div tag of class article
# print(article)
# it will return None it it does have a div tag with class footer



# headline = article.h2.a.text
# print(headline)

# summary = article.p.text
# print(summary)



elements = soup.find_all('div', class_ = 'article')
# element is now a list
for element in elements:
    print(element.h2.a.text)
    print(element.p.text)
    print()