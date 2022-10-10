import matplotlib.pyplot as plt
x=[1,2,5]
y=[2,4,1]
plt.plot(x,y)
plt.show()

# error because of strings
x=['1','2','5']
y=['2','4','1']
plt.plot(x,y)
plt.show()