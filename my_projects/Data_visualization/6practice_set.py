
from matplotlib import pyplot as plt

from random import choice



class RandomWalk:
    """A class for random walk."""

    def __init__(self, ranges=500):
        self.ranges = ranges

        self.x_value = [0]
        self.y_value = [0]


    def get_step(self):
        """This method will do all the calculation for the random walk."""

        self.x_direction = choice([1, -1])
        self.x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.x_step = self.x_direction * self.x_distance

        return self.x_step


    def fill_walk(self):
        """This method will append the x and y values in the list."""

        while len(self.x_value) <= self.ranges:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step and y_step == 0 :
                continue

            self.x_value.append(self.x_value[-1] + x_step)
            self.y_value.append(self.y_value[-1] + y_step)

            


rw = RandomWalk()

rw.fill_walk()




fig, ax = plt.subplots()

ax.scatter(rw.x_value, rw.y_value)
ax.plot(rw.x_value, rw.y_value, c='red')
ax.scatter(rw.x_value[0],rw.y_value[0] , s=100, c='red')
ax.scatter(rw.x_value[-1],rw.y_value[-1] , s=100, c='black')

ax.set_title("Random Walk.", size=25)

# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)

plt.show()


    


            


