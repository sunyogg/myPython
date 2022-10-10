
#positional arguments
def pet_type(type,name):
    print("\nI have a ",type)
    print("Whose name is",name)

pet_type('dog','kaalu')

#--------------------------------------------------------------------------------------------

#multiple function calls
def pet_description(type,name):
    print("\nI have a ",type)
    print("Whose name is",name)

pet_description('dog','kaalu')
pet_description('fish','anabell')
pet_description('cat','meow')

#--------------------------------------------------------------------------------------------
#Order Matters in Positional Arguments
def pet_type(type,name):
    print("\nI have a ",type)
    print("Whose name is",name)

pet_type('kaalu','dog')
pet_type('dog','kaalu')

#--------------------------------------------------------------------------------------------

# keyword arguments
# You directly associate the name and the value within the argument
def pet_description(type,name):
    print('I have a',type)
    print("And the",type+"'s name is",name.title())
#see how position of argument doesn't matter
pet_description(type = 'dog', name = 'trigger')
pet_description(name = 'tiger',type = 'dog')

#--------------------------------------------------------------------------------------------
#default values
def pet_description(name,ptype = 'dog'):
    print("I have a",ptype)
    print("and the",ptype+"'s name is",name)
pet_description('kaalu')
pet_description('tiger')
pet_description('kaalu','cat')
pet_description(name = 'trigger',ptype = 'cat')

# error  -> non-default argument follows default argument
#When you use default values, any parameter with a default value needs to be listed 
#after all the parameters that don’t have default values. This allows Python to 
# continue interpreting positional arguments correctly.
def pet_description(ptype = 'dog',name):
    print("I have a",ptype)
    print("and the",ptype+"'s name is",name)
pet_description('kaalu')


def pet_description(pet_name,pet_type = 'dog'):
    print('-> pet name: ',pet_name)
    print('-> pet type: ',pet_type)

pet_description('mauli')
pet_description('goda',pet_type = 'fish')
#pet_description(pet_type = 'lizard','booni')# Positional argument cannot appear after keyword arguments
pet_description(pet_name = 'groomi',pet_type = 'reptile')
pet_description('meow','cat')





