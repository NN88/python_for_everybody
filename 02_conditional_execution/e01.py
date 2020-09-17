# Exercise 1: Rewrite your pay computation to give the employee 1.5 times
# the hourly rate for hours worked above 40 hours.

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
