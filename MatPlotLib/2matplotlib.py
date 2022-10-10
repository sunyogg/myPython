
from matplotlib import pyplot as plt

# ----------------------------------------------------------------------------------------------------------------------------------------

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [37732, 41247, 45372, 48876, 50142, 53850, 57287, 63016, 65998, 67003, 69000]
py_dev_y = [48876, 53850, 57287, 63016, 64234, 65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [43515, 46823, 49293, 53437, 54788, 56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(dev_x, py_dev_y, label='Python', width=0.7)
plt.bar(dev_x, js_dev_y, label='Javascript', width=0.7)
plt.bar(dev_x, dev_y, label='All dev', width=0.7)

plt.xlabel('Age')
plt.ylabel('Salary($)')

plt.legend()

plt.grid(axis='y', color='black', ls='--')

plt.show()


# ----------------------------------------------------------------------------------------------------------------------------------------
# study more about: 
# xtics 
# managing while introducing more bars in same graph.


import numpy as np 

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(dev_x)) 
# [0 1 2 3 4 5 6 7 8 9 10]
# [-0.75, 0, 0.25] [0.75, 1, 1.25]

bar_width = 0.25
# width = 100/((no.of bar + 1)*100)

dev_y = [37732, 41247, 45372, 48876, 50142, 53850, 57287, 63016, 65998, 67003, 69000]
py_dev_y = [48876, 53850, 57287, 63016, 64234, 65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [43515, 46823, 49293, 53437, 54788, 56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(x_indexes - bar_width, py_dev_y, label='Python', width = bar_width)
plt.bar(x_indexes, js_dev_y, label='Javascript', width = bar_width)
plt.bar(x_indexes + bar_width, dev_y, label='All dev', width = bar_width)

plt.xlabel('Age')
plt.ylabel('Salary($)')

plt.title("Median salary($) by age." )

plt.legend()

plt.grid(axis='y', color='black', ls='--')

plt.xticks(ticks=x_indexes, label=dev_x)

plt.show()

# ----------------------------------------------------------------------------------------------------------------------------------------
