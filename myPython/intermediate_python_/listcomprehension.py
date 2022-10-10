# list comprehension
'''
num = [1,2,3,4,5,6,7,8,9,10]

my_num = [n for n in num if n%2 == 0]

print(my_num)

'''
# list comprehension in nested loops

my_list = []
for numbers in range(4):
    for letters in 'abcd':
        my_list.append((numbers,letters))
#print(my_list)

# using list comprehesion for above loop
my_list1 = [(i,s)for i in range(4) for s in 'abcd']
#print(my_list1)
# my_list = [list comprehension conditional statement]
# --------------------------------------------------------------

# Dictionary comprehension

names = ('don','van','tobby','eric','corye')
surnames = ('houser', 'mathews', 'haddin', 'metthinson', 'mato')

namesandsur = zip(names, surnames)
#print(namesandsur)

my_dict = {}
for name, sur in zip(names, surnames):
    my_dict[name] = sur


my_dict = {name:sur for name,sur in zip(names,surnames) if name != 'don'}
#print(my_dict)
  
# my_dict = {dictionary comprehension conditional statement}

# --------------------------------------------------------------
# set comprehension

nums = [8,2,3,7,4,8,3,7,2,8,4,7,2,3]
my_set = set()

for i in nums:
    my_set.add(i)

#print(my_set) 

my_set = {n for n in nums}
#print(my_set)

my_gen = (n*n for n in nums)
for n in my_gen:
    print(n)

