#1
#sorting a list permanantly
vehicles=['honda','maruti','yamaha','harley','suzuki','bmw,','audi']
print(vehicles)
vehicles.sort() #sorted alphabetically
print(vehicles) #in both the cases the order of list is permanantly changed
vehicles.sort(reverse=True) #sorted alphabetically but reversed
print(vehicles)

#2
#sorting a list temporarily, such that the original order still exist
#sorted(vehicles)
vehicles=['honda','maruti','yamaha','harley','suzuki','bmw,','audi']
print("\nhere is the original list\n",vehicles)
print("\nhere is the sorted list\n",sorted(vehicles))
print("\nhere is the original list again",vehicles)

#3
#printing a list in reverse order
#vehicles.reverse()
vehicles=['honda','maruti','yamaha','harley','suzuki','bmw,','audi']
print(vehicles)
vehicles.reverse()
print(vehicles)
vehicles.reverse()
print(vehicles)
#reverse changes the order of the list permanantlly but we can revert back to
#original order applying reverse again to the reversed vehicles


#4 finding the length of list

vehicles=['honda','maruti','yamaha','harley','suzuki','bmw,','audi']
print(len(vehicles))
