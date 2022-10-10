import itertools


# ---------------------------------------------------
# counter

counter = itertools.count() # An Iterator.

# print(next(counter))
# for i in counter:
#     print(i)

# --------------------------------------------------

# # We can use counter as a count inside a function
# while True:
#     if (next(counter)) == 16:
#         break
#     print('hello')

# --------------------------------------------------

# data = [100, 200, 300, 400, 500]

# x = (zip((counter), data)) # an iterator (x)

# print(next(x))
# print(next(x))

# for i in x :
#     print(i)

# --------------------------------------------------

# data = [1, 2, 3, 4, 5]

# z = list(itertools.zip_longest((range(10)), data))

# print(i)

# # Ouput:
# '''
# (0, 1)
# (1, 2)
# (2, 3)
# (3, 4)
# (4, 5)
# (5, None)
# (6, None)
# (7, None)
# (8, None)
# (9, None)
# '''

# --------------------------------------------------


# s = itertools.cycle(('on', 'off'))

# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))


# --------------------------------------------------

# x = itertools.repeat(2, 3)

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# --------------------------------------------------

# def return_square(n):
#     return n ** 2

# # print(return_square(2))

# # map(funciton() ,iterables)
# # iterables are given as argumnet to the function
# x = map(return_square, range(10))

# print(list(x))

# --------------------------------------------------

# def powered(n, m):
#     return n ** m

# # print(powered(3, 3))

# x = map(powered, [5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5])

# print(list(x))

# --------------------------------------------------

# x = map(pow, range(10), itertools.repeat(2))

# print(list(x))

# --------------------------------------------------

# x = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)])


# print(list(x))

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# # permutation  : order does matters     : (a, b) and (b, a) are different
# # combination  : order does not matters : (a, b) and (b, a) are same

# letters =['a', 'b', 'c', 'd']
# numbers = [0, 1, 2, 3]
# names = ['corey', 'nicole']

# per_num = itertools.permutations(numbers, 4)
# comb_let = itertools.permutations(letters, 2)
# print(list(per_num))
# print(list(comb_let))
# print()
# per_num = itertools.combinations(numbers, 4)
# comb_let = itertools.combinations(letters, 2)
# print(list(per_num))
# print(list(comb_let))

# --------------------------------------------------

# letters =['a', 'b', 'c', 'd']
# numbers = [0, 1, 2, 3]
# names = ['corey', 'nicole']

# # permutations with repetitions
# prod_let = itertools.product(letters, repeat=2)
# prod_num = itertools.product(numbers, repeat=2)

# for i in prod_num:
#     print(i)

# # combinations with repetitions
# comb_num = itertools.combinations_with_replacement(numbers, 2)
# for i in comb_num:
#     print(i)

# -------------------------------------------------- 

# # chain

# letters =['a', 'b', 'c', 'd']
# numbers = [0, 1, 2, 3]
# names = ['Corey', 'Nicole']

# # looping through many iterables at the same time.
# comb = itertools.chain(letters, numbers, names)

# -------------------------------------------------- 

# # islice

# slic = itertools.islice(range(50), 5, 30, 2 )

# # for i in slic:
# #     print(i)


# with open('itertools/data.log', 'r') as f:
#     content = itertools.islice(f, 3) # remember this is an iterator
#     for i in content:
#         print(i, end='')

# -------------------------------------------------- 
# # filter function
# numbers = [0, 1, 2, 3]
# def lt_2(n):
#     if n < 2:
#         return  True
#     return False

# result = filter(lt_2, numbers)
# for i in result:
#     print(i) 

# -------------------------------------------------- 

# numbers = [0, 1, 2, 3]

# def lt_2(n):
#     if n < 2:
#         return  True
#     return False

# result = itertools.filterfalse(lt_2, numbers)


# for i  in result:
#     print(i)

# -------------------------------------------------- 

# # dropwhile

# numbers = [0, 1, 2, 3, 2, 1, 0]

# def lt_2(n):
#     if n < 2:
#         return  True
#     return False

# result = itertools.dropwhile(lt_2, numbers)

# for i  in result:
#     print(i)

# # dropwhile
# # [0, 1, 2, 3, 2, 1, 0]
# # 0 -> True
# # 1 -> True
# # 2 -> False # prints every elements after the first false 
# #              including the current element.

# -------------------------------------------------- 

# # take while
# numbers = [0, 1, 2, 3, 2, 1, 0]

# def lt_2(n):
#     if n < 2:
#         return  True
#     return False

# result = itertools.takewhile(lt_2, numbers)

# for i  in result: 
#     print(i)
 
# # [0, 1, 2, 3, 4, 5]
# # 0 -> True
# # 1 -> True
# # 3 -> False # will return every element that were true before
# #              first false

# -------------------------------------------------- 

# letters =['a', 'b', 'c', 'd']
# numbers = [0, 1, 2, 3]
# names = ['Corey', 'Nicole']


# selectors = [True, True, False, True]

# result = itertools.compress(letters, selectors)

# for item in result:
#     print(item)

# --------------------------------------------------
 
letters =['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
names = ['Corey', 'Nicole']

result = itertools.accumulate(numbers)

print(list(result))
# fabonacci series

# --------------------------------------------------

import operator

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = itertools.accumulate(numbers, operator.mul)

print(list(result))













