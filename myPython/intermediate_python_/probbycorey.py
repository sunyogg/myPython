


# class Sentence:

#     def __init__(self, sentence):
#         self.sentence = sentence
#         self.index = 0
#         self.words = self.sentence.split()

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index >= len(self.words):
#             raise StopIteration

#         index = self.index 
#         self.index += 1
#         return self.words[index]


# s = Sentence('This is a test')

# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))



def sentence(string):
    words = string.split()
    # words = ['This', 'is', 'a' 'test']
    for word in words:
        yield  word

    print('restarting')

# Yes, return stops execution and exits the function. return always** exits 
# its function immediately, with no further execution if it's inside a for 
# loop.

z = sentence("This is a test")
print(next(z))
print(next(z))
print(next(z))
print(next(z))




# for i in z:
#     print(i)






# print(z)
# print(next(z))
# print(next(z))
# print(next(z))