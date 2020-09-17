# Exercise 7: Rewrite the grade program from the previous chapter using a function
# called computegrade that takes a score as its parameter and returns a grade
# as a string.

score = float(input('Enter Score between 0.0 and 1.0: '))

if score > 1.0:
    print("Error: Bad Score")
    exit()

def computegrade(score):
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    elif score < 0.6:
        print('F')

computegrade(score)
