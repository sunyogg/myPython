
'''Python’s dictionaries, which allow you to
connect pieces of related information. You’ll learn how to access the information once it’s
in a dictionary and how to modify that information.
Because dictionaries can store an almost limitless
amount of information, I’ll show you how to loop through the data in a dictionary. 
Additionally, you’ll learn to nest dictionaries inside lists, lists inside dictionaries
, and even dictionaries inside other dictionaries.'''

#a simple dictionary
alien_0={'color':'green','point':'5','length':'9'}
print(alien_0['color'])
print(alien_0['point'])
print(alien_0['length'])


#accessing values in a dictionary
alien_0={'color':'green','point':'5'}
new_points=alien_0['point']
print(f"you just earned {new_points} points") #f strings ki kya zarurat jab hum 
print("you just earned",new_points,"points")#is method ko use kar sakte hai?


#adding new values to the dictionaries
alien_0={'color':'green','point':'5'}
print(alien_0)
alien_0['height']=7
alien_0['level']='hard'
print(alien_0)


#starting with an empty dictionary
#alien_0={}
#print(alien_0)
#alien_0['points']=5
#alien_0['name']='augustomus'
#print(alien_0)


#modifying values in a dictionary
#1)
alien_0={'color':'green'}
print('the color of alien is',alien_0['color'])
alien_0['color']='red'
print('the color of alien is now',alien_0['color'])
print(f"the color of alien is now {alien_0['color']}") #using f string

#2)
alien_0={'x_position':5,'y_position':25,'speed':'slow'}
alien_0['speed'] = 'fast'
print('original position',alien_0['x_position'])
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else: #this must be a fast alien
    x_increment = 3

#new position = old x_position + x_increment
new_position = alien_0['x_position'] + x_increment
print('new position',new_position)


#removing key value pair from the dictionary
alien_0 = {'name':'augustomus','color':'green','point':5}
print(alien_0)
del alien_0['point']
print(alien_0)


# a dictionary of similar object
#different way of writing dicitionary

fav_food={
    'arun':'chaat',
    'varun':'fulki',
    'tarun':'momos',
    'karun':'chaat'
    }

print(fav_food)
print("arun's favourite food is",fav_food['arun'])


#using get() to access values
alien_0={'color':'green','damage':5,'position':6.4,'points':10}
#print(alien_0['points'])
#point_value=alien_0.get('points','points value does not exist in dictionary')
#print(point_value)
print(alien_0.get('points','points value does not exist in the dictionary')) #better way to use get()


















