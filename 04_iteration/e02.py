# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead
# of the average.

try:
    arr = []
    while True:
        num = input("Enter a number: ")
        if num != 'Done' and int(num):
            print(num)
            arr.append(int(num))
            continue
        if num == "Done":
            smallest = min(arr)
            largest = max(arr)
            print("Smallest: ", smallest)
            print("Largest: ", largest)
            break
except Exception as e:
    print("Error is: ", e)
