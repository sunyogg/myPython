
def makepizza(size,*toppings):
    print(f"You ordered a pizza of size {size} inches with following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")


def userinfo(fname,lname,**moreinfo):
    moreinfo['first'] = fname
    moreinfo['last'] = lname
    print("Following information provided by the user:")
    for key,value in moreinfo.items():
        print(f"{key} : {value}")

