# 10.1 

# reading complete file at once
with open('learningpython.txt') as file:
    content = file.read()

print('\n',content,'\n')


# reading a file by one line at a time
with open('learningpython.txt') as file1:
    for line in file1:
        print(line.strip())
print('')


# reading a file by first storing the file's line in a list
with open('learningpython.txt') as file2:
    lines = file2.readlines()
for line in lines:
    print(line.strip())


# -------------------------------------------------------------------------------------------

# 10.2
# getting hold on replace(), before doing the excercise. 

pets = 'I really like dogs. You know theres a different feel in dogs. I love dogs'

petcs = pets.replace('dogs','cats')
petcd = pets.replace('dogs','cats',1)
petc = pets.replace('dogs','cats',-1)

print(pets)

print(petc)
print(petcd)
print(petcs)


with open('learningpython.txt') as file:
    for line in file:
        replaced = line.replace('python','c')
        print(replaced.strip())

# -------------------------------------------------------------------------------------------