'''
# input = 5
# output = 1 4 9 16

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

#-----------------------------------------------------------------------------------------

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

#-----------------------------------------------------------------------------------------

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

#-----------------------------------------------------------------------------------------

# input = 5
# output = 12345

numbers = [value for value in range(2,151)]
imnumbers = []
n = int(input())
for number in numbers:
    if number <= n:
        imnumbers.append(number)
print(imnumbers)
result = "1"
for imnumber in imnumbers:
    result = result + str(imnumber)
    print(result)
#print(result)

#-----------------------------------------------------------------------------------------
# there is an empty list, then asking user for inputs about whatever they wanna do 
# with the list like if they want to insert or append any element or pop or remove any
# elements or sort or reverse the list

numbers = []
n = int(input())
for i in range(n):
    x = input('write: ')
    x = x.split()
    if x[0] == 'insert':
        numbers.insert(int(x[1]),int(x[2]))
    elif x[0] == 'append':
        numbers.append(int(x[1]))
    elif x[0] == 'pop':
        numbers.pop()
    elif x[0] == 'print':
        print(numbers)
    elif x[0] == 'sort':
        numbers.sort()
    elif x[0] == 'reverse':
        numbers.reverse()
    elif x[0] == 'remove':
        numbers.remove(int(x[1]))

#-----------------------------------------------------------------------------------------
# print runner up from the group of number given by the user:
# input: 6
#        1 2 3 6 6 5
# output: 5

#n =  int(input("Items in list: ")) I don't think this thing is required
req_numbers = []
x = input()
numbers = x.split()
for number in numbers:
    a = int(number)
    req_numbers.append(a)

req_number_set = set(req_numbers)
req_number_list = list(req_number_set)

req_number_list.sort()
print(req_number_list)

len_req_list = len(req_number_list)
c = len_req_list - 2
print(req_number_list[c])

#-----------------------------------------------------------------------------------------

'''


# # input = 1222311
# # output = (1, 1) (3, 2) (1, 3) (2, 1)


# # First, the character 1 occurs only once. It is replaced by (1,1) . Then 
# # the character 2 occurs three times, and it is replaced by (3,2) and so on.

# #num = str(input())

# num = '1231331'
# nums = []

# final = []
# #print(num.index())

# for i in num:
#     nums.append(i)

# print(nums)

# for k in nums:
#     lis = []
#     index_of_k = nums.index(k)
#     index_of_k1 = (num.index(k) + 1) 

#     if index_of_k == num[index_of_k1]:
#         lis.append(k)
#         lis.append(num[index_of_k1])
        

#     else:
#         lis.append(k)

#     final.append(lis)


#-----------------------------------------------------------------------------------------

# taxi driver

t = int(input())
nums = []
strin = []
condition = []

for i in range(t):
    strings = str(input())
    strum = strings.split(" ")
    strin = []

    for i in strum:
        strin.append(int(i))
    if strin[0]<strin[1]:
        condition.append("FIRST")
    elif strin[0] == strin[1]:
        condition.append("ANY")
    else:
        condition.append("SECOND")

for i in condition:
    print(i)

#-----------------------------------------------------------------------------------------


# nums = [1, 2, 3, 4, 5, 9]

# index of maximum number.
# print(nums.index(max(nums)))

# print(nums.index(3))