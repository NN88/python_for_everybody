# Exercise 3: Write a program that reads a file and prints the letters in
# decreasing order of frequency. Your program should convert all the input
# to lower case and only count the letters a-z. Your program should not
# count spaces, digits, punctuation, or anything other than the letters a-z.
# Find text samples from several different languages and see how letter
# frequency varies between languages. Compare your results with the tables
# at wikipedia.org/wiki/Letter_frequencies.


import string

try:
    fhand = open(input("Input file name: ") or "_files/mbox.txt")
except Exception as e:
    print("Error is: ", e)

counts = {}
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.whitespace))
    line = line.lower()
    for letter in line:
        counts[letter] = counts.get(letter, 0) + 1

print(counts)
