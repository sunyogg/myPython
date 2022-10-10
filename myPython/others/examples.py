'''numbers=[3,1,2,7,5,6,4,8,9,10]
numbers.sort(reverse=True)
print(numbers)

#f stirngs

first='sunyog'
last='lodhi'
full=f"{first}{last}"
print(full)


vehicles=['audi','bugati','bmw']
for vehicle in vehicles:
    if vehicle=='bmw':
        print(vehicle.upper())
    else:
        print(vehicle.title())

metals = {'diamond': 40, 'gold': 30, 'silver': 20, 'bronze': 10, 'iron': 5}
#print(metals['titanium'])
#print(metals.get('titanium','does not exist'))
for metal in metals:
    print(metal)

#lets talk about set()
list = ['chaat','fulki','dosa','idli','chaat','fulki','manchurian','momos']
print(list)
print(set(list))
for food in list:
    print(food)
print('')
for food in set(list):
    print((food))

print(len(list))
print(len(set(list)))


for i in range(3):
    x = int(input('Enter a number = '))
    y = int(input('Enter second number = '))
    z = x+y
    print("The sum of",x,"and",y,'is',z)

#breaking the line in print statement
print('hey dear, how are you doing '
'i hope you are doing fine')


#not able to understand this
fname = 'sunyog'
lname = 'lodhi'
print( 'my full name is',fname,lname)


fname = 'sunyog'
lname = 'lodhi'
full_name = fname,lname
print('my full name is',full_name)
print('my full name is',fname,lname)
print( 'my full name is',fname+' '+lname)
print(f"my full name is {fname} {lname}")


string = 'sunyog'
print(len(string))

list = ['sunyog']
print(list)

name = input("Enter your name : ")
if name != 'mindo' or 'sanjog':
     print('You entered',name)
else:
    print("This is your nick name")

name = 'sanjog', 'sunyog'
print(name)


string = '*'
number = 0
while number <= 10:
    number += 1
    print(string)
    string +='*'
    

#different ways of printing a variable
name = 'sunyog'
surname = 'lodhi'
print('my name is ' + name+' '+surname )
print('my name is',name,surname) #best ?
print (f'my name is {name} {surname}')



def food(fruit):
    for x in fruit:
        print(x)

fav_food = ['apple','mango','banana']
food(fav_food)

def food(fruit):
	for x in fruit:
    	print(x)
        
fav_fruits = ['apple','banana','mango']
food(fav_fruits)'''



'''
number = [12, 35, 9, 56, 24]
number.append('sunyoh')
print(number)
number.append(13)
print(number)
number.insert(0,'sunny')
print(number)
number.insert(0,69)
print(number)


n = 30
if n % 2 != 0 :
    print(n,"Weird")
if n % 2 == 0 and 2 <= n <= 5:  # 2 , 4
    print(n,"Not Weird")
if n % 2 == 0 and 6 <= n <= 20: #6, 8, 10, 12, 14, 16, 18, 20
    print(n,"Weird")
if n % 2 == 0 and n > 20 : # 22, 24, 26, 28, 30...
    print(n,"Not Weird")


#hackerrank problem
lists = [value for value in range(0,21)]
useful_numbers = []

n = int(input())
if n in lists:
    for list in lists:
        if list < n:
            useful_numbers.append(list)
else:
    print("Wrong input")            
    
        
for useful_number in useful_numbers:
                print(useful_number **2)


#leap year
flag = True
while flag:
    year =  int(input())
    if year % 4 == 0:
        if year % 100 != 0 :
            print(year,"is a leap year")
        if year % 100 == 0:
            if year % 400 == 0:
                print(year,"is a leap year")
            else:
                print(year,"is not a leap year")
    if year % 4 != 0:
        print(year,"is not a leap year")
    if (year) == 'quit':
        flag = False

#factorial number

numbers = [value for value in range(1,101)]
factorial_numbers = []
n = int(input('Number = '))
for number in numbers:
    if n >= number:
        factorial_numbers.append(number)
print(factorial_numbers)

import math
result = math.prod(factorial_numbers)
print(result)


result = 1 
for factorial_number in factorial_numbers:
    result = factorial_number * result
    
print(result)


print(2+2)
print("2"+"2")
print("2"+2)
print(2+"2")


#lets define a function that will tell whether a year is leap year or not
a = "leap year"
b = "not a leap year"


def leapyear(n):
    if n % 4 == 0:
        if n % 100 != 0:
            return a
        if n % 100 == 0:
            if n % 400 == 0:
                return a 
            else:
                return b 
    if n % 4 != 0:
        return b 

print(leapyear(2008))


numbers = [value for value in range(1,151)]
requirednumbers = []
n =  int(input())
for number in numbers:
    if number <= n:
        requirednumbers.append(number)
print(requirednumbers)
for requirednumber in requirednumbers:
    result = "1"
    result = result + str(requirednumber)

print(result)

def sum(x,y):
    z = x + y 
    return z  

print(sum(4,8))


def evenodd(x):
    z = 'even'
    v = 'odd'
    if x % 2 == 0:
        return z 
    else:
        return v

print(evenodd(8))


def lens(x):
    return len(str(x))

print(lens('sunyog'))

def petdetail(petname,pettype):
    print('Pet name: ',petname)
    print('pet type: ',pettype)
    print(" ")

petdetail('kaalu','dog')
petdetail('dog','kaalu')
petdetail('tommy') # number of argument should be equal to number of parameter
def formattedname(firstname,lastname):
    fullname = (firstname +' '+ lastname)
    return fullname 

neatlyformattedname = (formattedname('sunyog','lodhi'))
print(neatlyformattedname)
x = 'hello how are you'
print(x.title())
print(x.capitalize())
print(x.casefold())
print(x.swapcase())


# How to reverse a list
numbers = [1,2,3,4,5]
# output = [5,4,3,2,1]'''
'''reqnumbers = []
while numbers:
    no = numbers.pop()
    reqnumbers.append(no)

print(reqnumbers)'''

'''12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print


n = int(input("Enter number of operation you want to perform: "))
numbers = []
for i in range(n):
    x = input("Enter the operation you want to perform: ")
    if x == 'insert':
        a = int(input())
        b = int(input())
        numbers.insert(a,b)
    elif x == 'append':
        c = int(input())
        numbers.append(c)
    elif x == 'remove':
        d = int(input())
        numbers.remove(d)
    elif x == 'pop':
        numbers.pop()
    elif x == 'print':
        print(numbers)
    elif x == 'reverse':
        numbers.reverse()
    elif x == 'sort':
        numbers.sort()



olist = ['sun','moon','earth','mars','venus','jupiter']
clist = olist[:]
clist.append('saturn')
clist.append('neptune')
print(clist)
print(olist)

tupple = ('sun','moon','earth','mars','jupiter')
print(tupple[0])
print(tupple[-5])


dictionaries = {'fname':'sanyog','lname':'lodhi'}
print(dictionaries)
dictionaries['age'] = 20
dictionaries['location'] = 'jabalpur'
print(dictionaries)



class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name} is sitting.")
    
    def rollover(self):
        print(f"{self.name} rolled over.")

my_dog = Dog('kaalu',6)
# object ya instance banate waqt __init__ funciton apne aap hi run ho jata hai

print(f"My dog's name is {my_dog.name} and he is  {my_dog.age} years old.")


my_dog1 = Dog('tommy',12)




strr = 'sanyog'
intt = 81037
flt = 56.027
listt = ['apple','mango','leaves','tree']
tup = ('gun','poweder','danger','eat')
print((hash(strr)))
print((hash(intt)))
print((hash(flt)))
print(hash(tup))
print(tup)
#print(hash(listt))

#print(strr)
#print(intt)
#print(flt)


n = int(input())
listt = []
for i in range(n):
    x = int(input())
    listt.append(x)
tupple = tuple(listt)
print(hash(tupple))


# from  list of duplicate elements to list of unique elements
numbers = [1,2,3,1,2,4,5,]
print(numbers)

uniquen = set(numbers)
print(uniquen)

uniquenlist = list(uniquen)
print(uniquenlist)



n = int(input())
numbers = []
x =  input()
y = x.split()
print(y)
for i in y:
    a = int(i)
    numbers.append(a)
req_numbers = set(numbers)
req_numbers_list = list(req_numbers)
req_numbers_list.sort()
print(req_numbers_list)


a = 5

def update_integer(updated):
    a = updated
    print(a)

def increment_integer(incremented):
    x = a + incremented
    print(x)

print(a)
update_integer(10)
increment_integer(10)
'''






'''s = 'AAABCADDE'
k  = 3
required = []


z = len(s)/3
for i in range(k):
    sliced = s[0:z]
    required.append(sliced)
'''

'''required = []
s_list = []
s = 'AABCAAADA'#'AAABCADDE' 
k = 3
y = len(s)
z = int(y/3)

for i in s:
    s_list.append(i)

reversed = s_list[::-1]    # s_list = ['A', 'A', 'B', 'C', 'A', 'A', 'A', 'D', 'A']
reversed = s_list[::-1]  # reversed = ['A', 'D', 'A', 'A', 'A', 'C', 'B', 'A', 'A']
print(s_list)
print(reversed)

while reversed :
    for i in range(z):
        popped = reversed.pop()
        required.append(popped)
    print(f"-----------------------{required}")
    rewards = set(required)
    lreward = list(rewards)
    print(lreward)
    del required[0:z]'''

    
'''# location = '/Users/sunyoglodhi/Desktop/python/my_work/my_practice/11-filesandexceptions/greet.txt'

import os
print(os.listdir()) # this method returns the list of files in the current working directory
print(os.getcwd()) # this method returns the address of directory we are in currently 
os.chdir('/Users/sunyoglodhi/Desktop/python/my_work/my_practice/11-filesandexceptions') # this functon changes the current working directory to the address we have give
print(os.getcwd()) # this method returns the address of directory we are in currently 

with open('greet.txt') as f:
    content = f.read()
    print(content)'''


'''k = 5
listt = list(a for a in range(k))
print(listt

mlist = []
for i in range(2):
    x = (input())
    xl = x.split()

    for xs in xl:
        mxl = int(xs)
        mlist.append(mxl)

print(mlist)'''

sting = 'hello, my name is sunyog!'
'''splitted = sting.split()
print(splitted)

a = (type(sting))
print(a)
if a == "<class 'str'>":
    print('true')
else:
    print('false')
'''

def func(x,ans):
    if (x==0):
        return 0
    else:
        return func(x-1,x+ans)


print(func(2,66))

























