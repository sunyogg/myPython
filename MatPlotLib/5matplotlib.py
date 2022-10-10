
# from matplotlib import pyplot as plt

# # x
# days =     [1, 2, 3, 4, 5, 6, 7]

# # y
# emp1 =   [1, 3, 2, 4, 1, 2, 3]
# emp2 =   [7, 8, 6, 9, 12, 7, 7]
# emp3 =   [4, 5, 4, 3, 2, 1, 6]
# emp4 =   [7, 5, 8, 6, 8, 8, 6]
# emp5 =   [1, 3, 2, 1, 1, 5, 1]

# label = ['emp1', 'emp2', 'emp3', 'emp4', 'emp5']

# plt.stackplot(days, emp1, emp2, emp3, emp4, emp5, labels=label)

# plt.grid(True)

# plt.legend(loc='upper right')

# plt.xlabel('days') 
# plt.ylabel('hours')

# plt.title('Stackplot')

# plt.show()

# ------------------------------------------------------------------------------------------------------

# from matplotlib import pyplot as plt


# day =     [1, 2, 3, 4, 5, 6, 7, 8, 9]

# player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
# player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
# player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

# label = ['player1', 'player2', 'player3']


# plt.stackplot(day, player1, player2, player3, labels=label)

# plt.xlabel('Days')
# plt.ylabel('Points')

# plt.grid(True)

# plt.legend(loc=(0.07, 0.05))

# plt.tight_layout()

# plt.title('Stackplot')

# plt.show()

# ------------------------------------------------------------------------------------------------------

from matplotlib import pyplot as plt


day = [1, 2, 3, 4, 5, 6, 7, 8, 9]

dev1 = [0, 2, 3, 3, 4, 4, 4, 4, 5]
dev2 = [0, 1, 1, 1, 2, 2, 2, 3, 4]
dev3 = [1, 1 ,1, 2, 2, 2, 3, 3, 3]

label = ['dev1', 'dev2', 'dev3']

plt.stackplot(day, dev1, dev2, dev3, labels=label)

plt.legend()

plt.xlabel('Days')
plt.ylabel('hours')

plt.title('Stackplot')

plt.grid(True)

plt.show()

# ------------------------------------------------------------------------------------------------------

# Here are all of the locations for legend (according to documentation):
# 'best'
# 'upper right'
# 'upper left'
# 'lower left'
# 'lower right'
# 'right'
# 'center left'
# 'center right'
# 'lower center'
# 'upper center'
# 'center'

# ------------------------------------------------------------------------------------------------------

# colors
# Blue: #008fd5
# red: #fc4f30
# yellow: #e5ae37
# green: #6d904f