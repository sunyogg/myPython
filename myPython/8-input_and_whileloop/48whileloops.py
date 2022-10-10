
#while loops
number = int(input("Please enter a number which is less than 10 = "))
while (number) <= 5:# jab takk number 5 se kamm rahega 
    print((number)) # tabb tak ye block of code run hota rahega
    (number) += 1

#--------------------------------------------------------------------------------------------

#letting user decide when to quit the program using while loops
print("\n\tCalculator")

print("\n\ta-Addition\n\tb-Subtraciton\n\tc-Multiplication\n\td-Division")
z = str(input("\nEnter the operation you want to perform\nor type 'quit' if you wanna quit calculator = "))
while z != 'quit':
    x = float(input("Enter the first number = "))
    y = float(input("Enter the second number = "))
    if z == 'a':
        print("The sum of the two numbers is",x+y)
    if z == 'b':
        print("The subtraction of the two numbers is",x-y)
    if z == 'c':
        print("The multiplication of the two numbers is ",x*y)
    if z == 'd':
        print("The division of two numbers is",x/y)
if z == 'quit':
    print('The calculator is closed.')

#------------------------------------------------------------------------------------------

prompt = "Enter your name and I'll print a message for you. "
prompt += "You can type 'quit' if you don't wanna continue. Your name = "
name = ""
while name != 'quit':
    name = input(prompt)
    if name == 'quit':
        print('Program stopped')
    else:
        print("Hey",name,"I hope you are doing well.")

#--------------------------------------------------------------------------------------------
# Flags
# the program is same as above but here we are using flags
prompt = "Enter your name and I'll print a message for you. "
prompt += "You can type 'quit' if you don't wanna continue. Your name = "
name = ""
active = True
while active:
    name = input(prompt)
    if name == 'quit':
        active = False
        print('Program stopped')
    else:
        print("Hey",name,"I hope you are doing well.")

#------------------------------------------------------------------------------------------------------------

# using break to stop the loop (* I didn't really understood the use of break here)
# here we dont need to use the flag, to check whether the condition is true or not
# we can just use break to stop the loop whenever we want
prompt = "Enter the name of city you have visited "
prompt  += "You can always type 'quit' to quit the program. = "
while True:
    city = input(prompt)
    if city =='quit':
        
        print("The program has been stopped")
        break #the program will exit immediately without running any code after break.
            
    else:
        print("Oh! I would love to visit",city.title())

#------------------------------------------------------------------------------------------------------

#using continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue #the continue statement tells Python to ignore the rest of the loop
                 #and return to the beginning.
    print(current_number)


#---------------------------------------------------------------------------------------------------
#a program asking for the user to enter toppings they want in their pizza

#defining some important variables
prompt = "Please enter pizza toppings you want in your pizza below. "
prompt += "You can quit the program by typing 'quit'."
toppings_list = []
stops = ['stop','quit']


# using while loops
while True:
    toppings = input('Enter your toppings here = ')
    if toppings not in stops :
        print("Okay we'll add",toppings.title())
        toppings_list.append(toppings)
        continue

#if the user type stop then we'll print all the toppings they have requested
#and tell them that we're making their pizza.
    if toppings =='stop':
        print("Thanks! We are making pizza with your desired toppings.")
        print("Here is the list of the toppings you requested:")
        for topping_list in toppings_list:
            print('->',topping_list.title())
        break
        
#if the user decides to quit then it will end the program
#therefore their will be no toppings
    if toppings =='quit':
        print("Okay we'll quit the program")
        break
           

    
   
    


