
# from matplotlib import pyplot as plt

# import csv

# from datetime import datetime

# wind = []
# date = []

# with open('downloading_data/sitka_weather_2018_full.csv') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     next(csv_reader)


#     for line in csv_reader:
#         current_date = datetime.strptime(line[2], '%Y-%m-%d')

#         try:
#             x = float(line[5])
#         except ValueError:
#             print("error at date", current_date)
#         else:
#             wind.append(x)
#             date.append(current_date)


# fig, ax = plt.subplots()

# ax.plot(date, wind, label='Rain')

# ax.set_title('Daily rainfall amount of Sitka rainforest.')
# ax.set_xlabel("Dates")
# ax.set_ylabel("Rainfall")

# plt.legend()

# plt.gcf().autofmt_xdate()

# plt.show()

# --------------------------------------------------------------------------------------------


# from matplotlib import pyplot as plt

# import csv

# from datetime import datetime

# sitka = 'downloading_data/sitka_weather_2018_full.csv'
# deathvalley = 'downloading_data/death_valley_2018_full.csv'


# dtmax = []
# dtmin = []
# stmax = []
# stmin = []
# date = []
# sdate = []


# with open(deathvalley) as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     for line in csv_reader:
#         current_date = (datetime.strptime(line['DATE'], '%Y-%m-%d'))
        
#         try:
#             x = (float(line['TMAX']))
#             y = (float(line['TMIN']))
#         except ValueError:
#             print(f"data missing at {current_date} in deathvalley.")
#         else:
#             dtmax.append(x)
#             dtmin.append(y)
#             date.append(current_date)


# with open(sitka) as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     for line in csv_reader:
#         current_date = (datetime.strptime(line['DATE'], '%Y-%m-%d'))
        
#         try:
#             x = (float(line['TMAX']))
#             y = (float(line['TMIN']))
#         except ValueError:
#             print(f"data missing at {current_date} in sitka.")
#         else:
#             stmax.append(x)
#             stmin.append(y)
#             sdate.append(current_date)
        
# fig, ax = plt.subplots()
# ax.plot(date, dtmax, label='dv_max')
# ax.plot(date, dtmin, label='dv_min')
# ax.plot(sdate[0:len(date)] ,stmax[0:len(dtmax)], label='st_max')
# ax.plot(sdate[0:len(date)], stmin[0:len(dtmin)], label='st_min')

# fig.autofmt_xdate()

# ax.fill_between(date, dtmax, dtmin, color='blue', alpha=0.3,
#     label='deathvalley')
# ax.fill_between(sdate[0:len(date)], stmax[0:len(dtmax)], stmin[0:len(dtmin)], 
#     color='black', alpha=0.3, label='sitka')

# ax.set_title("Max and min temperature of Sitka rainforest and Death valley")
# ax.set_xlabel('Date')
# ax.set_ylabel('Temperature')

# ax.legend()

# ax.grid(True)

# plt.show()

# --------------------------------------------------------------------------------------------


from matplotlib import pyplot as plt

import csv

from datetime import datetime

sitka = 'downloading_data/sitka_weather_2018_full.csv'
deathvalley = 'downloading_data/death_valley_2018_full.csv'


dtmax = []
dtmin = []
stmax = []
stmin = []
date = []
sdate = []


with open(deathvalley) as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        current_date = (datetime.strptime(line['DATE'], '%Y-%m-%d'))
        
        try:
            x = (float(line['TMAX']))
            y = (float(line['TMIN']))
        except ValueError:
            print(f"data missing at {current_date} in deathvalley.")
        else:
            dtmax.append(x)
            dtmin.append(y)
            date.append(current_date)


with open(sitka) as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        current_date = (datetime.strptime(line['DATE'], '%Y-%m-%d'))
        
        try:
            x = (float(line['TMAX']))
            y = (float(line['TMIN']))
        except ValueError:
            print(f"data missing at {current_date} in sitka.")
        else:
            stmax.append(x)
            stmin.append(y)
            sdate.append(current_date)
        
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharey=True)
ax1.plot(date, dtmax, label='dv_max')
ax1.plot(date, dtmin, label='dv_min')
ax2.plot(sdate[0:len(date)] ,stmax[0:len(dtmax)], label='st_max')
ax2.plot(sdate[0:len(date)], stmin[0:len(dtmin)], label='st_min')

fig.autofmt_xdate()

ax1.fill_between(date, dtmax, dtmin, color='blue', alpha=0.3,
    label='deathvalley')
ax2.fill_between(sdate[0:len(date)], stmax[0:len(dtmax)], stmin[0:len(dtmin)], 
    color='black', alpha=0.3, label='sitka')

ax1.set_title("Max and min temperature of Sitka rainforest and Death valley")
ax2.set_xlabel('Date')
ax1.set_ylabel('Temperature')
ax2.set_ylabel('Temperature')

ax1.legend()
ax2.legend()

ax1.grid(True)
ax2.grid(True)

plt.show()

# --------------------------------------------------------------------------------------------

        
