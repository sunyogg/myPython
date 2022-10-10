#1
#poping an item from the list
vehicles=['honda','maruti','yamaha','harley','suzuki']
print(vehicles)
popped_vehicles=vehicles.pop() #storing popped value in a variable so that we can print it later
print(vehicles) #this will print popped list
print(popped_vehicles) #this will prove that we have access to popped item


#2 using the popped item for soome purpose
brothers=['sunyog','suyog','sourabh','prasoon','pratik']
eldest_brother=brothers.pop()
print("my eldest brother is",eldest_brother.title())


brothers=['sunyog','suyog','sourabh','prasoon','pratik']
youngest_brother=brothers.pop(1) #you can pop any item of the list with index number
print("my youngest brother is",youngest_brother.title())