# Exercise 5: Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and print out the converted temperature.

# (0°C × 9/5) + 32 = 32°F
# (27.5°C × 9/5) + 32 = 81.5°F

celsius = input("Enter Celsius: ")

try:
    fahrenheit = ((float(celsius) * 9/5) + 32)
    print("Fahrenheit is: " + str(fahrenheit))
except:
    print('Please enter a number')
