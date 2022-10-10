#4.10
vehicles=['bullet','honda','suzuki','yamaha','harley','tesla','bmw','audi','bugati']
print("the first three items of the list are:")
for vehicle in vehicles[0:3]:
    print(vehicle)

print("\nthree items from the middle of the list are:")
for vehicle in vehicles[3:6]:
    print(vehicle)

print("\nthe last three items of the list are:")
for vehicle in vehicles[-3:]:
    print(vehicle)

#4.11
foods=['fulki','chaat','momos','dosa','idli','chineese']
friend_foods=foods[:]

foods.append('pizza')
friend_foods.append('burger')

print("\n",foods)
print(friend_foods)

print("\nmy favourite food are:")

for food in foods[:]:
    print(food)

print("\nmy friends favourite food are:")
for friend_food in friend_foods[:]:
    print(friend_food)

#4.12
#i have already used loops in above exercise


