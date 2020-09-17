# Exercise 4: Assume that we execute the following assignment statements:

# width = 17
# height = 12.0
# For each of the following expressions, write the value of the expression and
# the type (of the value of the expression).

# width//2

# width/2.0

# height/3

# 1 + 2 * 5

# Use the Python interpreter to check your answers.


width = int(17)
height = float(12.0)

first_value = width/2
first_type = type(first_value)
print(first_value)
print(first_type)

second_value = width/2.0
second_type = type(second_value)
print(second_value)
print(second_type)

t_value = height/3
t_type = type(second_value)
print(t_value)
print(t_type)

f_value = 1 + 2 * 5
f_type = type(f_value)
print(f_value)
print(f_type)
