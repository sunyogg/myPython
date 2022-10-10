
courses = ['physics', 'maths','python','statistics']
courses2 = ['trigonometry', 'psychology', 'web development']

#courses.extend(courses2)
# courses.append(courses2)
#courses.extend(courses)
#courses2.extend(courses)
#for index, course in enumerate(courses, start=1)  :
    #print(index,course)

stin = ', '.join(courses)
# print(stin)
lis = stin.split(', ')
#print(lis)

# ------------------------------------------------------------

courses = ['physics', 'maths', 'python', 'statistics']

x = (enumerate(courses, start = 1))
for i,s in x :
    print(i, s)

# ------------------------------------------------------------
# tuple

courses = ('physics', 'maths', 'python', 'statistics')
courses.add('tuple')
print(courses)


# ------------------------------------------------------------

cs_courses = {'physics', 'maths','python','statistics'}
art_courses = {'maths', 'python', 'history', 'polity'}


print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

print(cs_courses)

# ------------------------------------------------------------

# empty list  
empty_list = []
empty_list = list()

# empty tuple
empty_tuple = ()
empty_tuple = tuple()

# empty set
not_empty_set = {} # This is not an empty set, it's an empty dictionary
empty_set = set() # This is an empty set.

# ------------------------------------------------------------
student = {'student':'jane', 'age':19, 'course': ['python', 'javascript', 'DSA']}
print(student)
student.update({'student':'john', 'age': 20, 'course':['c', 'c++']})
print(student)


print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key,':',value)

# ------------------------------------------------------------
 
admin = True

if admin:
    # The code above means if admin equals to True
    print('admin is true.')

if not admin:
    # the code above means if admin equals to False
    print('admin is false')

# ------------------------------------------------------------ 


print('hello world')

