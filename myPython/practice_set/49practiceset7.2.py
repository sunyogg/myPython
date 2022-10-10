'''
#7.4
prompt = "Please enter pizza toppings you want in your pizza below. "
prompt += "You can quit the program by typing 'quit'."
active = True
pizza_toppings = ""
while active:
    pizza_toppings = str(input("Enter your desired pizza toppings here = "))

    if pizza_toppings == 'quit':
        active = False
        print("Program stopped as per your request.")
        break
    else:
        print("Okay! We'll add",pizza_toppings.title())

#------------------------------------------------------------------------------------------

#7.5
age = ()
print("\nYou can type anything more than 999 to stop the program.")
while age != 1000:
    age = int(input("Enter your age = "))
    if (age) <= 3:
        money = 'free'
    if 3 < (age) <= (12):
        money = 10
    if 12 < (age) < (18):
        money = (15)
    if 18 < (age) < 1000:
        money = (20)
    if age >= 1000:
        print("The program has been stopped")
        break
    print("your ticket will be",(money))

#----------------------------------------------------------------------------------------
#7.6

#printing the available list of toppings in a pizzaria
print("\n\t Sanjog's pizzaria")
print("Here is the list of available toppings:")
available_toppings = ['pepperoni','mushroom','extra cheese','sausage','onion',
'black olives','green pepper','fresh garlic','tomato','paneer']
for available_topping in available_toppings:
    print('-> ',available_topping.title())

#making some list and empty list, which we can use inside the while loop
stopper = ['quit','stop']
toppings = []
flag = True

#starting the while loop
while flag:
    topping = input("\nEnter the name of pizza toppings you want in your pizza = ")

#for a topping to be accepted, it has to be in the list of availabe_toppings and
#should not be in the list stopper
    if topping not in stopper:
        if topping in available_toppings:
            print("Alright! Adding",topping.title())
            toppings.append(topping)
        else:
            print("Sorry! we don't have",topping.title())
    
#This is how user will quit the program.
    if topping =='quit':
        flag = False
        print("The program has stopped as per you wish.")

#Once the users have decided their toppings, we'll print the list of toppings he chose
    if topping =='stop':
        flag = False
        print("\nMaking your pizza sir.")
        print("Here is the list of your requested toppings:")
        for toppingx in toppings:
            print('-> ',toppingx.title())
'''
#-------------------------------------------------------------------------------------       
number = 0
while number < 10:
    number += 1
    if number % 2 == 0 :
        continue
    else:
        print(number)








