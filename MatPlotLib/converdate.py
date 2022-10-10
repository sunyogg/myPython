
import datetime


dt_str = '2019-05-31'
dt = datetime.datetime.strptime(dt_str, '%Y-%m-%d')


dates = ['2019-05-18', '2019-05-19', '2019-05-20', '2019-05-31']

datel = []

for dat in dates:
    dat = datetime.datetime.strptime(dt_str, '%Y-%m-%d')
    datel.append(dat.date())


print(datel)