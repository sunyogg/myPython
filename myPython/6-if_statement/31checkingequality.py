
car='Audi'
print(car=='Audi')
print(car=='audi')#equality operator is case sensitive
print(car.lower()=='audi')#if case sensitivity doesnt matter, we can lower the case before
print(car)                #checking the equality and original value does not get affected
print(car=='bmw')
print(car!='honda')

#numerical value
x=int(input("Enter your age:"))
if x >= 18:
    print("You can access our site")
else:
    print("Sorry you are below 18, you cannot enter the site")

