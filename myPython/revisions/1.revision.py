#variables

age=9
print('my age is',age)

name='sunyog'
print("my name is",name)

name='suyog'
print("my name is",name)

#strings

name= "suyog"
print(name.title())
print(name.title())
print(name.upper())

#combining and concatenating strings
intro='my name is'
name= 'sunyog'
print(intro+" "+name)
print('hello',intro+" "+name,'how you doing?')
print(intro,name)

age=20
print('sunyog is'+' '+ str(age) +' '+'years old.')
print("sunyog is", age, "years old.")

#tabs or new lines
print('\n\thow are you')

#stripping
name=' sunyog '
print(name+'hello')
print(name.lstrip()+'hello')
print(name.rstrip()+'hello')
print(name.strip()+'hello')

#practice set
name='suyog'
print("hello",name.title(),"how are you doin?")
print(name.upper())
print(name.lower())
print(name.title())

body='Albert Einstein once said'
quote='"people are weird."'
print(body+" "+ quote)

man='Albert Einstein'
quote='"people are weird."'
print(man,'once said',quote)

#numbers
print(4+4)
print(8-4)
print(2*2)
print(8/2)
print(2**2)

#comments
#hello how you doing
# import this

# Lists
vehicles= ['honda','suzuki','yamaha','audi','bmw']
print('my first bike was of',vehicles[2],'brand.')
print(vehicles[0])
print(vehicles[2])
print(vehicles[-1])
for vehicle in vehicles:
    if vehicle == 'bmw':
        print(vehicle.upper())
    else:
        print(vehicle.title())

vehicles= ['honda','suzuki','yamaha','audi','bmw']
vehicles[-2]='bugati'
print(vehicles)

#append
vehicles.append('ferrari')
print(vehicles)

#insert
vehicles= ['honda','suzuki','yamaha','audi','bmw']
print(vehicles)
vehicles.insert(0,'volkswagen')
print(vehicles)

#delete
vehicles= ['honda','suzuki','yamaha','audi','bmw']
print(vehicles)
del vehicles[0]
print(vehicles)

#pop
vehicles= ['honda','suzuki','yamaha','audi','bmw']
print(vehicles)
popped_vehicles = vehicles.pop()
print(vehicles)
print(popped_vehicles)

vehicles= ['honda','suzuki','yamaha','audi','bmw']
print("The last vehicle on the list is",vehicles.pop())
#using pop to remove any item from the list
print(vehicles.pop(3),'is the only vehicles on the list that starts with a letter A')


#removing a item by value
vehicles= ['honda','suzuki','yamaha','audi','bmw']
print(vehicles)
rem_vehicle = 'audi'
vehicles.remove(rem_vehicle)
print(rem_vehicle,'is too expensive for me')
print(vehicles)

#practice set
guest = ['aman','raman','pawan','suman','chaman','karam']
#removing and inserting another person in the list
popped = guest.pop(0)
guest.insert(0,'bhasam')
print(popped,'wont be able to come to the party ')
print('\nTherefore is the updated list of guests:\n',guest,'\n')
#adding more people to the list
print('oh wow I just found a bigger table so more people can come to my birthday party')
print('Okay so here is the updated list of more people who can come to my party')
guest.append('rajeev')
guest.append('aditya')
guest.append('shankar')
#printing the updated guest list
print(guest)
# updating the list again
print('\n I am really sorry to inform you that the bigger table wont be able to arrive at time')
print('therefore i cant invite everyone of you, here is the updated list:')
rejected_guest = []
x = guest.pop(-2)
y = guest.pop(2)
z = guest.pop(-3)
rejected_guest.append(x)
rejected_guest.append(y)
rejected_guest.append(z)
print(guest)

for peoples in rejected_guest:
    print('hii',peoples,'i am really sorry but i wont be able to invite you to my party')
for people in guest:
    print('hii',people,'you are whole heartedly invited to my birthday party')


#sorting a list
vehicles = ['honda','suzuki','yamaha','audi','bmw']
print(vehicles)
vehicles.sort()
print(vehicles)
vehicles.sort(reverse = True)
print(vehicles)
print(sorted(vehicles))
vehicles.reverse()
print(vehicles)

#finding length of a list
vehicles = ['honda','suzuki','yamaha','audi','bmw']
print(len(vehicles))


places = ['california','paris','bali','himalayas','kathmandu','afghanistan','newyork','uk','australlia']
#printing original list
print(places)

#printing the sorted list using sorted()
print(sorted(places))

#printing again to see that list is in its original form
print(places)

#printing the list in reverse order using the sorted function
print(sorted(places,reverse = True))

#printing the list again to check if the list is in its original order
print(places)

# reverse sorting the list permanently 
places.reverse()
print(places)

#reverse sorting it again to bring it back to original form.
places.reverse()
print(places)

#sorting the list using the sort() funtion
places.sort()
print(places)

#reverse sorting the list using the sort() funtion
places.sort(reverse = True)
print(places)

#looping a list
magicians = ['alice','tom','jerry','oggy','sam','dave']
for magician in magicians:
    print("hello!",magician,'i liked your magic')
print('everyone! thanks for coming')

magicians = ['alice','tom','jerry','oggy','sam','dave']
for magician in magicians:
    print('Hello',magician.title(),'thanks for coming mate.')
print('would love to see you all again.')

pizzas = ['peperoni','cheesy','plain']
for pizza in pizzas:
    print('i like',pizza.title(),'pizza a lot.')
print('even though i dont eat pizza that often') 

#using range funtion
for value in range(0,5):
    print(value)


#Using range() to Make a List of Numbers
numbers = list(range(0,21,1))
print(numbers)

#using range to print a list of first 10 squares
squares = []
for square in range(0,11):
    x = (square**2)
    squares.append(x)  
print(squares)


 # list comprehension   
cubes = [value**3 for value in range(0,21)]
print(cubes)

#practice on list and loops
x = (list(range(0,21)))
print(x)
print(max(x))
print(min(x))
print(sum(x))

squares = []
for value in range(0,31):
    square = value**3
    squares.append(square)
print(squares)

x = [value**3 for value in range(0,31)]
print(x)
#print(list(range(0,-31,-3)))


#slicing a list
places = ['california','paris','bali','himalayas','newyork','uk','australlia']
for place in places[0:3]: #looping through a slice of list
    print(place.title())

print(places[0:3])
print(places[:2])
print(places[1:])
print(places[:])
print(places)

#copying a list using slice
fav_places = ['california','paris','bali','himalayas']
friend_place = fav_places[:2]
print("My favourite places are",fav_places)
print("\n My friends favourite place are",friend_place)

#to prove that both the list are different
fav_places.append('lisbon')
friend_place.append('martina')
print(fav_places)
print(friend_place)

places = ['california','paris','bali','himalayas']
print("The first 2 items of the list are: ")
for place in places[0:2]:
    print(place.title())

#tuples = unchangeable\immutable list is called tuples
numbers = (0,1,2,3,4,5,6,7,8,9)
for number in numbers:
   print(number)
#numbers[0] = 96

#this is the only way to modify tuple
numbers = (11,33,55,77,88)
print(numbers)


# IF STATEMENTS
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'Audi'
print(car.lower() == 'audi') #it is case sensitive.
age = 20
print(age>19)
print(age<9)
print(18<age<21)

#this example is important, since the code stops running further if any condition is found to be true. but we need the code to be complety excuted
#solution at line 374
x = int(input("Enter your age = "))
if 70 > x >= 18:
    print("You can access our site! Please enter your username below:")
    y = str(input("->"))
    print("Welcome!",y)
if x <= 70:
    print("Sorry! You are too old to enter our site.")
else:
    print("Sorry! You are not eligible to enter our site.")

# in and not in
users = ['sunyog','suyog','prasoon','pratik','amit','bhavna','arun','asha']
x = str(input('Enter your username = '))
if x.lower() in users:
    print('You are our existing customer. Please enter your password below:')
if x.lower() not in users:
    print('Looks like you are new here. Enter your username and password')



x = int(input('enter number :'))
if x is 10:
    print("true")
else:
    print("false")
    

# and conditional test
x = int(input("Enter your brother's age = "))
y = int(input('Enter yours age = '))
if x>=18 and y>=12:
    print("you can enter park")

else:
    print("no entry")

#or conditional test
x = int(input("Enter your brother's age = "))
y = int(input('Enter yours age = '))
if x>=18 or y>=12:
    print("you can enter the mall")

else:
    print("sorry no entry")


numbers = list(range(0,1001,3))
y = int(input("Enter a number = "))
if y in numbers:
    print("Please choose another number.")
if y not in numbers:
    print("You can proceed further.")
    

print("Thanks for taking admission!")
age = int(input("Enter your age = "))
if age < 4:
    print("There will be no admission fee.")
elif 4 <= age < 18:
    print("There will be an admission charege of 5$.")
else:
    print("There will be an admission charge of 10$.")


#use simple if statements so that the compilor will go through all the conditions even if it finds a true condition in first line
requested_cakes = ['chocolate','strawberry','vanilla']

if 'chocolate' in requested_cakes:
    print('Adding chocolate to your cake...')
if 'strawberry' in requested_cakes:
    print('Adding strawberries in your cake...')
if 'vanilla' in requested_cakes:
    print('Adding vanilla to your cake...')
print('Your cake is ready')

for requested_cake in requested_cakes:
    print('Adding',requested_cake + '...')
print('Your cake is ready.')

friends = []
if friends:
    for friend in friends:
        print(friend)
else:
    print('You have no friends?')
    

#checking whether a list is empty or not
l1 = ["Hire", "the", "top", "1%", "freelancers"]

l2 = []

if l2:
    print("list l2 is not empty")
else:
    print("list l2 is empty")

if l1:
    print("list l1 is not empty")
else:
    print("list l1 is empty")


available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms','pepperoni','extra cheese','red chilly']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding",requested_topping)
    else:
        print('Sorry! We dont have',requested_topping)
    
print("Your pizza is ready.")

#some practice questions

users = ['aman','amit','shlok','ansh','anshul','amitabh','anshu',]
new_users = ['raman','pawan','chaman','suman','amit','Ansh']
for new_user in new_users:
    if new_user.lower() in users:
        print("The username",new_user,"is taken. Please choose another one.")
    else:
        print('Welcome',new_user)


users = ['aman','amit','shlok','ansh','anshul','amitabh','admin']
for user in users:
    if user == 'admin':
        print("Hello admin! You wanna see the statistics of the site.")
    else:
        print("hello!",user,"Welcome.")

numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print(str(number)+"st")
    elif number == 2:
        print(str(number)+'nd')
    elif number == 3:
        print(str(number)+'rd')
    else:
        print(str(number)+'th')


dictionaries = {'sun':20,'suy':21,'pra':24,'prat':28}
print(dictionaries)
#accessing elements of list
#print(dictionaries['sun'])
#print(dictionaries['suy'])
#print(dictionaries['prat'])
#print(dictionaries[24])
print("congrats prasoon now you are",dictionaries['pra'],"years old.")

#adding elements in dictionaries
dictionaries['sou'] = 22
dictionaries[69] = 96
dictionaries[28] = 'coincidence'
print(dictionaries)

#updating elements of list
dictionaries['pra'] = 25
#print(dictionaries)

#using an empty list
empty = {}
empty['gold'] = 20
empty['silver'] = 15
empty['diamong'] = 30
print(empty)


alien = {'x_position':5, 'y_position':25, 'speed':'slow'}
print('original position',alien['x_position'])
alien['speed'] = 'medium'
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else: #it must be a fast alien
    x_increment = 3


new_position = alien['x_position'] + x_increment
print('New Position:',new_position)

#removing key value pair
dictionaries = {'sun':20,'suy':21,'pra':24,'prat':28,'sou':22}
del dictionaries['sun']
print(dictionaries) 

#dicitionary of similar objects or an organized dictionary
dictionary = {
    'diamond': 40,
    'gold': 30,
    'silver': 20,
    'bronze': 10,
    'iron': 5,
}
print(dictionary)

# using get() to access values
#it is really helpful when you dont know if the value that you want to access 
#exist on the dictionary or not.
metals = {'diamond': 40, 'gold': 30, 'silver': 20, 'bronze': 10, 'iron': 5}
#print(metals['titanium'])
#print(metals.get('titanium','does not exist'))
for metal in metals:
    print(metal)

