# Exercise 1: Write a simple program to simulate the operation of the grep
# command on Unix. Ask the user to enter a regular expression and count
# the number of lines that matched the regular expression:

# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author

# $ python grep.py
# Enter a regular expression: ^X-
# mbox.txt had 14368 lines that matched ^X-

# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4218 lines that matched java$

import re

counts = 0
try:
    reg_ex = input("Enter a regular expressions: ")
    fhand = open("_files/mbox.txt")
    for line in fhand:
        line = line.rstrip()
        if re.findall(reg_ex, line):
            counts = counts + 1

    print(counts)

except Exception as e:
    print("Error is: ", e)



