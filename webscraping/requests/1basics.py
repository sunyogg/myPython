
# Some high level stuff continue later.


import requests

url = 'https://imgs.xkcd.com/comics/python.png'

source = requests.get(url)











# print(source.status_code)
# print(source.ok)
# print(source.headers)


# print((source.content))
# with open('comic.png', 'wb') as f:
#     f.write(source.content)