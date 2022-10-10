
# remove is used when you want to remove an item from the list
# you know the value of.
#1
vehicles=['honda','maruti','yamaha','harley','suzuki']
print(vehicles)
vehicles.remove('honda')
print(vehicles)


#2
vehicles=['honda','maruti','yamaha','harley','suzuki']
cheapest_vehicle='maruti'# removed value ko hum baad me access to nahi kar sakte, lekin
#remove karne se pehle usse kisi variable me store kar ke baad me use karr skte hai
vehicles.remove(cheapest_vehicle)
print(cheapest_vehicle,"makes most affordable vehicles")