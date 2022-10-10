
# for program 1.0.1
def make_pizza(size,*toppings):
    print(f"You have ordered a pizza of {size} inches.")
    print('With the follwing toppings: ')
    for topping in toppings:
        print(f"-> {topping.title()}")

# for program 1.0.2

def user_info(fname,lname,**infos):
    infos['first'] = fname
    infos['last'] = lname
    for key,value in infos.items():
        print(f"{key} : {value}")