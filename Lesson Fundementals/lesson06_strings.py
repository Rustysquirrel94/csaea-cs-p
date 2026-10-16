# STRING MANIPULATION IN PYTHON
# built-in methods: len(), upper(), lower(), capitalize()

# String formattin,string concatination


greeting = "Hello"

first_name = "Ada"
last_name = "Lovelace"
# Option 1
print("Hello",first_name, last_name,"!")
# concatination
print("Hello" + " " + first_name + " " + last_name + "!")
# F string
print(f"Hello{first_name} {last_name}!")

# 0 1 2 3 4 
# H e l l o
greeting = "Hello"
second_letter = greeting[1]
print(second_letter)

#  String indexing and slicing 
word = "Super-calif-ragil-istic-expi-ali-docious"
print("\nThe word is: ",word)
print("First letter is :", word[0])
print("The last letter is:",word[-1])
print("Range of letters (non-inclusive)", word[3:7])
# will start at and display index 3 but wont include index 7
print("First five letters",word[:5])
print("everything after first 5 " ,word[5:])
print("LAst seven ",word[-7:])
print("Step through every second character",word[::2])
print("string in reverse",word[::-1])

last_name = "    Lovelace"
length = (len(last_name))
print("Length of string is ", length)

# Challenge 1: Favorite Quote
# Ask the user for their favorite quote and display its length.
# EXAMPLE OUTPUT:
# Enter your favorite quote: Those who believe in telekinetics, raise my hand.
# Your quote is 48 characters long.

quote = input("What is your favorite quote:")
print(f"Your Favorite quote is {len(quote)} characters long.")


# Challenge 2:
# Ask the user to enter a word that is at least 7 characters long. 
# Print the 2nd through 6th characters.
# Use string slicing.
user = input("Please intput a word that is at least 7 characters long:")
print("The characters of 2-6 of your word is ",user[1:6] )

# Challenge 3: Name Formatter
# Ask the user for their first and last name, then format it as "Last, First".
# Use concatenation or f-strings.
# Example output:
# Enter your first name: Ada
# Enter your last name: Lovelace
# Formatted name: Lovelace, Ada



user_first = input("Enter first name:")
user_second = input("Enter Last name:")
print(f"{user_second}, {user_first}")





charcter = "MonKeY GuY"
print("\nLowercase:", charcter.lower())
print("\nUpppercase:", charcter.upper())
print("\nCap first letter:", charcter.capitalize())
print("\nTitle format:", charcter.title())

print()

# FInd and replace test
sentence = "the cow did a backflip over the moon"
new_sentence = sentence.replace("backflip","frontflip")
print(sentence,new_sentence)

#Join and split
groceries ="milk,eggs,bread,butter,peanut"
print("\nOriginal string:",groceries)

# split the string into a python list based on a "delimiter"
items = groceries.split(",")
print(items)

# Join a list back together into a string
joined = " and ".join(items)
print(joined)
print(type(items))
print(type(joined))


# Challenge 3: Word Mutation
# Ask for a word and print it backwards, in uppercase, and lowercase.
# Example output
# Enter a word: Python
# Uppercase: PYTHON
# Lowercase: python
# Backwards: nohtyP

word = input("Enter word:")
print("Uppercase:",word.upper())
print("Lowercase:",word.lower())
print("Backwards:",word[::-1])
