
# 10.3 
# the message we are typing is getting stored at input.txt

with open('guest.txt','w') as file:
    x = input("Enter the message you want to store in the file: ")
    file.write(x)

# --------------------------------------------------------------------------------------------

# 10.4

print("Enter your name below or enter 'quit' to stop the program.")
while True:
    with open('guest_book.txt','a') as file:
        x = input("Enter your name: ")
        if x != 'quit':
            file.write(f"{x}\n") # here using f string is better than using any other conventional method.
            print(f" Hey {x}! thanks for visiting our hotel.")
            continue
        else:
            print("Quiting program...")
            break

# --------------------------------------------------------------------------------------------
# 10.5 

print("Enter below, why you like python or type quit to quit the program.")
while True:
    
    with open('whypython.txt','a') as file:
        x = input("Why you like python: ")
        if x != 'quit':
            file.write(f"{x}\n")
            continue
        else:
            print("Quitting program...")
            break

# --------------------------------------------------------------------------------------------


