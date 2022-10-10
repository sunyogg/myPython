def greetme():
    print("hello sanyog")


greetme()

def greetyou(name):
    print(f"hello {name}! how are you? ")

greetyou('rahyul')




def describe_pet(name = 'sumila',type = 'reptile'):

    print(f"Your {type} name is {name.title()}")

describe_pet('kaalu','dog')
describe_pet('cat','billonta')
describe_pet(type = 'fish', name = 'marina')

describe_pet('sonali')
describe_pet()




def get_formatted_name(fname, lname,mname = ''):
    
    if mname:
        print(f"Your full name is: {fname.title()} {mname.title()} {lname.title()}")
    
    else:
        print(f"Your full name is: {fname.title()} {lname.title()}")




get_formatted_name('sanyog','lodhi','patel')


def get_dictionary(username,age):
    dictionary = {'username':username,'age':age}
    dictionary['username'] = username
    dictionary['age'] = age
    return dictionary

user = get_dictionary('sanyog',28)
print(user)


data = {}
def get_userdata(username, age, salary = ''):
    data[username] = age
    data['salary'] = salary

print("Enter your name and age below:")
print("Enter 'q' to stop the program.")

while True:
    name = input("Enter your name: ")
    if name == 'q':
        break
    else:
        age = int(input("Enter your age: "))
    
    get_userdata(name,age)

    passs = input("'yes' and 'no' if you wann pass to another person:  ")
    if passs == 'yes':
        continue
    else:
        break

print(data)
'''
while True:
    try: 
        age = int(input("Enter your age: "))
    except ValueError:
        print("You can't age define using an alphabet. Please use integers.")
    else:
        print(f"You are {age} year(s) old.")
'''

# passing list in a function
def greet_users(names):
    for name in names:
        print(f"Hello {name.title()}! How are you?")

users = ['john','neil','mick','tom']
greet_users(users)


# transferring elements of one list to another without using function

names = ['sean','tom','jean','jakob','smith','penny']
usernames = []

# for loop is usefull when you want to copy elements from one list to another
for name in names:
    usernames.append(name)

print(names)
print(usernames)


# using while loop to transfer elements of one list to another
names = ['sean','tom','jean','jakob','smith','penny']
usernames = []


while names:
        poppedname = names.pop()
        usernames.append(poppedname)

print(names)
print(usernames)

def modify_list(names):
    names.pop()
    print(names)

listt = ['shawn','sean','jean','jackob']

# You can see how the effects of functions are permanent
modify_list(listt)
print(listt)





names = ['sean','tom','jean','jakob','smith','penny']
usernames = []


while names:
        poppedname = names.pop()
        usernames.append(poppedname)

print(names)
print(usernames)


def print_models(unprinted_designs, completed_models):
    x = unprinted_designs[:]
    while x:
        popped = x.pop()
        #print(f"Printing {popped.title()}")
        completed_models.append(popped)


    print("\nfollowing elements has been printed: ")
    for completed_model in completed_models:
        print(f"-> {completed_model}")

models = ['phonecase','robot','container','screw','nut','bolt']
completed_models = []


print_models(models,completed_models)




def tell_name(*toppings):
    for name in toppings:
        print(f"-> {name.title()}")


tell_name('ashish','ashu','max','tobby')


def make_pizza(size,*toppings):
    print(f"We are making your pizza of {size} inch size.")
    print("With the following toppings:")
    for topping in toppings:
        print(f"-> {topping}")


make_pizza(6,'pepperoni','cheese','chilly','tomatos')



def give_info(fname,lname,**more):
    print(fname,lname)
    more['first'] = fname #adding fname and lname to the dictionary more
    more['last'] = lname
    print(more)


give_info('sanyog','lodhi',location = 'Jabalpur',country = 'India')




#import functionclassesmodules
# from functionclassesmodules import make_pizza
# from functionclassesmodules import user_info, make_pizza
from functionmodules import user_info as ui , make_pizza as mp
# from functioclassesmodules import make_pizza as mp 

# program 1.0.1
mp(6,'pepperoni','chilly','cheese','sauce')

# program 1.0.2
ui('sunyog','lodhi',age = 20, location = 'jabalpur')