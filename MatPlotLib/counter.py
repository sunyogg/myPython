from collections import Counter

langs = ['python', 'java', 'javascript', 'c', 'c++', 'c#', 'typescript','php','swift', 'go']
# import random

# num = []
# for i in range (101):
#     x = random.choice(langs)
#     num.append(x)

# y = (Counter(num))
# print(y)
# print(y.most_common(5))

c = Counter(['cat', 'dog', 'lion'])
print(c)

c.update(['dog', 'cat', 'fox', 'dog'])

for item in c.values():
    print(item)



# print(c)


# ----------------------------------------------------------------------------------------------------------------------