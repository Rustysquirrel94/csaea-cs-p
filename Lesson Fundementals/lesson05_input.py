# USER INPUT IN PYTHON
# print ("<PROMPT>")

name = input("Whats your name: ")
print(f"Hello {name}")
print(type(name))
age = input("Enter your age:")
print(f"Your age is:{age}")

print(type(age))

age_converted = int(age)
print(type(age_converted))

height = float(input("Whats your height:"))
print(f"You are {height} feet tall")
print(type(height))
print(height + 1)


# Challenge 1: Favorite Color
# Ask the user for their favorite color and print out a message using it.
fav_color = input("What is your favorite color:")
print(f"{fav_color} a really nice color")
# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

print(f"Them added is {num1 + num2}")

# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.
# pi radius squared 
import math
dia = int(input("What is the diameter: "))
rad = dia/2
pi = math.pi
area = int(math.pow((pi * rad),2))
print(f"the area is {area}")


# Challenge 4: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.
import random
typeofdi = int(input("How many sides does the die have: "))
roll =random.randint(1, typeofdi)
print(f"You rolled a {roll}!")
