#5.3v
alien_color='green'
if alien_color=='green':
    print('you earned 5 points')
#2)
alien_color='yellow'
if alien_color=='green':
    print('you earned 5 points')


#5.4
alien_color='green'
if alien_color=='green':
    print('you got 5 points')
else:
    print('you got 10 points')

#2)
alien_color="yellow"
if alien_color=="green":
    print('you got 5 points')
else:
    print('you got 10 points')

#5.5
alien_color='green'
if alien_color=='green':
    print('you got 5 points')
elif alien_color=='yellow':
    print('you got 10 points')
elif alien_color=='red':
    print("you got 15 points")


alien_color='yellow'
if alien_color =='green':
    print('you got 5 points')
elif alien_color=='yellow':
    print('you got 10 points')
elif alien_color=='red':
    print('you got 15 points')

alien_color='red'
if alien_color =='green':
    print('you got 5 points')
elif alien_color=='yellow':
    print('you got 10 points')
elif alien_color=='red':
    print('you got 15 points')

#5.6 stages of life

age=int(input("\nEnter your age:"))
if age<2:
    print("You are Baby.")
elif 2<=age<4:
    print("You are Toddler.")
elif 4<=age<13:
    print("You are a kid.")
elif 13<=age<20:
    print("You are a Teenager.")
elif 20<=age<65:
    print("You are an Adult.")
else:
    print("You are Elder.")

#5.7 favourite food
fav_food=['chaat','fulki','dosa']
if 'icecream' in fav_food:
    print("I really like multi-flavoured icecream")
if 'chaat' in fav_food:
    print('chaat is my favourite food since childhood')
if 'pizza' in fav_food:
    print('I really like extra cheesy pizza')
if 'fulki' in fav_food:
    print('fulki is my only favourite food that can fill my stomach within budget')
if 'momos' in fav_food:
    print("momos are weird you feel like you didnt like the taste but then you'll want to eat them again")
if 'dosa' in fav_food:
    print("dosa is one  of those street food that won't affect your health that much")