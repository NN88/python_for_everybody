# Exercise 6:
# Read the documentation of the string methods at
# https://docs.python.org/3.5/library/stdtypes.html#string-methods
# You might want to experiment with some of them to make sure you understand how
# they work. strip and replace are particularly useful.
# The documentation uses a syntax that might be confusing. For example,
# in find(sub[, start[, end]]), the brackets indicate optional arguments.
# So sub is required, but start is optional, and if you include start, then end
# is optional.

# lstrip()
before = "           You should probably lstrip() this"
print("Before: ", before)
after = before.lstrip()
print("After: ", after)

# rstrip()
before = "You should probably rstrip() this         "
print("Before: ", before)
after = before.rstrip()
print("After: ", after)

# replace()
before = "This language is ruby but another good language is ruby"
print("Before: ", before)
after = before.replace("ruby", "python", 1) # only replace the 1st occurence
print("After: ", after)
