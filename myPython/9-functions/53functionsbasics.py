
# defining a simple function
def greet_user():
    print('hello, how are you?')

greet_user()

#-------------------------------------------------------------------------------------------

# a function that will pass greeting message to the name, which is passed inside the
#paranethesis
def greet(username):#parameter
    print('hello',username.title(),'how are you doing?')

name = input("Please enter your username: ")
greet(name)#argument
# word parameter and argument can be used in place of each other

#-------------------------------------------------------------------------------------------

# a function that will add 2 values which are going to be passed inside the parenthesis
# of the function.
def summ(x,y):
	print(x+y)
a = int(input("Enter a number: "))
b = int(input("Enter second number: "))
summ(a,b)

#-------------------------------------------------------------------------------------------

# Difference between None and print() inside a fucntion

def formatted_name(first,last):
    formatted_name = f"{first} {last}"
    return formatted_name.title()
    # value of this function is formatted_name.title() 

print(formatted_name('sunyog','lodhi'))



def formatted_name(first,last):
    formatted_names = f"{first} {last}"
    print(formatted_names.title())
    # value of this function is None.

print(formatted_name('sunyog','lodhi'))

#You are printing the return values of your functions. Your functions all return 
# None (the default return value when you don't use an explicit return statement).


#You are printing the value returned by functions that have no explicit return 
# statement. The value returned from such a function is None by default. You are 
# printing this value. Try using a return statement sometimes instead of always 
# printing, e.g. return 'Goodbye!'.
#-------------------------------------------------------------------------------------------