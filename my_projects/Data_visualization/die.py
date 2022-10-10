from matplotlib import pyplot as plt

import random

class Dice:
    """A class representing a singel dice."""

    def __init__(self, sides=6):
        """Assume a six sided dice"""
        self.sides = sides


    def roll_dice(self):
        """Return a random side of the dice from 1 and number of sides."""
        return (random.randint(1, self.sides))













































































# # print(random.randint(1, 8))

# # 2 dices
# # 8 sided
# # roll them 1000 times
# # maybe we should histogram here


# def roll_dice(sides, times):
#     dice1 = []
    
#     for i in range(times):
#         x = random.randint(0, sides)
#         dice1.append(x)

#     return dice1



# fig, ax = plt.subplots()

# bin = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ax.hist(roll_dice(8, 1000), bins=bin, edgecolor='red')

# plt.show()

# ---------------------------------------------------------------------------------------------




