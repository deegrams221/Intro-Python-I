# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
#  To tell Python, that we want to use the global variable, we have to explicitly state this by using the keyword "global"
x = 12

def change_x():
    global x
    x = 99

change_x()

# This prints 12. What do we have to modify in changeX() to get it to print 99?
print(x)


# This nested function has a similar problem.
# Python3 introduced nonlocal variables as a new kind of variables. nonlocal variables have a lot in common with global variables. One difference to global variables lies in the fact that it is not possible to change variables from the module scope, i.e. variables which are not defined inside of a function, by using the nonlocal statement.
# if I were to use "global" here it would still retun 120.
def outer():
    y = 120

    def inner():
        nonlocal y
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999? Google "python nested function scope".
    print(y)

outer()