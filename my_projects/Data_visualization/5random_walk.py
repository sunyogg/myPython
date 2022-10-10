from matplotlib import pyplot as plt

from module4_random_walk import RandomWalk


rw = RandomWalk(50000)
rw.fill_walk()

xx = (rw.x_values)
yy = (rw.y_values)
color = [x for x in range(0,50000)]


# plt.scatter(xx, yy, c=color, cmap=plt.cm.Blues)
# # q
# plt.show()


fig, ax = plt.subplots(figsize=(15, 7))
ax.scatter(xx, yy, c=color, cmap=plt.cm.Blues, s=1 )
ax.set_title("Random walk")
# I am not able to add color bar, don't know why, maybe research about it later.
# plt.colorbar()


# Emphasize the first and last point
# just create another scatter graph but for the first and last value
# in the x_values and y_values list and we will color them different.
ax.scatter(0, 0, color='green', s=20)
ax.scatter(rw.x_values[-1], rw.y_values[-1], color='red', s=20)


# remove the axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


plt.show()


















































# My try

# class RandomWalk:

#     def __init__(self, ranges=500):
        
#         self.ranges = ranges
#         self.x_num = [0]
#         self.y_num = [0]


#     def fill_walk(self):

#         while len(self.x_num) <= self.ranges:

#             self.x_direction = choice([1, -1])
#             self.x_distance = choice([0, 1, 2, 3, 4])
#             self.x_travel = self.x_direction * self.x_distance

#             self.y_direction = choice([1, -1])
#             self.y_distance = choice([0, 1, 2, 3, 4])
#             self.y_travel = self.y_direction * self.y_distance

#             if self.x_travel and self.y_travel == 0:
#                 continue

#             self.x_num.append(self.x_num[-1] + self.x_travel)
#             self.y_num.append(self.y_num[-1] + self.y_travel)









