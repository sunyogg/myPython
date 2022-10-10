
# 9.13

from random import randint as rand

# creating a class that represents a dice of certain sides
class Dice():
    
    # this method will define the sides of the dice that we want to roll
    def __init__(self,sides = 6):
        self.sides = sides

    # this function will roll the dice and choose the random number between 0 and
    # the number of sides of the dice
    def roll_dice(self):
        a = rand(0,self.sides)
        print(a)

# rolling a 6 sided dice
dice1 = Dice()
dice1.roll_dice()

# rolling a 10 sided dice
dice10 = Dice(10)
dice10.roll_dice()

# rolling a 20 sided dice
dice20 = Dice(20)
dice20.roll_dice()

# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# 9.14 

from random import choice

lottery  = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e']

w = choice(lottery)
x = choice(lottery)
y = choice(lottery)
z = choice(lottery)

winner = w+x+y+z

print("Any ticket matching",winner,"wins the prize.")

    

# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# 9.15

from random import choice

lottery  = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e']

winner = 'abc7'
times = 0
while True:
    w = choice(lottery)
    x = choice(lottery)
    y = choice(lottery)
    z = choice(lottery)
    chicken = w+x+y+z
    print(chicken)
    times += 1

    if chicken != winner:
        continue
    else:
        print("found winner in",times,"times")
        break


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

from random import choice
lottery = ['1','2','3']

winner = '12'
times = 0

while True:
    p = choice(lottery)
    q = choice(lottery)

    comb = p+q
    print(comb)

    if comb != winner:
        times += 1
        continue
    else:
        print(f"Found the winner {comb} in {times + 1}")
        break

# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––