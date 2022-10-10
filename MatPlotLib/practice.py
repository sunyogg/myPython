# import numpy as np

# from matplotlib import pyplot as plt


# dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# x_indexes = np.arange(len(dev_x))
# # [0 1 2 3 4 5 6 7 8 9 10]
# # [-0.75, 0, 0.25, 0.50] [0.75, 1, 1.25, 1.50]
# # [-0.50, -0.75, 0, 0.25] [0.50, 0.75, 1, 1.25]
# # [-0.50, -0.75, 0, 0.25] [0.75, 1, 1.25, 1.50]
# # [-0.75, 0, 0.25, 0.50] [0.75, 1, 1.25, 1.50] 


# # [0 1 2 3 4 5 6 7 8 9 10]
# # [-0.75, 0, 0.25] [0.75, 1, 1.25]

# wid = 0.20 
# # width = 100 / ((no.of bar + 1 ) * 100

# dev_y = [37732, 41247, 45372, 48876, 50142, 53850, 57287, 63016, 65998, 67003, 69000]
# py_dev_y = [48876, 53850, 57287, 63016, 64234, 65998, 70003, 70000, 71496, 75370, 83640]
# js_dev_y = [43515, 46823, 49293, 53437, 54788, 56373, 62375, 66674, 68745, 68746, 74583]
# j_dev_y = [41232, 43233, 47231, 50123, 52123, 54241, 59234, 63234, 66233, 67532, 72123]


# plt.bar(x_indexes - wid, py_dev_y, width=wid, label='Python')
# plt.bar(x_indexes, js_dev_y, width=wid, label='Javascript')
# plt.bar(x_indexes + (wid), j_dev_y, width=wid, label='java' )
# plt.bar(x_indexes + (2*wid), dev_y, width=wid, label='All dev' )

# plt.grid(True)

# plt.legend()

# plt.xticks(ticks=x_indexes, labels=dev_x)

# plt.show()





list = [2, 4, 5, 3, 1]
list.sort()
print(list)