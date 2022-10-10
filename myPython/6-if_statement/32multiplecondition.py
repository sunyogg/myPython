#using "and" to test multiple conditions
x=int(input("Enter your age="))
y=int(input("Enter your brothers age="))
if x and y >= 18:
    print("You guys can book a ticket for the spa.")
else:
    print("you guys are below 18 and cannnot enter our spa.")  


#using "or" to test multiple conditions
x=int(input("\nEnter your age="))
y=int(input("Enter your brothers age="))
if x or y >= 18:
    print("You guys can book a ticket for the jurrasic park.")
else:
    print("you guys are below 18 and cannnot enter jurrasic park.")  


#Checking Whether a Value Is in a List using "in" and "not in"
number=list(range(0,100))
x=int(input("Enter a number="))
if x in number:
    print("number is in the list")
else:
    print("the number is not in the list")


#checking whether a value is in or not in list
#1)
flavour=['chocolate','vanila','strawberry','elaichi']
print('orange' in flavour)
print('spicy' not in flavour)

#2)
banned_user=['john','jack','dave','david','smith']
user=str(input('Enter your name:'))
if user in banned_user:
    print('you are a banned user in our site, please go away')
else:
    print('welcome to online chat station',user)

