

from plotly.graph_objs import Bar, Layout

from plotly import offline

import random

class Dice:

    def __init__(self, sides=6):
        """Initialize the attributes a dice"""
        self.sides = sides


    def roll_dice(self):
        """This method will roll the dice and return the outcome"""
        result =  random.randint(1, self.sides)
        return result

die1 = Dice()
die2 = Dice()
die3 = Dice()

result = [die1.roll_dice() + die2.roll_dice() + die3.roll_dice() for i in range(10000)]
max_result = die1.sides + die2.sides + die3.sides 

# for i in range(10000):
#     a = die1.roll_dice()
#     b = die2.roll_dice()
#     c = die3.roll_dice()
#     d = a + b + c
#     result.append(d)


frequency = [result.count(s) for s in range(3, (max_result + 1))]

# for s in range(3, (max_result + 1)):
#     num = result.count(s)
#     frequency.append(num)

x_values = [x for x in range(3, (max_result + 1))]
y_values = frequency


data = [Bar({'x':x_values, 'y':y_values})]


my_layout = Layout(title='Result of rolling 3 D6 dices 1000 times.',
    xaxis={'title':'outcomes'}, yaxis={'title':'Probability of Outcomes'})

offline.plot({'data':data, 'layout':my_layout}, filename='D666.html')



