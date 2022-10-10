
# Properties of first class functions:
    # A function is an instance of the Object type.
    # You can store the function in a variable.
    # You can pass the function as a parameter to another function.
    # You can return the function from a function.
    # You can store them in data structures such as hash tables, lists, …

#-----------------------------------------------------------------------------------------

def add(num1, num2):
    print(num1 + num2)
f = add # Here the function is not executed. 
        # It takes the function object referenced by add and creates a second 
        # name i.e 'f' pointing to it.
f(2, 4) # Since we have used parenthesis here, this is where
        # the fucntion is executed.

#-----------------------------------------------------------------------------------------

# first class function.

def square(number):
    return number * number

# Here we have assigned a variable to a function.
f = square

# now we can treat the  variable f as function square
print(f(4))
print(square)
print(f)

#-----------------------------------------------------------------------------------------

# higher order function
# Using functions as parameter of another function.

def square(number):
    return number * number

def sqaure_of_square(number):
    return number * number


x = sqaure_of_square(square(2))
print(x) # 16


def square(number):
    return number * number

def cube(number):
    return number * number * number

def my_map(function, array):
    result = []
    for i in array:
        result.append(function(i))
    return result

num = [1, 2, 3, 4, 5]
x = my_map(cube, num) # since we are not trying to execute the function cube
                      # right in the my_map function call hence we will not  
                      # use the  parenthesis with cube.

print(x)

#-----------------------------------------------------------------------------------------

# When we call a function with parentheses, the function gets execute and 
# returns the result to the callable. In another case, when we call a function 
# without parentheses, a function "reference" is sent to the callable rather 
# than executing the function itself.

def logger(msg):
    
    def log_message():
        print('log:', msg )

    return log_message

log_hi = logger('hi')
log_hi()

#-----------------------------------------------------------------------------------------