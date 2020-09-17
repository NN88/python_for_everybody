# Exercise 2: Given that fruit is a string, what does fruit[:] mean?

fruit = 'banana'
fruit[:]
# => 'banana'
# It means [start at the beg index of 0 : go until the end of the string]
# If you omit the first index (before the colon), the slice starts at the
# beginning of the string. If you omit the second index, the slice goes to
# the end of the string
