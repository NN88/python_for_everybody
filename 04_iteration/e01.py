# Exercise 1: Write a program which repeatedly reads numbers until the user
# enters "done". Once "done" is entered, print out the total, count, and average
# of the numbers. If the user enters anything other than a number, detect their
# mistake using try and except and print an error message and skip to the next
# number.

try:
    arr = []
    while True:
        num = input("Enter a number: ")
        if num != 'Done' and int(num):
            print(num)
            arr.append(num)
            continue
        if num == "Done":
            total = 0
            count = 0
            for i in arr:
                count = count + 1
                total = int(total) + int(i)

            count = int(count)
            total = int(total)
            average = total / count
            average = float(average)

            print("Count: ", count)
            print("Total: ", total)
            print("Average: ", average)
            break

except:
    print("Invalid input")
