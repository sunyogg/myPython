
#range function can be used to print series of number
for numbers in range(0,10):
    print(numbers)


#we can also use range function to print list by wrapping list function on range function
numbers=list(range(0,11))
print(numbers)

#We can also use the range() function to tell Python to skip numbers in a given range.
for even in range(0,21,2):
    print(even)

#making a list of first 10 square numbers
squares=[]
for  value in range(0,11):
    square=value **2
    squares.append(square)
print(squares)


#more concise
squares=[]
for value in range(0,11):
    squares.append(value**2)
print(squares)

#Simple Statistics with a List of Numbers
numbers=[0,1,2,3,4,5,6,7,8,9,10]
print(min(numbers))
print(max(numbers))
print(sum(numbers))





