# Exercise 4: Add code to the above program to figure out who has the most
# messages in the file.

# After all the data has been read and the dictionary has been created, look
# through the dictionary using a maximum loop (see Section [maximumloop]) to
# find who has the most messages and print how many messages the person has.

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195


try:
    fhand = open(input("Input file name: ") or "_files/mbox.txt")
except Exception as e:
    print("Error is: ", e)

counts = dict()
largest = -1

for line in fhand:
    if line.startswith("From"):
        words = line.split()
        word = words[1]
        counts[word] = counts.get(word,0) + 1

for k,v in counts.items():
    if v > largest:
        largest = v
        title = k

print(title, largest)

