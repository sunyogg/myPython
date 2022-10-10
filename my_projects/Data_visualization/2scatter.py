

from matplotlib import pyplot as plt

from numpy import random

plt.style.use('seaborn')

input_vals = [x for x in range(10)]
squares = [s**2 for s in input_vals]
size = [x for x in random.randint(50, 1000, size=10) ]

# input_vals = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()

# cmap=plt.cm.Reds
ax.scatter(input_vals, squares, c=squares, cmap='Reds', s = size)
ax.set_title("Scatter plot")
ax.set_xlabel("x axis")
ax.set_ylabel('y axis')

# set the range for each axis
ax.axis([-2, 11, -10, 110])

# set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()

# ----------------------------------------------------------------------------
