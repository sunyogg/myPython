
'''
LEGB
Local, Enclosing, Global, Built-in
Local: variables defined within a function.
Globals: variables defined at the top level of the module,
or defined outside of any function or explicitly declared global
using a global module.
Built-ins: are just named  that are preassigned in python. 

Python will first check if the variable is in local scope, if 
does not find it there then it will check in Enclosing scope and if 
it does not find it there it will check in Global scope and if it 
does not find it there it'll check in Built-in scope and if it 
still does not find it there it will throw an error saying variable 
not defined 
Local variable doen't live outside the function. So if there is any
variable defined inside a function and if you try print the value
of that variable outside the function it'll throw an error saying
variable not defined.

'''
# -----------------------------------------------------------------------------------------
'''
x = 'Global x'

def test():
    global x
    # this line tells python that we want to work with 
    # Global variable x 
    x = 'local x'
    print(x)

test()
print(x)

if there are two variables of same name, say we have defined x 
as a global variable and as well as a local variable then, both
the x's will have different value and they can't be overridden 
by one another unless we explicitly tell python to work with global
variable even inside a function.

'''

#----------------------------------------------------------------------------
'''
import builtins
#print(dir(builtins))

def min():
    pass

m =  min([1,2,3,4,5,6])
print(m) 
# Here when we tell python to print(m) and checks the scope of 
# variable m or min() then it checks that min is a function
# defined by user. Therefore when following the LEGB rule, python
# found the function in a Global scope before the builtin scope
# and threw an error saying: takes 0 positional arguments but 1 was 
# given, as we defined min as function without any parameter.

'''
# -----------------------------------------------------------------------------------------


x = 'global_x'

def outer(): # Enclosing function
    x = 'outer_x'
    def inner(): # Inner function
        # global x
        # nonlocal x
        x = 'inner_x'
        print(x)
    inner()
    print(x)

outer()
print(x)
''' 
python can only check scope outside of the local, ex- if doesn't
find anything in local it'll search in enclosing, and if nothing
in enclosing it'll search in global and if nothing in global 
it'll search in builtins, so it won't reverse it's order
like if we print a variable in enclosing function that python
will first search in enclosing then in global it won't inside
in the local scope.
'''

