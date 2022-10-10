# This is called nesting. You can nest dictionar­ ies inside a list, a list of items 
# inside a dictionary, or even a dictionary inside another dictionary. Nesting is a 
# powerful feature.

# -> dictionary in a list

alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

#A more realistic example would involve more than three aliens with code that 
# automatically generates each alien. In the following example we use range() to 
# create a fleet of 30 aliens:

aliens = []
#creating 30 aliens
for alien_number in range(30): #range() returns a series of numbers, which just tells Python how many times we want the loop to repeat.
    new_alien = {'color':'green','points':5}
    aliens.append(new_alien)

#show how many aliens have been created
print(len(aliens))

#printing first 5 aliens in list aliens
for alien in aliens[:6]:
    print(alien)

#How might you work with a group of aliens like this? Imagine that one aspect of a 
# game has some aliens changing color and moving faster as the game progresses. When 
# it’s time to change colors, we can use a for loop and an if statement to change 
# the color of aliens.

#making 30 aliens
aliens = []
for i in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#changing group of aliens
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
        #up_alien = {'color':'yellow','points':10}
        #aliens.append(up_alien)
        
#printing first five aliens
for alien in aliens[:6]:
    print(alien)

#--------------------------------------------------------------------------------------------
# -> list in a dictionary

pizzas = {
    'crust':'thick',
    'toppings':['mushroom','extra cheese']
}

# summarizing the order
print("\nYou odered the pizza with",pizzas['crust'],"crust."
    "And with the following toppings:")
for pizza in pizzas['toppings']:
    print('->',pizza.title())


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'javascript'],
    }

for name,languages in favorite_languages.items():
    if len(languages) > 1:
        print('\n',name.title()+"'s favourite language(s) are:")
    #for language in favorite_languages[name]:
        for language in languages:
            print('\t->',language.title())
    else:
        print('\n',name.title()+"'s favourite language is:")
        for language in languages:
            print('\t->',language.title())

#--------------------------------------------------------------------------------------------

#-> dictionary in a dictionary
users = {'arunl':{'first':'arun','last':'lodhi','location':'bahoripar'},
        'suyogl':{'first':'suyog','last':'lodhi','location':'chowkital'},
        'sourabhl':{'first':'sourabh','last':'lodhi','location':'lakhnadon'}
    }
for name,details in users.items():
    print('Username: ',name)
    #for detail in details.values():
    print('\tFull name: ',details['first'].title(),details['last'].title())
    print('\tLocation: ',details['location'].title())

