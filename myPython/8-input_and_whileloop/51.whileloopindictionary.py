# filling dictionary with user input using a while loop

fooders = {}
flag = True
while flag:
    name = input("Enter your name: ")
    food = input("what is your favourite food: ")
    fooders[name] = food
    conti = input("you wanna continue? - yes/no: ")
    if conti == 'yes':
        continue
    if conti == 'no':
        break
for key,value in fooders.items():
    print('Results:')
    print(key+"'s favourite food is",value.title())

#---------------------------------------------------------------------------------------

# filling dictionary with user input using a while loop
responses = {}
yes_no = ['yes','no']
polling_active = True
while polling_active:
    name = input("Please enter your name: ")
    response = input("Enter the name of city that you want to travel: ")
    responses[name] = response
    conti = input("Do you wanna continue - yes/no: ")
    if conti == 'yes':
        continue
        #polling_active = True

    if conti =='no':
        break
        #polling_active = False

    if conti not in yes_no:
        print('wrong input!')
        break

print('Here are the results: ')
for key,value in responses.items():
    print(key.title(),'would like to visit',value.title())

#---------------------------------------------------------------------------------------






