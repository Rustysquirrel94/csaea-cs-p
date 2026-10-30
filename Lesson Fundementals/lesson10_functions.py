# Python functions are simply blocks of code that can be reused. 
# To run a function, you *call* the function by writing its name, followed by parenthesis, and any arguments that it needs.

# https://www.w3schools.com/python/python_functions.asp# Python functions are simply blocks of code that can be reused. 
# To run a function, you *call* the function by writing its name, followed by parenthesis, and any arguments that it needs.

#  https://www.w3schools.com/python/python_functions.asp

def say_hi():
    print("Hi")

def say_bye():
    print("Bye")

say_hi() #calling a function
say_bye()
say_hi()
say_bye()

# Functions more commonly RETURN values, not merely print
# We can pass an ARGUMENT into a function's PARAMETER# We can pass an ARGUMENT into a function's PARAMETER

def express_this(e):# e is called a PARAMETER, which is a placeholder for an ARGUMENT     
    return


expression = express_this(1+2)# the mathmatical expression here is the ARGUMENT, the actual value that will be used by a functions PARAMETER

print(expression)

def greeter(name):
    return f"Hi {name}"

first = greeter("Jojo")
second = greeter("Bizbo")
third = greeter("Hoppy")
print(first,second,third)
#                               WRITING RETURN IS LIKE WRITING PRINT!
def remainder(a,b):
    return a % b
result = remainder (10,9)
print(remainder(10,3))
print(result)
def is_far(distance):
    if distance >= 100:
        return "That's far"
    if distance < 100 and distance > 20:
        return "That's not too far"
    if distance < 20:
        return "Hey that's pretty close by!"

# call is_far() on four differnt distances then print
uno = is_far(150)
dos =is_far(34)
tres=is_far(10000)
cuatro=is_far(0.32123123148129495)

print(f"\n{uno}\n{dos}\n{tres}\n{cuatro}")

# I want to create a function that takes in a number and doubles it, then adds it to a list.
# The function should also take in a number of times that we should double the number
# Write a function named doubler(num,times) that has TWO parameters: 
# First parameter:  the number i want doubled
# Second paramater: how many times the loop should run 
#Example output:
# doubler(1, 5)
# result should be [2, 4, 8, 16, ]

def doubler(num,times):
    doubler_list = []
    number = num
   
    for n in range(times):
     number *= 2  
     doubler_list.append(number)
    return doubler_list
      

answer = doubler(2,5)
print(answer)

# For Challenges 1 - 3, first write pseudocode, then solve in code.
 
# Challenge 1. 
# Make a calculator with 4 procedures that accept two arguments each. 
# 1) add any two numbers and print the result
# 2) subtract any two numbers and print the result
# 3) divide any two numbers and print the result
# 4) multiply any two numbers and print the result 

def adder(a,b):
   print(a + b)
   return a+b

adder(1,2)

def subtracter(a,b):
   print(a - b)
   return a-b


def multiplyer(a,b):
   print(a * b)
   return a*b


def divider(a,b):
   print(a / b)
   return a/b

divider(8,2)

def average(a,b,c,d,e):
   add_it_up=a+b+c+d+e
   add_it_up/=5
   print(add_it_up)
   return (add_it_up)

average(1,28,4,16,92)

def evenorodd(a):
    if a % 2 ==0:
        print("Even")
        return("Even")
    else:
        print("Odd")
        return("Odd")
               
               
               
evenorodd(8347)

# Challenge 4
# Use the pseudocode below to write code:
# Make a function called "analyze_word" that counts how many vowels and consonants are in a word
# Tools: uses a for loop, IF/THEN statement, "aeiou".

# The function analyze_word accepts one argument, a single word (string):
# Initialize two variables:
# vowelCount set to 0
# consonantCount set to 0
# Use a loop to iterate through each character in the word.
# Inside the loop, use an IF/ELSE statement:
# If the character is a vowel (a, e, i, o, u), increment vowelCount.
# Otherwise, increment consonantCount.
# After the loop ends: 
# 	return a string that states how many vowels and how many consonants are in the word.

# Call the function with a sample one-word string and print the returned result outside the function

def analyze_word(word):
    list(word)
    vowel ="aeiou"
    vowel_count =(0)
    consonant = "qwrtypsdfghjklzxcvbnm"
    consonant_count =(0)

    for vowel in word:
        if vowel in word:
            vowel_count += 1
        print(vowel_count)
        return vowel_count

       
    for consonant in word:
        if consonant in word:
            consonant_count += 1
        print(vowel_count)
        return vowel_count
    
    print(f"There are {vowel_count} vowels and {consonant_count} in the word {word}")

    

        
analyze_word("house")