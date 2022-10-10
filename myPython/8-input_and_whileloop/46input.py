
name = input("Enter your name: ")
print('Hello!',name,'How are you?')
#---------------------------------------------------------------------------------------------------------
prompt = 'Please tell your name, so that we can print a personalized mesasge for you. '
prompt +="ok. Now tell me your name = "
name = input(prompt)
print("Hello !",name,"How are you?")

#---------------------------------------------------------------------------------------------------------

age = int(input("Enter your age = "))
bage = int(input("Enter your brothers age = "))
sum = (age)+ (bage) + 5
print("The sum of yours, your brother age and 5 is :",sum)

#---------------------------------------------------------------------------------------------------------

height = float(input("Enter your height in feet: "))
#height = float(height)
if (height) >= 5:
    print("You are eligible for the rollercoster ride!")
else:
    print("Sorry! You are not eligible to ride.")

#---------------------------------------------------------------------------------------------------------

#modulo operator divides one number and returns remainder.
print('Even Odd determiner.')
while True:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(number,"is even.")
    else:
        print(number,'is odd.')

#---------------------------------------------------------------------------------------------------------
