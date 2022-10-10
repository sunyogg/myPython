

from matplotlib import pyplot  as plt

import csv


with open('data6.csv') as csv_file:

    csv_reader = csv.DictReader(csv_file)
# csv_reader = {'Age': '18', 'All_Devs': '17784', 'Python': '20046', 'JavaScript': '16446'}

    age_x = []
    all_dev_salary = []
    py_dev_salary = []
    js_dev_salary = []

    for line in csv_reader:

        age_x.append(int(line['Age']))
        all_dev_salary.append(int(line['All_Devs']))
        py_dev_salary.append(int(line['Python']))
        js_dev_salary.append(int(line['JavaScript']))

        # Research on why i put int() below, it was very difficult to 
        # find out the solution but as always, stackoverflow rocks.
        # or check straightlineerror.py


    # print((age_x))
    # print((all_dev_salary))
    # print((py_dev_salary))
    # print((js_dev_salary))



plt.plot(age_x, all_dev_salary, label='All dev salary', c='k', lw=2, ls='--')
plt.plot(age_x, py_dev_salary, label='Python salary',c='r', lw=2, ls='-.')
plt.plot(age_x, js_dev_salary, label='Javascript salary',c='orange', lw=2)

overall_py_median = 57287

y = tuple(py_dev_salary)

plt.fill_between(age_x, py_dev_salary, js_dev_salary, alpha=0.25)

plt.xlabel('Age')
plt.ylabel('Salary')

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()













































'''
age = ['18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55']

all_dev_salary = ['17784', '16500', '18012', '20628', '25206', '30252', '34368', '38496', '42000', '46752', '49320', '53200', '56000', '62316', '64928', '67317', '68748', '73752', '77232', '78000', '78508', '79536', '82488', '88935', '90000', '90056', '95000', '90000', '91633', '91660', '98150', '98964', '100000', '98988', '100000', '108923', '105000', '103117']

py_dev_salary = ['20046', '17100', '20000', '24744', '30500', '37732', '41247', '45372', '48876', '53850', '57287', '45000', '50000', '55000', '70000', '71496', '75370', '83640', '84666', '84392', '78254', '85000', '87038', '91991', '100000', '94796', '97962', '93302', '99240', '102736', '112285', '100771', '104708', '108423', '101407', '112542', '122870', '120000']

js_dev_salary = ['16446', '16791', '18942', '21780', '25704', '29000', '34372', '37810', '43515', '46823', '49293', '53437', '56373', '62375', '66674', '68745', '68746', '74583', '79000', '78508', '79996', '80403', '83820', '88833', '91660', '87892', '96243', '90000', '99313', '91660', '102264', '100000', '100000', '91660', '99240', '108000', '105000', '104000']
'''
# ----------------------------------------------------------------------------------------------------------------------------------
