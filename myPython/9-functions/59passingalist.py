
def greet_users(names):
    for name in names:
        print("Hello",name.title(),"how are you?")

usernames = ['jack','tom','smith','sean']
greet_users(usernames)

#---------------------------------------------------------------------------------------------
# transferring elements of one list to another without using functions
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_designs = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("printing",current_design+'...')
    completed_designs.append(current_design)

print(completed_designs)
'''
for unprinted_design in unprinted_designs:
    current_design = unprinted_design
    completed_designs.append(current_design)'''

print(completed_designs)
#---------------------------------------------------------------------------------------------
# writing the above code using functions
# transfering elements of one list to another using functions
def design(unprinted_designs,completed_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing",current_design+'...')
        completed_designs.append(current_design)
    #print(completed_designs)
    
def showprintedmodel(completemodels):
    print("Following model has been printed:")
    for completemodel in completemodels:
        
        print("->",completemodel)

requested_designs = ['toy_car','screw_driver','chopper','angle']
accomplished_designs = []

design(requested_designs,accomplished_designs)
showprintedmodel(accomplished_designs)

print(requested_designs) #see how the original list of requested designs gets empty.

#---------------------------------------------------------------------------------------------
