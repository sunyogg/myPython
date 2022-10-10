#if statement
age=int(input("Enter your age="))
if age >= 18:
    print("you are old enough to vote")
    print("you can register yourself to vote")


#if else statement
print("\nYou are about to watch restricted content.\nplease enter your age.")
age=int(input("\nEnter your age:"))
if age >= 18:
    print("You can watch the restricted content. ")
else:
    print("You are not old enough to watch the restricted content.")

#if elif else chain
#1) simple
print("\nYour are about to buy the tickets for amusement park")
print("Please enter your age so that we can tell you how much you have to pay")
age=int(input("\nEnter your age:"))
if age < 13:
    print("You are not old enough to enter the amusement park.")
    print("Please note that you can always come with your guardian")
elif age < 18:
    print("Please pay 3$ bill in the vending machine.")
else:
    print("Please pay 5$ bill in the vending machine")


#2) different way
print("\nYour are about to buy the tickets for amusement park")
print("Please enter your age so that we can tell you how much you have to pay")
age=int(input("Enter your age:"))
if age < 6:
    price='3$'
elif age < 18:
    price='5$'
elif age >= 18:
    price='10$' 

'''Python does not require an else block at the end of an if-elif chain. Some- times 
an else block is useful; sometimes it is clearer to use an additional elif statement 
that catches the specific condition of interest:'''

print("you are",age,"years old, please pay:",price)

#3)
'''The if-elif-else chain is powerful, but it’s only appropriate to use when you just 
need one test to pass. As soon as Python finds one test that passes, it skips the 
rest of the tests. This behavior is beneficial, because it’s efficient and allows you
to test for one specific condition.
However, sometimes it’s important to check all of the conditions of interest. In this 
case, you should use a series of simple if statements with no elif or else blocks. This
technique makes sense when more than one condi- tion could be True, and you want to 
act on every condition that is True'''

#yaha ek se jyada condition sahi ho sakti hai to sirf "if" ka use kiya hai taaki 
#interpretor sirf ek condition sahi hone me ruke na, if ka use karne se agar koi ek bhi 
#condition sahi bhi hoti hai to bhi saare condition test kari jayengi
requested_flavours=['chocolate','vanilla']
if 'chocolate' in requested_flavours:
    print('adding chocolate')
if 'strawberry' in requested_flavours:
    print('adding strawberry')
if 'vanilla' in requested_flavours:
    print('adding vanilla')
if 'elaichi' in requested_flavours:
    print('adding elacihi')

print("finished making icecream\n")

#This code would not work properly if we used an if-elif-else block, because the code 
#would stop running after only one test passes. Here’s what that would look like:
requested_flavours=['chocolate','vanilla']
if 'chocolate' in requested_flavours:
    print('adding chocolate')
elif 'strawberry' in requested_flavours:
    print('adding strawberry')
elif 'vanilla' in requested_flavours:
    print('adding vanilla')
elif 'elaichi' in requested_flavours:
    print('adding elacihi')

print("finished making icecream")





