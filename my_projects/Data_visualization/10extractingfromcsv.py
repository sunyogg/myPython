
# import os

# os.chdir('/Users/sunyoglodhi/Desktop/python/my_work/my_projects/Data_visualization/dowloading_data')
# print(os.getcwd())
# -------------------------------------------------------------------------------------------------------------

# from matplotlib import pyplot as plt

# import csv

# from datetime import datetime

# import matplotlib.ticker as plticker


# station = []
# name = []
# dates = []
# prcp = []
# tavg = []
# tmax = []
# tmin = []

# filename = 'sitka_weather_07-2018_simple.csv'
# with open(filename) as csv_file:
#     csv_reader = csv.DictReader(csv_file)

# # csv_reader = {'STATION': 'USW00025333', 'NAME': 'SITKA AIRPORT, AK US', 'DATE': '2018-07-01', 'PRCP': '0.25', 'TAVG': '', 'TMAX': '62', 'TMIN': '50'}



#     for line in csv_reader:
#         station.append(line['STATION'])
#         name.append(line['NAME'])
#         dates.append(line['DATE'])
#         prcp.append(line['PRCP'])
#         tavg.append(line['TAVG'])
#         tmax.append(float(line['TMAX']))
#         tmin.append(line['TMIN'])



# days = []
# for date in dates:
#     x = datetime.strptime(date, '%Y-%m-%d')
#     days.append(x)

# plt.plot(days, (tmax), label='max temp')

# plt.legend()

# plt.xlabel("Days")
# plt.ylabel("Temperature")
# plt.title("Daily high temperature of july 2018")

# plt.gcf().autofmt_xdate()
# plt.show()


# -------------------------------------------------------------------------------------------------------------


import csv 

from datetime import datetime

import matplotlib.pyplot as plt


datestr = []
tmax = []
tmin = []

# 
filename = 'death_valley_2018_simple.csv'
with open('downloading_data/death_valley_2018_simple.csv') as csv_file:
    csv_reader = csv.reader(csv_file)

    # To skip the header line
    next(csv_reader)

    
    for line in csv_reader:
        datestr.append(line[2])
        tmax.append(float(line[4]))
        tmin.append(float(line[5]))

# converting the normal date in string type to datetime type.
datet = []
for date in datestr:
    x = datetime.strptime(date, '%Y-%m-%d')
    datet.append(x)


# plotting the graph
plt.plot(datet, tmax, label='Max temp')
plt.plot(datet, tmin, label='Min temp')

plt.xlabel("Date")
plt.ylabel("Temperature; high and low")
plt.title("High and low temperture data of year 2018.")

plt.legend(title='Description')

plt.fill_between(datet, tmax, tmin, color='pink', alpha=0.7)
plt.gcf().autofmt_xdate()

plt.show()


# -------------------------------------------------------------------------------------------------------------q






















"""

try :
    count = 0
    for l in tmax:
        float(l)
        count += 1
except ValueError:
    print('error at', count)
"""