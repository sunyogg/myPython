

def printmodel(unprintedmodels,completedmodels):
    '''This functionp picks elements from unprintedmodels and use them in a printing 
       statement and then append them to an empty list'''
    while unprintedmodels:
        currentmodels = unprintedmodels.pop()
        print(f"Printing {currentmodels.title()}...")
        completedmodels.append(currentmodels)


    
def showprintedmodel(completedmodels):
    '''This function prints the list of all the elements that have been printed'''
    print("\nHere is the list of printed model:")
    for completedmodel in completedmodels:
        print(f"- {completedmodel.title()}")
