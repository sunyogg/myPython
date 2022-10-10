'''
# * -> tuple
# ** -> dicitionary

# passing an arbitrary number of arguments
# stored in form of tuples
def toppings(*toppings):
    print("Here is the list of toppings you requested:")
    for topping in toppings:
        print(topping)

toppings('pepperoni')
toppings('paneer','cheese','pepperoni','strawberries','fries')

#---------------------------------------------------------------------------------------------

# mixing positional and arbitrary arguments
def makepizza(size,*toppings):
    print(f"\nmaking pizza of size {size} inches with following toppings:")
    for topping in toppings:
        print(f"- {topping}")

makepizza(16,'pepperoni')
makepizza(18,'pepper','chilly tomato','fries','extra cheese')
'''
#---------------------------------------------------------------------------------------------

# using arbitrary keyword elements
# stored in form of dictionary
def userinfo(fname,lname,**more):
    more['first'] = fname
    more['last'] = lname
    return more

a = userinfo('sanyog','lodhi',age = 28,location = 'jabalpur')
print(a)


#---------------------------------------------------------------------------------------------