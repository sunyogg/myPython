
#----------------------------------------------------------------------------------------

#looping through all the key-value pair in  dictionary
user = {
    'u_name':'sanjog',
    'name':'sunyog',
    'l_name':'lodhi'
    }
#if you want to print all the key and values in the dictionary
#print('here you go:',user.items()), check the output to understand
for key,value in user.items(): 
    print('\nkey:',key)
    print('value:',value)

# what will happen if we only assign one variable
#itll print a tuple of key and value, since we only used one variable
for value in user.items():
    print(value)

#what will happen if we type value before key -> it'll take value as key
#so in other words, first variable is always key
#and the second variable is always value, irrespective of what you name them
for value,key in user.items():
    print(value)

#favourite food
#accessing and using elements in a statement
fav_food = {
    'arun':'momos',
    'amit':'chaat',
    'asha':'dosa',
    'bhavna':'fulki'     
    }

for name,favorite_food in fav_food.items():
    print("\n",name+"'s favorite food is:",favorite_food)

#--------------------------------------------------------------------------------------------

#looping through all the keys in a dictionary
fav_food = {
    'arun':'momos',
    'amit':'chaat',
    'asha':'dosa',
    'bhavna':'fulki'     
    }
for name in fav_food.keys():
    print('\n',name.title())
if 'erin' not in fav_food:
    print('hey erin please tell us your favourite food')

#if you only want to print only the keys in the dictionary, you can use simple loop
#for name in fav_food:
   # print(name)
#even though all the keys will be printed using this method, it not a very accurate 
#professional way to this, 


# We’ll loop through the names in the diction­ ary as we did previously, but when the 
# name matches one of our friends, we’ll display a message about their favorite 
# language
fav_food = {
    'arun':'momos',
    'amit':'chaat',
    'asha':'dosa',
    'bhavna':'fulki'
    }
friends = ['arun','amit']
for name in fav_food.keys():

    if name in friends:
        food = fav_food[name]
        print(name.title(),"I see you love",food,"even i love them.")
    else:
        print(name)

#--------------------------------------------------------------------------------------------------

#looping through the dictionary's key in a particular order
#using the sorted fucntion to sort dictionary

fav_food = {
    'arun':'momos',
    'amit':'chaat',
    'asha':'dosa',
    'bhavna':'fulki',
    'sourabh':'chicken',
    'praoon':'noodles',
    'suyog':'manchurian'     
    }
for key in sorted(fav_food.keys()):
    print("Hey!",key,"thank you for telling me your favourite.")

print("These are food choosen by the people:")
for value in sorted(fav_food.values()):
    print('\t',value)

#------------------------------------------------------------------------------------------------
#looping through all the values in dictionary
fav_food = {
    'arun':'momos',
    'amit':'chaat',
    'asha':'dosa',
    'bhavna':'fulki',
    'pratik':'noodles',
    'sourabh':'chicken',
    'praoon':'noodles',
    'suyog':'manchurian',
    'sunyog':'chaat'     
    }
#print(fav_food.values())#see how it prints the list of the values in the dicitonary
for name in fav_food.values(): 
    print('->'+name)
print('')
for name in set(fav_food.values()):
    print('->'+name)
#we have used set() method here it which is a collection of only unique values
print(len(fav_food.values()))
print(len(set(fav_food.values())))

#----------------------------------------------------------------------------------------------------
