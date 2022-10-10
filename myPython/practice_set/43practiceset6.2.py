
#6.4
glossary = {
    'print':'To print input',
    'input':'Ask user to input data',
    'int':'User for integers',
    'str':'Used for strings',
    'float':'Used for values that contains decimal',
    'for':'A kind of loop',
    'if':'A statement',
    }
#print(glossary['print'])
for keyword,meaning in glossary.items():
    print(keyword,':',meaning)

#----------------------------------------------------------------------------------------
#6.4
river_dict = {'ganga':'india','amazon':'africa','nile':'egypt'}
for river,country in river_dict.items():
    print('The',river.title(),'runs through',country.title())

print('\n These are the following countries in the list:')
for country in river_dict.values():
    print(country.title())

print('\n And these are the river in the dictionary:')
for river in river_dict.keys():
    print(river.title())

#--------------------------------------------------------------------------------------
#6.5

favorite_languages = ['jen','sarah','edward','phil','tommy','smith','caroline','diana']
poll = ['jen','sarah','edward','phil']
for language in sorted(favorite_languages):
    if language in poll:
        print('\nHey',language.title(),'Thanks for taking the poll, i really appreciate it')
    else:
        print('\nHey',language,'please take the poll, your help will be really appreciated')
        
#-------------------------------------------------------------------------------------------