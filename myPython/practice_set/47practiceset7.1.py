#7.1

message = "Please enter the name of the car "
message += "that you would like to rent: "
car = input(message)
print("Let me see, if i can get you a",car.title()+'...')

#7.2
print("Subway")
seat = int(input("Please enter the number of people that are in your dinning gruop: "))
if seat >= 8 :
    print("We're really sorry. You have to wait until we arrange a table for",seat)
else:
    print("Your table for",seat,"is ready. Happy dinning!")

#7.3
print('Multiple of 10')
number = int(input("Please enter the number: "))
if number % 10 == 0:
    print(number,"is a multiple of 10.")
else:
    print(number,"is not a multiple of 10.")


