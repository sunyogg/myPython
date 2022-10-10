
import random

class Dice:
    """Creating a dice."""

    def __init__(self, times=1, sides=6, count=1):
        """Initializing the attributes"""
        self.times = times
        self.sides = sides
        self.count = count


    def roll_dice(self):
        """Rolling the dice depening on the number of sided and number of dices."""
        # This list will store the sum of the outcomes of both the dices.
        result = []
        # loop for number of times the dice is going to be thrown.
        for i in range(self.times):
            # variable res will be the sum of outcomes of both the dices.
            res = 0
            # loop for number of dices that are going to be thrown.
            for s in range(self.count):
                x = random.randint(0, self.sides)
                res += x
            result.append(res)
        return result



# die = Dice(1, 6, 2)

# # counting the number of times 12 appear i.e. getting 6 in both dice.
# count = 0
# for x in range(1000):
#     s = die.roll_dice().pop()
#     if s == 12:
#         count += 1
# print(count)

# # When dices are thrown 2 times.
# for x in range(10000):
#     s = die.roll_dice().pop()
#     t = die.roll_dice().pop()
#     if s + t == 24:
#         count += 1
# print(count)