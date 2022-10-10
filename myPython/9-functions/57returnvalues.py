
#An explicit return statement immediately terminates a function execution and sends 
#the return value back to the caller code.
def add(a,b):
    print(a + b)
    print(a + b + 3)
    return a + b
    print(a + b + 5)

add(8,2)
#--------------------------------------------------------------------------------------------------

def full_name(fname,lname):
    fullname = (fname.title() + ' ' + lname.title())
    return fullname

name = full_name('sunyog','lodhi')
print(name)
#--------------------------------------------------------------------------------------------------

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#--------------------------------------------------------------------------------------------------
def negative(x):
    print(x * -1)
negative(3)

def negatives(x):
    return (x * -1)

negative_value = negatives(8)
print(negative_value)

#--------------------------------------------------------------------------------------------------
# making an argument optional
# middle name example

def getformattedname(fname,lname,mname = ''):
    if mname:
        formattedname = f"{fname} {mname} {lname}"
        return formattedname.title()
    else:
        formattedname = f"{fname} {lname}"
        return formattedname.title()

a = getformattedname('sunyog','lodhi','singh')
b = getformattedname('sunyog','lodhi')

print(a)
print(b)

#--------------------------------------------------------------------------------------------------
#returning a dictionary

detail = {}
def formattedname(fname,lname):
    detail['firstname'] = fname.title()
    detail['lastname'] = lname.title()
    return detail
a = formattedname('sunyog','lodhi')
print(a)



def formattedname(fname,lname):
    detail = {'first':fname.title(),'second':lname.title()}
    return detail
a = formattedname('sanyog','lodhi')
print(a)



detail = {}
def formattedname(fname,lname,mname = ''):
    if mname:
        detail['first'] = fname.title()
        detail['middle'] = mname.title()
        detail['last'] = lname.title()       
        return detail

    else:
        detail['first'] = fname.title()
        detail['last'] = lname.title()
        return detail

print(formattedname('suyog','lodhi'))
print(formattedname('suyog','lodhi','singh'))



def formattedname(fname,lname,age = None):
        detail = {'first':fname,'last':lname}
        if age:
            detail['age'] = age
        return detail
        
a = formattedname('sanyog','lodhi',20)
b = formattedname('sanyog','lodhi')
print(a)
print(b)

#--------------------------------------------------------------------------------------------------
# Using a Function with a while Loop
def formattedname(fname,lname):
    name  = f"{fname.title()} {lname.title()}"
    return name

while True:
    print("Enter your name below.")
    print("Press 'q' to quit the program ")

    a = (input("Enter your first name: "))
    if a == 'q':
        break

    b = (input("Enter your last name: "))
    if b == 'q':
        break

    naam = formattedname(a,b)
    print(f"hello! {naam}. How are you?")

#--------------------------------------------------------------------------------------------------


