# Exercise 2: Write a program to prompt for a file name, and then read through
# the file and look for lines of the form:

# X-DSPAM-Confidence:0.8475

# When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart
# the line to extract the floating-point number on the line. Count these lines
# and then compute the total of the spam confidence values from these lines.
# When you reach the end of the file, print out the average spam confidence.

# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745

# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519


try:
  fhand = open(input("What is your file name?:") or "_files/mbox.txt")
except Exception as e:
  print("Error is :", e)
  exit()

acc = 0
count = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence"):
        index = line.find(" ")
        number = float(line[19:].strip())
        acc = acc + number
        count = count + 1

average = acc / count
print("Average spam confidence", average)
