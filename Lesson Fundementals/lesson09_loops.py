# Loops\iteration\ TO iterate
# LOOPS IN PYTHON
# Loops repeat a block of code until they hit a limit or condition.
# They exist to save us from typing the same line 500 times.
# Python gives us for-loops and while-loops.

import time
# The FOR-LOOP.
# A for-loop repeats for each element in a sequence (like a list or string).
# usually with lists

animals = ["lamb","dog","Beaver","penguin","goose"]
print(animals)
# ok so the for _____ is a variable and its like creating a new variable to use in just that loop for ex
for i in animals:
    print(f"I like  the animal {i}")

for animal in animals:
    print("Now im petting a",animal)


for a in animals:
    print("Now I'm petting a", a)
    time.sleep(0.1)
# time.sleep makes it so that whatever the out put it will be delayed by (_)seconds

# We can loop a specific number of times using range().

for i in range(5):
    print("Counting",i)
    time.sleep (0.3)

 # range(start, stop, step)




#             start, stop, counting by
 #  for num in range(2,11,2) 
 
 
for num in range(5, 105, 5):
    print(num)
    

#
 # Strings are also iterable, so they can be looped as well!

fav_word = "Shennanigans"

letter_list = []

for letter in fav_word:
    print(letter)
    letter_list.append(letter+"!")
print(letter_list)

# Challenge 1: Sum Calculator
# Use a for-loop to find the sum of numbers from 1 to 10.
# ie, 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# Expected output: 55
print()
total = 0
for n in range(1,11):
    total += n
    print(total)

# print()
# total = 0
# for i in range(1,11):
#     total = total + i

# print(total)
#______________________________________________________
# A while-loop repeats *while* a condition is true.
# If you forget to change the condition, it loops forever.
# And then your program becomes immortal. Avoid that.

# += to add to a variable, -= to subtract to a variable, = to overright 

count = 0

while count < 5:
    print((f"Looping: We are on index {count}"))
    count += 1 
    time.sleep(0.5)

    # Example with user input 

# user_input = ""
# while user_input != "exit":
#     user_input = input("type exit to escape:").lower


# Loop Control Statements

for i in range(1,11):
    
      if i == 3:
          print("skipping num 3")  
          continue # skips this interation
      if i == 6:
          print("Breaking at 6")
          break # stop the loop entirely
      if i == 9:
          pass # place holder,does nothing, will code in future

      
print("Number", i)
    


# Challenge 2: Guess Until Correct
# Create a while-loop that keeps asking for a number until the user types 7.
user_guess = ""
while user_guess != "7":
    user_guess = (input(" Please guess a number: "))
    print("wrong")
print("Correct!")
   

#         user_input = ""
# while user_input != "exit":
#     user_input = input("Type 'exit' to escape")


for i in range(10, 0, -3):
    print(i)

for i in range(3):
    if i == 5:
        break
    else:
        print("done")


total = 0
n = 1
while total < 20:
    total = total + n
    n += 2

print(total, n)

count = 0
for letter in "pineapple":
    if letter in "aeiou":
        count += 1
        print(count)


n = 10
while n >= 0:
    n -= 3 
print("Escaped!")

# Challenge 5: Write a guessing game with 5 tries and hints.
# The computer picks a secret number from 1 to 20. The player gets 5 guesses.
# The player will receive HINTS if they have an incorrect guess.
#
# preconditions: 
# the random library; 
# a random integer stored as the 'secret' that the player must guess.
#
# Pseudocode:
#   repeat 5 times (use a for-loop with range):
#       ask the player for a guess (convert it to an int!)
#       if guess equals secret → print "Got it!" and stop the loop
#       otherwise, if guess is bigger → print "Too high"
#       otherwise → print "Too low"
#   if the loop never stopped early → print "Out of guesses! It was" + secret

import random
secret = random.randint(1, 20)

for p in range(5):
    guess = int(input("Write your guess:"))
    if guess == secret:
        print("You got it Joe!")
    elif guess > secret:
        print("To High!")
    elif guess < secret:
        print("To Low!")
    else:
        print("Wrong")