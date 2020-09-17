# Exercise 1: Write a function called chop that takes a list and modifies it,
# removing the first and last elements, and returns None.
# Then write a function called middle that takes a list and returns a new list
# that contains all but the first and last elements.


def chop(t):
    del t[0]
    del t[-1]
    return None

def middle(t):
    lyst = t[1:-1]
    return lyst

print('\n')
t = [1,2,3,4,5]
print("t is set: ", t)
chopp = chop(t)
print("chop function:", chopp)
print("t is now: ", t)

print('\n')
t = [1,2,3,4,5]
print("t is: ", t)
middle = middle(t)
print("middle function:", middle)
print("t is now: ", t)
