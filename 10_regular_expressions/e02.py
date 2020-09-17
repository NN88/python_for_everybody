# Exercise 2: Write a program to look for lines of the form

# `New Revision: 39772`
# and extract the number from each of the lines using a regular expression and
# the findall() method. Compute the average of the numbers and print out
# the average.

# Enter file:mbox.txt
# 38549.7949721

# Enter file:mbox-short.txt
# 39756.9259259

import re
summ = []

try:
    fhand = open(input("Input file name: ") or "_files/mbox-short.txt")
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    exit()


for line in fhand:
      line = line.rstrip()
      match = re.findall('^New Revision: ([0-9.]+)', line)
      if len(match) > 0:
          for val in match:
              val = float(val)
              summ = summ + [val]


total_sum = sum(summ)
count = float(len(summ))
average = total_sum / count
print(average)
