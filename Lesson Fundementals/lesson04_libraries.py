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


seed = 111.93
step2 = (math.sqrt(seed))
step3 = (step2 ** 8)
step4 = (step3 / 1100)
# seed5 = (seed + seed2 + seed3 + seed4) /320 
final = math.ceil(step4)
print(f"Your random number is {final % 10}")

for z in range(5):
    print("Hi")
# example
for n in range(5):
    calcs = seed + 2234 * 22 / 3
    randint = math.ceil(calcs)
    print(f"Simple random num gen: {randint % 10}")
    seed += 1

    # Pythons random library

    import random
    
    random_integer = random.randint(1,100)
    print(random_integer)

    random_float = random.random()
print(random_float)

my_list = ["taco", "burrito", "enchilada", "quesadilla"]

random_selection = random.choice(my_list)
print(random_selection)

random.shuffle(my_list)
print(my_list)

# Challenge 2: Simulate a Die Roll
# Use the random library to simulate rolling a six-sided die.
# The output should be a random integer between 1 and 6.
# Store the result in a variable called "die_roll" and print it with a message.

dice = ["1","2","3","4","5","6"]
die_roll = random.choice(dice)
print(f"You rolled a {die_roll}!")

# Challenge 3: Random Square Root
# Use random library to pick a number between 1 and 75. Store it in "num".
# Use math library to find its square root.
# Print the number, its square root, and the square root rounded UP with math.ceil().

num = random.randint(1,75)
sqnum = math.sqrt(num)
rounded_sqnum = math.ceil(sqnum)
print(num)
print(sqnum)
print(rounded_sqnum)


# Challenge 4: Power Roll
# Roll two dice with the random library: one is the "base," one is the "exponent."
# Use math library to raise the base to the exponent. (ie, base to the POWer of exponent)
# Print both rolls and the result as an integer (hint: int() removes the .0).

base_di = random.randint(1,6)
expo_di = random.randint(1,6)
final_di = int(math.pow(base_di, expo_di))

print(f"base die is {base_di}")
print(f"exponent die is {expo_di}")
print(f"final die is {final_di}")