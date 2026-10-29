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
    for n in range(times):
     num *= 2  
     doubler_list.append(num)
    return doubler_list
      
    
    

answer = doubler(2,3)
print(answer)