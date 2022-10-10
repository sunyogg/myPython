try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide a number by zero")

print('this line will get printed even if python gets an error above')

# ---------------------------------------------------------------------------------------------------

print("Enter two numbers and I'll divide them:")
print("Press 'q' to quit the program.")

while True:
    x = input("-> ")
    if x == 'q':
        break
    y = input("-> ")
    if y == 'q':
        break
    try:
        answer = (int(x)/int(y))
    except ZeroDivisionError:
        print("Not defined. You can't divide a number by zero.")
    else:
        print(answer)

# ---------------------------------------------------------------------------------------------------

try:
    with open('python.txt') as f:
        content = f.read()
    
except FileNotFoundError:
    print("Oops! The file you entered does not exist.")

else:
    print(content)

# ---------------------------------------------------------------------------------------------------
# working with multiple files to analyze text

def count_words(filename):
    """ Count the approximate number of words in a file"""
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        print("Oops! The file you entered does not exist.")

    else:
        # count the approximate number of words in a file
        listwords = content.split()
        nwords = len(listwords)
        print(f'This text file has {nwords} words. ')

count_words('/Users/sunyoglodhi/Desktop/python/resources-pcc/chapter_10/alice.txt')
count_words('hell.txt')
count_words('/Users/sunyoglodhi/Desktop/python/resources-pcc/chapter_10/little_women.txt')
count_words('/Users/sunyoglodhi/Desktop/python/resources-pcc/chapter_10/moby_dick.txt')

# we could have also used the list of names of books and then used a for loop to
# count the number of words of every book in the list, but since the books are not
# in the same directory so here we are providing complete path of the file to 
# the function count_words()

# ---------------------------------------------------------------------------------------------------

# failing silently
# To make a program fail silently, you write a try block as usual, but you 
# explicitly tell Python to do nothing in the except block. Python has a pass 
# statement that tells it to do nothing in a block

def count_words(filename):
    """ Count the approximate number of words in a file"""
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        pass # see how we have used pass here inorder to not get any output
             # if the programs fails to run, in other words failing silently.

    else:
        # count the approximate number of words in a file
        listwords = content.split()
        nwords = len(listwords)
        print(f'This text file has {nwords} words. ')

count_words('/Users/sunyoglodhi/Desktop/python/resources-pcc/chapter_10/alice.txt')
count_words('hell.txt')
count_words('/Users/sunyoglodhi/Desktop/python/resources-pcc/chapter_10/little_women.txt')
count_words('/Users/sunyoglodhi/Desktop/python/resources-pcc/chapter_10/moby_dick.txt')


# ---------------------------------------------------------------------------------------------------



