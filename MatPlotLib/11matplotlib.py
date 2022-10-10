# sub plots
# fig are the container holding our plot
# axes are the actual plots
import csv

from matplotlib import pyplot as plt


age = []
all_dev_s = []
js_dev_s = []
py_dev_s = []


with open('data11.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        age.append(int(line['Age']))
        all_dev_s.append(int(line['All_Devs']))
        js_dev_s.append(int(line['JavaScript']))
        py_dev_s.append(int(line['Python']))


# fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

# print(ax)
ax1.plot(age, py_dev_s, label='python')
ax1.plot(age, js_dev_s, label='javascript', ls='--')


ax2.plot(age, all_dev_s, label='All developer')

ax1.set_title("Median salary($) by age")
ax1.set_ylabel('Salary($)')
ax2.set_xlabel('Age')
ax2.set_ylabel('Salary($)')
plt.show()

