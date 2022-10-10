
from matplotlib import pyplot as plt

import csv

import requests

from bs4 import BeautifulSoup





url = 'https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos'

source = requests.get(url)



# let's create a csv file to store data
header = ['video_name', 'uploader', 'views', 'upload_date']
csv_file = open('pop_yt_vid.csv', 'w') 
csv_writer = csv.writer(csv_file)
csv_writer.writerow(header)

soup = BeautifulSoup(source.text, 'lxml')

# accessing  table
table = soup.find('table', class_='wikitable sortable')

# accessing  table body
body = table.find('tbody' )

video_names = []
uploaders = []
views = []
dates = []

# getting all those row inside table body
for tr in body.find_all('tr')[1:]:

    # for video_name
    for td in tr.find_all('td')[1:2] :
        video_name = (td.text.strip().replace('"',''))

        # for view count
        for td in tr.find_all('td')[3:4]:
            view_count = (td.text)

        # for upload date
        for td in tr.find_all('td')[4:5]:
            upload_date = (td.text)


        # for uploader
        for td in tr.find_all('td')[2:3] :
            try: 
                u = (td.a['title'])
            except TypeError:
                for td in tr.find_all('td')[2:3] :
                    uploader = (td.text)
            else:
                uploader = u 

            uploaders.append(uploader)
            video_names.append(video_name)
            views.append(view_count)
            dates.append(upload_date)

updated_vn = []

for element in video_names:
    x = element.split('[')
    updated_vn.append(x[0])


csv_writer.writerows(zip(updated_vn, uploaders, views, dates))






csv_file.close()


# caption = (table.caption.text)




# problem :
# all the rows have same tag, but none of them have class name, that means 
# it is very difficult to differentiatebetween or access all the tags.




views = []
uploader = []

with open('pop_yt_vid.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        views.append(float(line['views']))
        uploader.append(line['uploader'])

fig, ax = plt.subplots()
ax.bar((uploader[:10] ), views[:10], color='pink', edgecolor='red')

ax.set_xlabel("Uploader")
ax.set_ylabel("Number of views (In Billion)")
ax.tick_params(axis='x', rotation=90)
# fig.autofmt_xdate(bottom=0.2, rotation=90, ha='right')
ax.grid(axis='y')

ax.set_title("Most popular songs of YouTube as of 22 may 2022.")

plt.tight_layout()

plt.show()





























# print(video_name)
        # if type(video_name) == list:
        #     video_name = 'list'
        #     # for td in tr.find_all('td')[1:2]:
        #     #     video_name = td.text.strip()
        # else:
        #     video_name = video_name










# print()
# print()
# print(updated_vn)
# print()
# print()
# print(uploaders)
# print()
# print()
# print(views)
# print()
# print()
# print(dates)
# print()
# print()