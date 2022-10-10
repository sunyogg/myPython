
x = 20
floor = 0
if x%10 == 0:
    floor = x/10
    print(int(floor))
elif x%10 != 0:
    floor = (int(x/10) + 1)
    print(int(floor))

print(abs(10-12))



flavors = ["strawberry", "pineapple", "vanilla", "chocolate"]

def printList(aList):
    if type(aList)  == type(2):
        print("Please only pass List and String as argument.")
    else:
        for items in aList:
            print(items.title())

numLt = [12, 345, 2, 4, 3466]
for i in numLt:
    print(i)

