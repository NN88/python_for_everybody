# Exercise 3: Encapsulate this code in a function named count, and generalize
# it so that it accepts the string and the letter as arguments.

# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

def count(string, target):
    word = str(string)
    target = str(target)
    count = 0
    for letter in word:
        if letter == target:
            count = count + 1
    print(count)

# notice we can do parameter assignment out of order
count(target="a", string="banana")
