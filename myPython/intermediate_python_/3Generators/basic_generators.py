

'''
def square_number(list):
    """This function will print the list of square of the given number."""
    result = []
    for number in list:
        square = number * number 
        result.append(square)
    return result
num = [1,2,3,4,5,6,7,8,9]
print(square_number(num))
'''


# Generator
# They help in conserving memory of the system since they aren't even doint
# anything and just waiting for the user to print the list or whatever.

def square_number(listt):
    """This function will print the list of square of the given number."""      
    for number in listt:
        yield (number * number)


my_num = square_number([1,2,3,4,5])
'''
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
print(next(my_num))
'''


listt = (x*x for x in range(1 ,6))
print(next(listt))
print(list(listt))
# if I put parenthesis here it will become generator.
print(listt)