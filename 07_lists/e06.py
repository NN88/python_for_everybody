# Exercise 6: Rewrite the program that prompts the user for a list of numbers
# and prints out the maximum and minimum of the numbers at the end when the
# user enters "done". Write the program to store the numbers the user enters
# in a list and use the max() and min() functions to compute the maximum and
# minimum numbers after the loop completes.

lyst = []
try:
    while True:
        inp = input("Enter a number: ")
        if inp != 'done':
            lyst.append(float(inp))
            continue
        else:
            break

except Exception as e:
    print("Error is: ", e)
    exit()


if len(lyst) > 0:
    maximum = max(lyst)
    minimum = min(lyst)
    print("Maximum: ", maximum)
    print("Minimum: ", minimum)
