# Exercise 5: This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from (i.e.,
#   the whole email address). At the end of the program, print out the
# contents of your dictionary.

# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}


try:
    fhand = open(input("Input file name: ") or "_files/mbox.txt")
except Exception as e:
    print("Error is: ", e)

counts = {}

for line in fhand:
    if line.startswith("From"):
        words = line.split()
        word = words[1]
        if "@" in word:
            split_email = word.split("@")
            domain = split_email[1]
            counts[domain] = counts.get(domain,0) + 1

print(counts)
