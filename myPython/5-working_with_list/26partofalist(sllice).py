
#slicing a list
'''vehicles=['bullet','honda','suzuki','yamaha','harley','tesla','bmw']
print(vehicles[0:3])
print(vehicles[:4])
print(vehicles[2:])
print(vehicles[-3:])
print(vehicles[:])


#looping through a slice
print("\nhere is the list of luxury vehicle")
for vehicle in vehicles[-3:]:
    print(vehicle)'''

#a)
#copying a list(both the list are separated once we copy the list)
my_vehicles=['bullet','honda','suzuki','yamaha','harley','tesla','bmw']
my_friends=my_vehicles[:]#separate list banani hai to slice([:])ka use karna hi padega

my_vehicles.append('audi')# this proves that both the list are different
my_friends.append('jeep')

print("my vehicles are:")
print(my_vehicles,"\n")
print("\nmy friends vehicles are:")
print(my_friends)

#b)
#here’s what happens when you try to copy a list without using a slice:
my_vehicles=['bullet','honda','suzuki','yamaha','harley','tesla','bmw']
my_friends=my_vehicles #notice that i didnt use slice herer
my_vehicles.append('audi')
my_friends.append('jeep')

print("\nmy vehicles are:")
print(my_vehicles,"\n")
print("\nmy friends vehicles are:")
print(my_friends)



