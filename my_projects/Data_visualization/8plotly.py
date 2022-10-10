
from plotly.graph_objs import Bar, Layout

from plotly import offline

from die import Dice

# --------------------------------------------------------------------------------------------------

# create the Dice instance
die1 = Dice()
result = []
for i in range(100):
    result.append((die1.roll_dice()))

# analyze the result.
frequency = []
for i in range(1, (die1.sides + 1)):
    frequency.append((result.count(i)))


# visualize the result
# x_values = [1, 2, 3, 4, 5, 6]
# frequency     = [25, 12, 20, 12, 15, 16]

x_values = list(range(1, (die1.sides + 1)))
data = [Bar(x=x_values, y=frequency)]

x_axis_config = {'title':'result'}
y_axis_config = {'title':'frequency of result'}

my_layout = Layout(title="Result of rolling one D6 100 times.",
        xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data':data, 'layout':my_layout}, filename='d6.html')

# --------------------------------------------------------------------------------------------------

die1 = Dice()
die2 = Dice()

result = []

max_result = die1.sides + die2.sides

for i in range(100000):
    a = die1.roll_dice()
    b = die2.roll_dice()
    c = a + b
    result.append(c)

frequencies = []
for i in range(2,  (max_result + 1)): # use max(result) only when using a large amount of data. so that possibility of max value is their.
    x = result.count(i)
    frequencies.append(x)
    
# visualize the result
x_values = [x for x in range(2, 13)]
y_values = frequencies

data = [Bar(x=x_values, y=y_values)]
my_layout = Layout(title="Result of rolling two D6 dices 1000 times.", 
    xaxis={'title':'result', 'dtick':1}, yaxis={'title':'frequency of result.'})
offline.plot({'data':data, 'layout':my_layout},  filename='d66.html')

# data = type of graph, x_values and y_values
# layout = title, xaxis_description, yaxis_description

# --------------------------------------------------------------------------------------------------