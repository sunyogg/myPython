from matplotlib import pyplot as plt

from matplotlib import dates as mpl_dates

import datetime

import csv


# dates = [
#     datetime(2019, 5, 24),
#     datetime(2019, 5, 25),
#     datetime(2019, 5, 26),
#     datetime(2019, 5, 27),
#     datetime(2019, 5, 28),
#     datetime(2019, 5, 29),
#     datetime(2019, 5, 30)
# ]

# y = [0, 1, 3, 4, 6, 5, 7]


# plt.plot_date(dates, y, linestyle='solid', markersize=3, mec='r')

# # You can make the dates for readable by alligning them vertically using
# # the code written below.
# plt.gcf().autofmt_xdate()

# # You can format the way dates look with help of code written below.
# date_format = mpl_dates.DateFormatter('%d, %b %Y')
# plt.gca().xaxis.set_major_formatter(date_format)

# plt.grid(axis='y')

# plt.show()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



with open('data9.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    dates = []
    open = []
    high = []
    low = []
    close = []
    adj_Close = []
    volume = []

# {'Date': '2019-05-18', 'Open': '7266.080078', 'High': '8281.660156', 'Low': '7257.259766', 'Close': '8193.139648', 'Adj Close': '8193.139648', 'Volume': '723011166'}

# The dates are in string format and you can probably check that by passing a 
# date 2019-05-17 with data after 2019-05-31 it will not get sort and in the
# graph 17 will come after 31

    for line in csv_reader:
        dates.append((line['Date']))
        open.append(float(line['Open']))
        high.append(float(line['High']))
        low.append(float(line['Low']))
        close.append(float(line['Close']))
        adj_Close.append(float(line['Adj Close']))
        volume.append(float(line['Volume']))


# Since the dates are in string format, you can sort them using the code written
# below.

datef = []
for datel in dates:
    dtt = datetime.datetime.strptime(datel, '%Y-%m-%d' )
    datef.append(dtt.date())

# You're getting None because list.sort() it operates in-place, meaning that 
# it doesn't return anything, but modifies the list itself. You only need to 
# call a.sort() without assigning it to a again.
# find the difference between 
# a = a.sort() == a = a.sorted()
# and  
# a.sort()

plt.xkcd()

datef.sort()

plt.plot_date(datef, close, linestyle='solid', ms=3, mec='r')

plt.gcf().autofmt_xdate()

plt.show()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------