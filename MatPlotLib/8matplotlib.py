
# from matplotlib import pyplot as plt
# import numpy as np

# x = np.random.randint(100, size=100)
# y = np.random.randint(100, size=100)
# sizes = 10 * np.random.randint(100, size=100)
# colors = np.random.randint(100, size=100)



# plt.scatter(x, y, s=sizes, alpha=0.50, c=colors, cmap='Blues')

# plt.colorbar()

# plt.show()

# ----------------------------------------------------------------------------------

# from matplotlib import pyplot as plt

# x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
# y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

# colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]

# sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
#          538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

# plt.scatter(x, y, s=sizes, c=colors, cmap='Greens', edgecolor='k', lw=1, alpha=0.75)

# cbar = plt.colorbar()
# cbar.set_label('Satisfaction')

# plt.show()

# ----------------------------------------------------------------------------------
# from csv file

# from matplotlib import pyplot as plt

# import csv

# view_count = []
# likes = []
# ratio = []

# with open('data8.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
# # csv_reader = {'view_count': '8036001', 'likes': '324742', 'ratio': '96.91'}
#     for line in csv_reader:
#         view_count.append(int(line['view_count']))
#         likes.append(int(line['likes']))
#         ratio.append(float(line['ratio']))




# plt.scatter(view_count, likes, edgecolor='k', lw=1, c=ratio, cmap='summer_r')

# plt.xscale('log')
# plt.yscale('log') 

# plt.xlabel('View Count')
# plt.ylabel('Likes')

# cbar = plt.colorbar()
# cbar.set_label('Like/Dislike Ratio')

# plt.title('Views to likes ratio scatter plot.')

# plt.show()

# ----------------------------------------------------------------------------------


from matplotlib import pyplot as plt
#from random import randint
from numpy import random

y = [y for y in (random.randint(1, 6, size = 100))]

x = [x for x in range(100)]
bin = [1,2,3,4,5]


plt.hist(y, bins=bin, edgecolor='red')

plt.xlabel('Dices')
plt.ylabel('Number of occurence')

plt.grid(axis='y')

plt.show()



# plt.scatter(y, x)

# plt.show()