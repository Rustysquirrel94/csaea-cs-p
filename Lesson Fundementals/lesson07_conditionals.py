# CONDITIONALS IN PYTHON
# comparison operators: ==, !=, <, >, <=, >=
# logical operators: and, or, not
# control flow: if, elif, else

# Boolean:
# always return either True or False
print(3 == 2)
print("Hello" == "Hi there")
print(7 != 4)
print(4 > 5)

# if 
num = 10
if num == 10:# only runs if condition is true 
    print("Your number is equal to 10")
    print(10+num)

# if else
num = 5
if num <= 12:
    print("Your num is less than or equal to 12")
else:
    print("Your num is greater than 12")

# if else elif
temperature = 72 
if temperature > 95:
    print("It is hot out!")
elif temperature >= 60:
    print("its nice out")
else:
    print("its cold")


print()

x = 2
y = 20

if x == y:
    print("they are equal!")
elif x>=y:
    print("x is greater than y")
else:
    print("y is greater than x")

# Logical operators:and 
# Both sides of the 'and' must  be true, otherwise it's false. 
age=16
has_permission= True

if age >= 16 and has_permission:
    print("You can drive")
else:
    print("you cant drive")

#Logical operators: 'or' and 'not'

day = "Saturday"

if day =="Saturday" or day == "sunday ":
    print("weekend")
else:
    print('weekday')

    print("--- Using 'is' and 'not' --- ")
#       !=
if day is not "Monday":
    print(" No moonday yay :)")



    
# Challenge 1: Movie Admission
# Ask the user for their age. 
# If under 13, “You can watch PG or G movies.”
# If 13–17, “You can watch PG-13 movies.”
# If 18+, “You can watch any movie.”
# Example output:
# Enter your age: 15
# You can watch PG-13 movies.
age = int(input("Enter your age:"))
if age <= 13:
    print("You can watch PG or G movies")
elif age >= 13 and age <= 17:
    print("You can watch PG-13 Movies")
else:
    print("You can watch any movie")

# Challenge 2: Leap Year
#   - Years divisible by 4 are leap years...
#   - ...unless they're divisible by 100, then they're NOT leap years...
#   - ...unless they're also divisible by 400, then they ARE leap years.
# Example output:
# Enter a year: 1900
# 1900 is not a leap year.
# (Test: 2024 -> leap, 1900 -> not, 2000 -> leap)

year = int(input("Enter Year:"))
if year % 4 ==0 and (year % 100):
    print(f"{year} is a leap year!")
elif year % 400 == 0:
    print(f"{year} is a leap year!")
else: 
    print("not a leap year")
    
    