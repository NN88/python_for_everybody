# Exercise 1: Revise a previous program as follows: Read and parse the "From"
# lines and pull out the addresses from the line. Count the number of messages
# from each person using a dictionary.

# After all the data has been read, print the person with the most commits by
# creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person
# who has the most commits.

# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195

#### PERSONAL NOTES
# Tuples are confusing to me so remember this:
# Tuples are immutable, comma seperated values, hashable, () , like csv
# Lists are mutable, [], list arrays
# Dictionaries are mutable, key=>value, {}, like assoc. arrayst


try:
    fhand = open(input("Input file name: ") or "_files/mbox.txt")
except Exception as e:
    print("Error is: ", e)

counts = {}
for line in fhand:
    if line.startswith("From"):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email,0) + 1

lst = []
for k,v in counts.items():
    lst.append((v,k))

lst.sort(reverse=True)
most_commit_email = str(lst[0][1])
most_commit_count = str(lst[0][0])
print(most_commit_email, most_commit_count)
