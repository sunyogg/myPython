# Decorating our functions allows us to easily add functionality to  our existing
# functions by adding that fucntionality inside of our wrapper

# decorator function.
def decorator_function(original_function):

    def wrapper_function():
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function()
        

    return wrapper_function

@decorator_function  
def display():
    print("display function ran.")

display = decorator_function(display)

#print('')
display()


# ---------------------------------------------------------------------------------------------------
'''
def decorator_function:
    pass

@decorator_function
def hello_function():
    pass
'is same as'
hello_function = decorator_function(hello_function)
'''
# ---------------------------------------------------------------------------------------------------

def decorator_function(original_function):

    def wrapper_function(*args, **kwargs):
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function  
def display():
    print("display function ran.")


@decorator_function
def display_info(name, age): 
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('john', 25)
display()

# ---------------------------------------------------------------------------------------------------
'''
# class decorators

class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function


    def __call__(self, *args, **kwargs):
        print("call method executed this before {}".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_class 
def display():
    print("display function ran.")


@decorator_class
def display_info(name, age): 
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('john', 25)
display()
'''
# ---------------------------------------------------------------------------------------------------

def decorator_function(original_function):

    def wrapper_function(*args, **kwargs):
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function  
def display():
    print("display function ran.")


@decorator_function
def display_info(name, age): 
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('john', 25)
display()

# ---------------------------------------------------------------------------------------------------

# Decorator are used to modify the functionality of a function without changing
# it's main code. So if we have a function that perform a certain task, and
# we also want that function to perform some other task, then we can use
# decorator, imagine if we want to change the functionality of many function
# imagine the amount of time it would take to change the code of all those
# distinct function, we only need to change the code of the wrapper function
# inside the decorator function in order to add the functionality of original
# function.