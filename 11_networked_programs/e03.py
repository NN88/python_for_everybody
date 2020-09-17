# Exercise 3:
# Use urllib to replicate the previous exercise of (1) retrieving the
# document from a URL, (2) displaying up to 3000 characters, and (3) counting
# the overall number of characters in the document. Don't worry about the
# headers for this exercise, simply show the first 3000 characters of the
# document contents.

import urllib.request, urllib.parse, urllib.error

try:
    # inputs
    fhand = urllib.request.urlopen(input("URL: ") or 'http://data.pr4e.org/romeo.txt')

    characters = 0
    for line in fhand:
        words = line.decode().split()
        characters = characters + len(words)
        if characters < 3000:
            print(line.decode().strip())
    print(characters)

except Exception as e:
    print(e)

finally:
    exit();
