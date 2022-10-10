#7.6

#printing the available list of toppings in a pizzaria
print("Here is the list of available toppings:")
available_toppings = ['pepperoni','mushroom','extra cheese','sausage','onion','black olives','green pepper','fresh garlic','tomato','panner']
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
            print("Alright! Adding",topping)
            toppings.append(topping)
        else:
            print("Sorry! we don't have",topping)
    
#This is how user will quit the program.
    if topping =='quit':
        flag = False
        print("The program has stopped as per you wish.")

#Once the users have decided their toppings, we'll print the list of toppings he chose
    if topping =='stop':
        print("\nMaking your pizza sir.")
        print("\nHere is the list of your requested toppings:")
        for toppingx in toppings:
            print('-> ',toppingx.title())

#-----------------------------------------------------------------------------------------------------






