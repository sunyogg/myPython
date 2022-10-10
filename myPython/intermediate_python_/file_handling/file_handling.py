'''
f = open('text.txt', 'r')
print(f.mode)
f.close()
'''
'''
with open ('text.txt', 'r') as f:
    size_to_read = 10
    #print(f.tell())
    content = f.read(size_to_read)
    print(content, end='')

    f.seek(2)
    #print(f.tell())
    content = f.read(size_to_read)
    print(content)
    #print(f.tell())
    while len(content) > 0:
        print(content, end='-')
        content = f.read(size_to_read)

with open('text.txt', 'w') as f:
    f.write('hello sanjog')
    f.seek(0)
    f.write('r')

# copying a file using Python file handling.
with open('Unknown.pdf', 'rb') as rf:
    with open('Unknown_copy.pdf', 'wb') as wf:
        for line in rf:
            wf.write(line)
'''