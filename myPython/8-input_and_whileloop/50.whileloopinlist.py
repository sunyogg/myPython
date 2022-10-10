'''
#moving items from one list to another using while loops

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user:",current_user.title())
    confirmed_users.append(current_user)
print("\n The following user has been verified")
 # Display all confirmed users.
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#---------------------------------------------------------------------------------------------

names = ['alice','sharon','caroline','smith','jack','dave','jessica']
new_names = []
while names:
    x_name = names.pop()
    new_names.append(x_name)
print(new_names)
#for new_name in new_names:
#    print(new_name)

#---------------------------------------------------------------------------------------------

#Removing all instances of specific values from a list
names = ['smith','sharon','smith','alice','jack','jessica','caroline','alice']
print(names)
while 'smith' in names:
    names.remove('smith')
print(names)
'''
#-----------------------------------------------------------------------------------------------

#creating an empty dictionary
responses = {}

while True:
    #asking response with name
    name = input("Enter your name: ")
    fav = input("Enter the name of the city you wanna visit: ")
    #adding response into the empty dictionary
    responses[name] = fav
    #asking user they wanna passs the response to other or stop here
    ask = input("do you wanna pass the response to another person: yes/no: ")
    if ask == 'yes':
        continue
    if ask == 'no':
        break
#printing the response
for name,fav in responses.items():
    print(name,":",fav)



