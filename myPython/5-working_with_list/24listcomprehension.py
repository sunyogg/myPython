'''1)A list comprehension combines the for loop and the creation of new elements into
     one line, and automatically appends each new element.
 2)To use this syntax, begin with a descriptive name for the list, such as squares.
   Next, open a set of square brackets and define the expression for the values you want
   to store in the new list. In this example the expression is value**2, which raises
   the value to the second power. 
   Then, write a for loop to generate the numbers you want to feed into the expression,
   and close the square brackets. The for loop in this example is for value in 
   range(1,11), which feeds the values 1 through 10 into the expression value**2.
   Notice that no colon is used at the end of the for statement.'''


numbers=[number for number in range(0,21)]
print(numbers)

evens=[even for even in range(0,21,2)]
print(evens)

numbers=[values**2 for values in range(0,11)]
print(numbers)

current_users=['Eric','John','dan','admin','carl','mark']
current_users_lower=[user.lower() for user in current_users]
print(current_users_lower)