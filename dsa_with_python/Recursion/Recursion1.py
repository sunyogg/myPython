# RECURSION -> Calling method inside it's own body.

# Very basic infinite recursion because we don't have base condition

def greet():
    print("Hello")
    greet()


def print_num(n):
    if (n == 5): # base condition
        return
    print(n) # body
    print_num(n + 1) # recursive call
