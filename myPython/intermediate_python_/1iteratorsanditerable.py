
num = [1, 2, 3]

print(dir(num))
print()

# loop over the iterable object 
# loop will call __iter__ on that object
# __iter__ will return an iterator that we can loop over

# if something is iterable it needs to have a special method __iter__ .
stg = 1
print(dir(stg))
# when i used the dir(stg) method it did not contain __iter__ method, which
# meant it cannot be iterated.
# so we can say something can be looped over if it has that method __iter__
# for i in stg:
#     print(i)
# and when i tried to iterate or when i tried to loop through stg in threw 
# an error saying object is not iterable.

# so what for loop is really doing is, it is calling the __iter__ method 
# and returning an iterator that can be looped over. that is why if the 
# object does not have __iter__ method therefore the loop cannot call the
# __iter__ method and hence we can loop that object.
# any object that contains that __iter__ method is iterable

# an iterator is an object with a state so that it remembers where it is during
# iteration.
'''
# ------------------------------------------------------------------------------------------
# an iterator is an object with a state so that it remembers where it is during
# iteration and iterator also know how to get to next value they do it using
# dunder next method.
# there are simple method that calls these dunder methods.
# instead of using 'nums.__iter__()' you can use 'iter(nums)'

nums = [1, 2, 3, 4, 5, 6]

# print(next(nums))

i_nums = iter(nums)
print(dir(i_nums)) 
print( i_nums)




# print(dir(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))
# an iterator is an object with a state so that it remembers where it is during
# iteration and iterator also know how to get to next value they do it using
# dunder next method.
# You see how an iterator remembers where it left off and when we pass next 
# again it takes us to next value which means it remembers where it left off.

print(next(i_nums))
# it'll throw an StopIteration method if the iterator is exhausted in other 
# words when it has no values inside it.

# ------------------------------------------------------------------------------------------------

# we can also understand the working of a for loop using like how does it 
# work in background


nums = [1, 2, 3, 4, 5, 6]

# working of a for loop
i_nums = iter(nums)
while True:
    try:
        item = next(i_nums)
    except StopIteration:
        break
    else:
        print(item)


# ------------------------------------------------------------------------------------------------

# let's create our own range function.

class MyRange:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end: 
            raise StopIteration
        current = self.start
        self.start += 1
        return current


ran = MyRange(1,9)

print(ran.__next__())
print(ran.__next__())

print(next(ran))
print(next(ran))
print(next(ran))
print(next(ran))
print(next(ran))
print(next(ran))
print(next(ran))
print(next(ran))
'''
# ------------------------------------------------------------------------------------------------

# # creating a generator function of above class.

# def my_range(start, end):
#     while start < end:
#         yield start
#         start += 1

# ran = my_range(1,4)
# print(ran)

# print(next(ran))
# print(next(ran))

# ------------------------------------------------------------------------------------------------

# so basically can i say that iterators are the objects that have both __iter__
# as well as __next__ method, whereas objects that are iterable only have
# __iter__ . So iterators are the object that can be looped and they also have
# a state so that it remembers where it is during iteration. Whereas objects
# that are iterable don't have that state, they can only be looped. 

# ------------------------------------------------------------------------------------------------