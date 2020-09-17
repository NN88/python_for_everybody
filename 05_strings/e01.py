# Exercise 1: Write a while loop that starts at the last character in the string
# and works its way backwards to the first character in the string, printing each
# letter on a separate line, except backwards.

saying = "Some really long ass string"
index = 0
while index >= -len(saying):
    letter = saying[index]
    print(letter)
    index = index - 1

