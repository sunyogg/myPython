
# * -> tuple
# ** -> dicitionary

# 8.12
def makesandwich(*items):
    print('Here is the list of items that you want in your sandwich:')
    for item in items:
        print(f"- {item}")


makesandwich('tomatos')
makesandwich('paneer','butter',)
makesandwich('pepperoni','fries','chilly','sauce')

#----------------------------------------------------------------------------------------

#8.13
def buildprofile(fname,lname,**moreinfo):
    moreinfo['first'] = fname
    moreinfo['last'] = lname
    for key,value in moreinfo.items():
        print(f"- {key} : {value}")

buildprofile('sanyog','lodhi',age = 20, location = 'jabalpur', country = 'india')

#----------------------------------------------------------------------------------------

#8.14
def buildcar(manufacture,modeln,**moreinfo):
    moreinfo['manufacturer'] = manufacture
    moreinfo['model name'] = modeln
    print("\n",moreinfo)
    print("\nCar info:")
    for key,value in moreinfo.items():
        print(f"{str(key).title()} : {str(value).title()}")

buildcar('audi','r8', color = 'black', year = 2018, type = 'sudan')

#---------------------------------------------------------------------------------------------






