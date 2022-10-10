#7.8
'''
sandwich_orders = ['chicken sandwich','veg sandwich','egg sandwich','nutella sandwich']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made",current_sandwich.title(),'for you.')
    finished_sandwiches.append(current_sandwich)
print("\nList of all the sandwiches that were made: ")
for finished_sandwich in finished_sandwiches:
    print('\t*',finished_sandwich.title())

#----------------------------------------------------------------------------------------

#7.9
sandwich_orders = ['pastrami','chicken','veg','pastrami','egg','nutella','pastrami',]
print(sandwich_orders)
print("Sorry guys we ran out of pastramin sandwich.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print('Here is the list of updated list:')
for sandwich_order in sandwich_orders:
    print('->',sandwich_order)

print(sandwich_orders)

#---------------------------------------------------------------------------------------------

#7.10
opinions = {}
stopper = ['yes','no']
flag = True
while flag:
    name = input("\nEnter your name: ")
    place = input("Write the name of the place where you'll want to spend your vacations: ")
    opinions[name] = place
    conti = input("You wanna continue - yes/no: ")
    if conti =='yes':
        continue
    if conti =='no':
        break
    if conti not in stopper:
        print('wrong input')
        break
print("\nHere are the the result of the survey: ")
for key,value in opinions.items():
    print(key.title(),'wish to go to',value.title(),'for vacation.')

#--------------------------------------------------------------------------------------------------------
'''
