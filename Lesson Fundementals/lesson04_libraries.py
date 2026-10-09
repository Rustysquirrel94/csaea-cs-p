# Doc on libraries: https://docs.python.org/3/library/index.html
# Doc on Math library: https://docs.python.org/3/library/math.html

import math

sq_root = math.sqrt(49)
print("The square root is", sq_root)

round_up = math.ceil(4.5)
print("Round up: ", round_up)

round_down = math.floor(4.8)
print(f"Rounded down:   {round_down}")

exponent = math.pow(2,5)
print(exponent)

#Constant : a variable that never changes 
# When constant variable you capitilize everything

PI = math.pi
print(PI)

# Challenge 1: Circle Area with Math Library
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14. 
# Formulas: the area of a circle is πr² -- the radius is diameter / 2


diameter = 14
radius = (diameter / 2)
circle_area = math.pow((PI * radius),2)
print(f"The circle area is: {circle_area}")


# Phython Random Library 


# Pseudorandom Number Generator


# Create your own pseudorandom number generator that utilizes as seed to output a random number. 
# The seed should be a floating-point number with five total digits (including those before and after the decimal), and it must be greater than 100.0. 
# Perform at least 3 different math calculations on it (ie, addition, subtraction, and division). 
# Use math library to round the float UP to an integer. 
# BONUS CHALLENGE: Make your random number output between 1 and 10. 

seed = 101.91
seed2 = (math.sqrt(seed))
seed3 = (seed2 ** 8)
seed4 = (seed3 / 1100)
# seed5 = (seed + seed2 + seed3 + seed4) /320 
final = math.ceil(seed4)
print(f"Your random number is {final}")
