# Exercise 1: Write a program that reads the words in words.txt and stores
# them as keys in a dictionary. It doesn't matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in
# the dictionary.

try:
    fhand = open(input("Input file name: ") or "_files/words.txt")
except Exception as e:
    print("Error is: ", e)

count = 0
dic = dict()
for line in fhand:
    words = line.split()
    for word in words:
        count += 1
        if word in dic:
            continue
        dic[word] = count

if 'Python' in dic:
    print('Python EXISTS!')
else:
    print('NOPE!')
