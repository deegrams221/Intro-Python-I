# For the exercise, look up the methods and functions that are available for use
# with Python lists.

# append(), insert(), extend(), sum(), count(), index(), min(), max(), sort(), reverse(), pop(), del(), remove(), 
# len(), copy(), clear(), any(), all(), ascii(), bool(), enumerate(), filter(), iter(), list(), map(), zip(), 
# slice(), reversed(), sorted()

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print('Solution 1:', x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)
print('Solution 2:', x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.pop(4)
print('Solution 3:', x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print('Solution 4:', x)

# Print the length of list x
# YOUR CODE HERE
print('Solution 5:', len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
print('Solution 6:', [i * 1000 for i in x])