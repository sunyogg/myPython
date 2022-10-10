# Piechart


# autopct='%1.1f&&'
# wedgeprops={'edgecolor':'black'}

# -------------------------------------------------------------------------------------------
'''
from matplotlib import pyplot as plt
share = [66, 23, 88, 44,  2]
names = ['pizza', 'icecream','burger', 'golgappa', 'meat']
my_explode = [0, 0, 0, 0.2, 0]
my_colors = ['red', 'blue', 'yellow', 'green', 'black']

plt.pie(share, labels=names, explode=my_explode, shadow=True)
plt.legend(title='Food')

plt.title('Piechart')

plt.show()
'''
# -------------------------------------------------------------------------------------------

from matplotlib import pyplot as plt

plt.xkcd()

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 
          18523, 18017, 7920, 7331, 7201, 5833]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 
          'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 
          'Assembly']
my_explode = [0, 0, 0, 0.2, 0]

plt.pie(slices[0:5], labels=labels[0:5], shadow=True, 
        wedgeprops={'edgecolor':'black'}, explode=my_explode, 
        autopct='%1.1f%%', startangle=45)

plt.title("Piechart of Programming language according to number of user.")

plt.tight_layout()

plt.show()

# -------------------------------------------------------------------------------------------