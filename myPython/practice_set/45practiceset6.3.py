
#6.7

info1 = {'fname':'sunyog','lname':'lodhi','age':20,'location':'chowkital'}
info2 = {'fname':'arun','lname':'lodhi','age':30,'location':'bahoripar'}
info3 = {'fname':'saurabh','lname':'lodhi','age':21,'location':'lakhnadon'}

people = [info1,info2,info3]

for individual in people:
    full_name = individual['fname'].title(), individual['lname'].title()
    print("They are",individual['fname'].title(), individual['lname'].title(),'and '
    'they are',individual['age'],'years old and they live in',individual['location'].title())
#-------------------------------------------------------------------------------------------------------
#6.8
pet1 = {'type':'dog','owner':'sunyog'}
pet2 = {'type':'cat','owner':'suyog'}
pet3 = {'type':'turtel','owner':'saurabh'}

pets = [pet1,pet2,pet3]
for pet in pets:
    print("this is a",pet['type'],'owned by',pet['owner'])
#-------------------------------------------------------------------------------------------------------
#6.9
fav_places = {'suyog':['mizoram','assam','california'],
    'prasoon':['london'],
    'pratik':['dubai','uk','nepal','australlia']
    }
for name,places in fav_places.items():
    if len(places) > 1:
        print("These are the places that",name.title(),"wants to visit: ")
        for place in places:
            print('\t-> ',place)
        
    else:
        print("This is the only place that",name.title(),"wants to visit:")
        for place in places:
            print('\t-> ',place)

 #-------------------------------------------------------------------------------------------------------   
#6.10

fav_numbers = {'suyog':[2,6,31],
    'sunyog':[28,7,20],
    'prasoon':[14,69],
    'pratik':[1]
    }
for name,numbers in fav_numbers.items():
    if len(numbers) > 1:
        print("Favourite numbers of",name,'are:')
        for number in numbers:
            print('\t->',number)
    else:
        print("The favourite number of",name,'is:')
        for number in numbers:
            print('\t->',number)

#-------------------------------------------------------------------------------------------------------   
#6.11

cities = {'delhi':{'country':'india','population':10000,'fact':'pollution'},
    'california':{'country':'usa','population':5000,'fact':'city of the world'},
    'tokyo':{'country':'japan','population':2500,'fact':'anime city'}}

for city,infos in cities.items():
    print(" \n ",city.title())
    for question,answer in infos.items():
        print('\t->',question.title(),':',answer)










