#let talk about set
list = ['chaat','fulki','pizza','boorgir','machurian','chaat','pizza','dosa']
print(list)
print(set(list))

print(len(list))
print(len(set(list)))

# or we can wrap set() around the original list
list1 = set(['chaat','fulki','pizza','boorgir','machurian','chaat','pizza','dosa'])
print(list1)

#You can build a set directly using braces and separating the elements with commas:

languages = {'python','c','c++','java','javascript','python','javascript'}
print(languages)