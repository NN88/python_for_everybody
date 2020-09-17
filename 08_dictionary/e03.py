# Exercise 3: Write a program to read through a mail log, build a histogram using
# a dictionary to count how many messages have come from each email address, and
# print the dictionary.

# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

try:
    fhand = open(input("Input file name: ") or "_files/mbox.txt")
except Exception as e:
    print("Error is: ", e)

counts = dict()
for line in fhand:
    if line.startswith("From"):
        words = line.split()
        if len(words) > 1:
            word = words[1]
            counts[word] = counts.get(word,0) + 1

print(counts)
