#4.3
'''
for numbers in range(0,21):
    print(numbers)
#4.4 and 4.5

million=list(range(0,1000000))
print(min(million))
print(max(million))
print(sum(million))

#4.6
odd=list(range(1,21,2))
print(odd)

#4.7
multiples=list(range(0,31,3))
print(multiples)'''

#4.8
cubes=[]
for values in range(0,10):
    cube=values**3
    cubes.append(cube)
print(cubes)  

#4.9
#different and more conscise approach
cubes=[values**3 for values in range(0,10)]