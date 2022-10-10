# input
'''
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10
'''

# output
"""
206
"""

# explanation
"""
Picking 5 from the 1st list, 9 from the 2nd list and 10 from the 3rd list 
gives the maximum S value equal to (5**2 + 9**2 + 10**2)%1000 = 206 .
"""


# let's do it

# timeandmodulo = str(input())
# time = int(timeandmodulo.split()[0])
# modulo = int(timeandmodulo.split()[1])

# equation = []

# for i  in range(time):
#     lis = str(input())
#     lis1 = lis.split()
#     lis2 = [int(x) for x in lis1]
#     y = [i % modulo for i in lis2]
#     max_index = y.index(max(y))

#     # print(lis2)
#     # print(y)
#     # print(max_index)

#     maxx = lis2[max_index]
#     # print(maxx)
#     equation.append(maxx ** 2)

# # print(equation)
# print((sum(equation)) % modulo)

# -----------------------------------------------------------------------------------------





























# array : of n integers
# 2 disjoint sets A and B
# both the set contains m integers
# like all integers of A
# dislike all intergers of B
# for integers(i) in array
# if i belongs to A -> +1
# if i belongs to B -> -1
# whats the result(sum) of all those (+1) and (-1)

# 3 2 -> n m
# 1 5 3 -> array of n int
# 3 1 -> A of m int
# 5 7 -> B of m int

# n -> length of array
# m -> length of sets

tell = str(input())
tell = [int(x) for x in tell.split()]
n = tell[0]
m = tell[1]

arr = str(input())
arr = [int(x) for x in arr.split()]
aset = str(input())
aset = [int(x) for x in (aset.split())]
bset = str(input())
bset = [int(x) for x in (bset.split())]

# arr = [1, 2, 3, 4, 5, 6, 7, 8,]
# aset = [1, 2, 3, 4]
# bset = [7, 8]

result = 0
for i in arr:
    if i in aset:
        result += 1
    if i in bset:
        result -= 1

print(result)
