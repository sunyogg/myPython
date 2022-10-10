
from matplotlib import pyplot as plt

# x = [x for x in range(500)]
# y = [i**3 for i in x]


# fig, ax = plt.subplots()
# ax.plot(x, y)

# plt.show()

# ----------------------------------------------------------------------------------

input_vals = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# if x not passed then
# x = [0, 1, 2, 3, 4]

plt.style.use('seaborn')

fig, ax = plt.subplots()



ax.plot(input_vals, squares, marker='*', lw=1, label="Sqaure of Integers")


ax.set_title("Squares")
ax.set_xlabel("Integers")
ax.set_ylabel("Sqaures")

ax.legend()
#ax.grid(True)

# set the size of the tick labels
ax.tick_params(axis='x', which='major', labelsize=14)

plt.tight_layout()

# if you want to save the file
# plt.savefig('squareplot.png', bbox_inches='tight')
plt.show()

#print(plt.style.available)



