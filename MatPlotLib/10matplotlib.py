import matplotlib.pyplot as plt

import csv

from itertools import count

from random import randint

from matplotlib.animation import FuncAnimation

x_vals = []
y_vals = []

index = count()

def animate(i):
    x_vals.append(next(index))
    y_vals.append(randint(0, 100000))
    plt.cla()
    plt.plot(x_vals, y_vals, marker='*', ms=3)


# Makes an animation by repeatedly calling a function *func*.
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()

plt.xlabel('Time')
plt.ylabel('Subscriber count')

plt.show()

# continue later

#--------------------------------------------------------------------------------------------