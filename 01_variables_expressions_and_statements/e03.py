# Exercise 3: Write a program to prompt the user for hours and rate per hour
# to compute gross pay.

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
gross = float(hours) * float(rate)
pay = str(gross)
print('Pay: ' + pay)
