#The criteria that must be met to create closure in Python are summarized in 
# the following points:
    # We must have a nested function (function inside a function).
    # The nested function must refer to a value defined in the enclosing function.
    # The enclosing function must return the nested function.


# A closure is a function is an inner function that remembers and has access 
# to variables in the local scope in which it was created even after the 
# outer function has finished executing.
# A closure closes over the free variable from their environment.

# A Closure is a function object that remembers values in enclosing scopes 
# even if they are not present in memory. 

def outer_function():
    msg = 'hi'
    
    def inner_function():
        print(msg)

    return inner_function # notice no parenthesis here.

my_func = outer_function()
print(my_func)
print(my_func.__name__)
my_func()
my_func()
my_func()
my_func()

# ---------------------------------------------------------------------------------------

def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function


hi_func = outer_function('Hi')
hello_func = outer_function('Hello')

del outer_function # the returned function still works even when the original 
                   # function was deleted.

 
hi_func()

hello_func( )

#print(dir(outer_function('hi'))) # notice how it contains closure object.
#print(dir(hello_func))

# ---------------------------------------------------------------------------------------
# Free variable
# Here variable a is defined in the scope of outer() function. If we look at 
# inner() function, a is not defined there. But, function inner() is using 
# variable a and hence variable a in inner() function is Free Variable.
# The technique by which free variables get attached to the function in Python 
# is known as Closures. Python accomplish this task by creating an intermediary 
# object called Cell.