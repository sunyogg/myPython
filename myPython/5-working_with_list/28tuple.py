#using tuple

'''numbers=(2,4,6,7,8,9,0)
#numbers[1]=5 ,notice how i am not able to assign a new value to index 1
#because tuples are immutable
print(numbers)
print(numbers[0])

#looping through all value in tuple, its same as in lists
for number in numbers:
    print(number)'''

#writing over a tuple
#Although you can’t modify a tuple, you can assign a new value to a variable that holds
#a tuple. So if we wanted to change our dimensions, we could redefine the entire tuple:
numbers=(2,4,6,8)
print("\noriginal numbers:")
for number in numbers:
    print(number)
numbers=(1,3,5,7)
print("\n modified numbers:")
for number in numbers:
    print(number)
    
