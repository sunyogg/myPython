
from matplotlib import pyplot as plt

plt.style.use('seaborn')
num =  [ x for x in range(1000)]
cub= [x**3 for x in num]

plt.scatter(num, cub, c=cub, cmap=plt.cm.Blues, s=2)
plt.show()


