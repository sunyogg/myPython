#1 appending an item to a list
names=['sunyog','suyog','pratik','prasoon','varun']
print(names)

names[-1]="arun" #exchanging an item from the list
print(names)

names.append("amit")
print(names)

#2  appending multiple items to an empty list
vehicles=[] #an empty list
vehicles.append("harley davidson")
vehicles.append("honda")
vehicles.append("tesla")
print(vehicles)

#3 #asking users for their name and then putting that name into the list(by myself)
names = []
x =int(input("Enter your name - "))
names.append(x)
print(names)
