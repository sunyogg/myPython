
# This first approach to importing, in which you simply write import followed by the 
# name of the module, makes every function from the module available in your program. 
# If you use this kind of import statement to import an entire module named 
# module_name.py, each function in the module is available through the following syntax:
# ->  module_name.function_name()

import pizzaandinfo
# pizzaandinfo module ke saare functions import karr liye
pizzaandinfo.makepizza(14,'pepperoni','extra cheese','chilly','pepper')
pizzaandinfo.userinfo('sunyog','lodhi',age = 20 , location = 'jabalpur')

#-------------------------------------------------------------------------------------------
# You can also import a specific function from a module. Here's the general syntax 
# for this approach:
# -> from module_name import function_name

from pizzaandinfo import makepizza
# pizzaandinfo module se sirf makepizza function import kiya hai
makepizza(13,'paneer','masala','pepperoni')

#-------------------------------------------------------------------------------------------

# You can import as many functions as you want from a module by separating each 
# function's name with a comma:

from pizzaandinfo import makepizza, userinfo
# importing specific multiple functions from pizzandinfo module
makepizza(14,'pepperoni','cheese')
userinfo('sanyog','lodhi',age = 20 , location = 'jabalpur')

#-------------------------------------------------------------------------------------------
# Using as to Give a Function an Alias

# If the name of a function you're importing might conflict with an existing name in 
# your program or if the function name is long, you can use a short, unique alias—an 
# alternate name similar to a nickname for the func- tion. You’ll give the function 
# this special nickname when you import the function.

from pizzaandinfo import makepizza as mp

mp(14,'pepperoni','extra cheese','tomatos')

#-------------------------------------------------------------------------------------------
#Using as to Give a Module an Alias

# If the name of a function you’re importing might conflict with an existing name in 
# your program or if the function name is long, you can use a short, unique alias—an 
# alternate name similar to a nickname for the function. You’ll give the function 
# this special nickname when you import the function.

import pizzaandinfo as pi
pi.makepizza(15,'pepperoni','strawberries','extra cheese','spicy')

#-------------------------------------------------------------------------------------------

# Importing All Functions in a Module

# The asterisk in the import statement tells Python to copy every function from the 
# module pizza into this program file. Because every function is imported, you can 
# call each function by name without using the dot notation.

from pizzaandinfo import *

makepizza(14,'pepperoni','extra cheese')
userinfo('sanyog','lodhi',age = 20 , location = 'jabalpur')

#-------------------------------------------------------------------------------------------

