
# working of len() method 

def lens(string):
    count = 0
    for i in string:
        count += 1
    return (count)

print(lens('hello world'))

# ---------------------------------------------------------------------------------


def hello_func():
    return ("hello world")

# return -> returns/ gives function value to the caller.
# print inside function -> simply prints anything, and it's not the value 
# of a function.
# an executed function is equal to the RETURN value

# hello_func() = "hello world" = value of function

print(hello_func().lower())

# ---------------------------------------------------------------------------------

# args -> return tuple
# kwargs -> return dictionary

def student(*args, **kwargs):
    print(args)
    print(kwargs)

arg = 'python', 'java', 'javascript', 'c++'
kwarg = {'name':'sunyog', 'field':'cse'}

#student('python', 'java', 'javascript', 'c++', name='sunyog', field='cse')
#student(arg, kwarg)
student(*arg, **kwarg)

# ---------------------------------------------------------------------------------




