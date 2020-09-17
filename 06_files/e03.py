# Exercise 3: Sometimes when programmers get bored or want to have a bit of fun,
# they add a harmless Easter Egg to their program Modify the program that prompts
# the user for the file name so that it prints a funny message when the user
# types in the exact file name "na na boo boo". The program should behave
# normally for all other files which exist and don't exist. Here is a sample
# execution of the program:

try:
    inp = input("What is your file name?:") or "_files/mbox.txt"
    if inp == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd")
        exit()
    else:
      fhand = open(inp)
except Exception as e:
    print("Error is :", e)
    exit()

acc = 0
count = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence"):
        index = line.find(" ")
        number = float(line[19:].strip())
        acc = acc + number
        count = count + 1


average = acc / count
print("Average spam confidence", average)
