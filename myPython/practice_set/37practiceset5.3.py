#5.8

usernames=['eric','john','dan','admin','carl','mark']
for username in usernames:
    if username=='admin':
        print('hello',username,',do you wanna see the status report')
    else:
        print('hello',username,', thanks for logging in to our site')


#5.9
usernames=[]
if usernames:
    for username in usernames:
        if username=='admin':
            print('hello admin do you wanna see the status report')
        else:
            print('hello',username,'thanks for loging in to our site')
else:
    print('we need to find user for our site')


#5.10
current_users=['Eric','John','dan','admin','carl','mark']
new_users=['eric','adam','steve','smith','andrew','John']

current_users_lower=[user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('the username',new_user,'is already taken, please choose another one.')
    else:
        print('the username',new_user,'is unique, you can proceed further.')


#5.11
numbers=[1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number==1:
        print('1st')
    elif number==2:
        print('2nd')
    elif number==3:
        print('3rd')
    else:
        print(str(number)+'th')
