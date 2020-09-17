# Exercise 2: Rewrite your pay program using try and except so that your program
# handles non-numeric input gracefully by
# printing a message and exiting the program.

try:
    hours = int(input('Enter Hours:'))
    rate = int(input('Enter Rate:'))
    if(hours > 40):
        overtime_hours = hours - 40
        overtime_rate = rate + (rate/2)
        overtime_pay = int(overtime_hours) * int(overtime_rate)

    regular_hours = 40
    regular_rate = rate
    regular_pay = int(regular_hours) * int(regular_rate)

    pay = regular_pay + overtime_pay
    print("Pay:" + str(pay))

except:
  print('Error, please enter numeric input')
