
#checking for special item on list
req_flavors=['chocolate','vanilla','strawberry','elaichi']
for req_flavor in req_flavors:
    if req_flavor=='vanilla':
        print('sorry we are out on vanilla')
    else:
        print('adding',req_flavor)


#dealing with empty list
req_flavors=[]
if req_flavors:
    for req_flavor in req_flavors:
        print('adding',req_flavor,'flavor')
    print('your icecream is ready.')
else:
    print('do you only want a cone?')


#Using Multiple Lists
#making sure that the input is valid
#Let’s watch out for unusual topping requests before we build a pizza.
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
req_toppings=['mushrooms','green peppers','extra cheese','paneer']
for req_topping in req_toppings:
    if req_topping in available_toppings:
        print('adding',req_topping)
    else:
        print('sorry we do not have',req_topping)
print('your pizza is ready')
    







