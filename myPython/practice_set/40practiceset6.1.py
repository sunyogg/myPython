
#6.1
sunyog_l={'first':'sunyog','last':'lodhi','age':20,'city':'jabalpur'}
print(sunyog_l['first'].title())
print(sunyog_l['last'].title())
print(sunyog_l['age'])
print(sunyog_l['city'].title())


#6.2
fav_number={
    'ankit':28,
    'aman':36,
    'ayush':69,
    'anshul':7,
    'anunsh':99
    }
print(fav_number)
print('favourite number of every person:')
print('ankit:',fav_number['aman'])
print('aman:',fav_number['ankit'])
print('ayush:',fav_number['ayush'])
print('ashul:',fav_number['anshul'])
print('anush:',fav_number['anush'])


#6.3
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }
word='\nstring'
print(word.title(),":",glossary['string'])

word='\ncomment'
print(word.title(),':',glossary['comment'])

word='\nlist'
print(word.title(),':',glossary['list'])

word='\nloop'
print(word.title(),':',glossary['loop'])

word='\ndictionary'
print(word.title(),':',glossary['dictionary'])
