import datetime

# datetime.date()
# ------------------------------------------------------------------------------------------

# d = datetime.date(2018, 11, 20)
# print(d)
# print(d.year)
# print(d.month)
# print(d.day)

# ------------------------------------------------------------------------------------------

# tday = datetime.date.today()
# print(tday)
# # This will return the day of the week.
# print(tday.weekday()) # monday=0, sunday=6
# print(tday.isoweekday()) # monday=1, sunday=7

# ------------------------------------------------------------------------------------------

# tday = datetime.date.today()
# tdelta = datetime.timedelta(days=7)

# print(tday - tdelta)
# print(tday + tdelta)

# # date2 = date1 +- timedelta
# # timedelta = date1 +- date2

# bdate = datetime.date(2022, 11 ,20)

# till_bday = bdate - tday

# print(f"Your birthday in {till_bday.total_seconds()} days.")

# ------------------------------------------------------------------------------------------

# datetime.date() gave us year, month and day without hour, minute, second and microsecond.
# datetime.time() gave us hour, minute, second and microsecond without year, month and day.
# datetime.datetime() will give us access to everything.

# datetime.time()
# 1 second = 1 million microseconds


t1 = datetime.time(6, 20, 30, 100000)

#print(t1)

# ------------------------------------------------------------------------------------------

# datetime.datetime()

dt1 = datetime.datetime(2022, 11, 3 , 15, 25, 30, 10000)
tdelta = datetime.timedelta(days=17)

#print(dt1 + tdelta)

# ------------------------------------------------------------------------------------------

# timezone
import pytz

# dt = datetime.datetime(2022, 11, 3, 6 ,00, 00, tzinfo=pytz.UTC)
# print(dt)

# # best 
# dt_now = datetime.datetime.now(tz=pytz.UTC)
# print(dt_now)

# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)

# ------------------------------------------------------------------------------------------
# Asia/Calcutta

# dt_now = datetime.datetime.now(tz=pytz.UTC)
# # print(dt_now)

# # changing timezone
# dt_in = dt_now.astimezone(pytz.timezone('Asia/Calcutta'))
# # print(dt_in)

# # naive datetime: datetime without timezone info
# # but naive datetime cannot be simply converted using the above method.
# # lets first try to convert using the above method.

# dtt = datetime.datetime.now()
# print(dtt)
# #dt_mount = dtt.astimezone(pytz.timezone('Asia/Calcutta'))
# # print(dtt)
# # In the YouTube video Corey told that the method above won't work but it's
# # working here.


# # another method that is working in the youtube video.
# # this method is not working
# dt_in = pytz.timezone('Asia/Calcutta')

# dtt = dtt.localize(dt_in)

# print(dtt)

# ------------------------------------------------------------------------------------------ 


dt_in = datetime.datetime.now(tz=pytz.timezone('Asia/Calcutta'))
# universally accepted format of writing date time.
# print(dt_in.isoformat())

# different formats of writing datetime
print(dt_in.strftime('%b %d, %Y '))
# print(dt_in.strftime('%c'))
# print(dt_in.strftime('%A %d %B, %Y'))

# ------------------------------------------------------------------------------------------

# Converting a normal datetime string to datetime
dt_str = 'Apr 29, 2022'
dt = datetime.datetime.strptime(dt_str, '%b %d, %Y')
print(dt)

dt_str = '2019-05-31'
dt = datetime.datetime.strptime(dt_str, '%Y-%m-%d')
print(dt)

# strftime() - Datetime to string
# strptime() - string to Datetime

# ------------------------------------------------------------------------------------------