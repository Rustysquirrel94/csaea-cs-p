import math

# comment


print("The cow jumped over the moon!  ")
# Variable delareations and Data Types

a = 4    # integer
b = 5.5  # float
c = "CSAEA"   # String(s)
d = False # Boolean


print(a, b, c , d)

# Operators
# + - / *     %  **  ??
# += -= /=
# % this thingy called the modules or smthing gives you the remainder of numbers
e = 21 / 7

print(e)
e += 7
print (e)

#f-string formatted string for displaying variabes in quotes

print(f"e is equal to {e}")


e -= 5
e *= 7

print(f"e is currently equal to {e}")


#Comparisons (booleans, which always return True or False)

#  <    >   <=   >=    ==   !+
                            #  Means is not equal to


print (3 < 5)

print(7 == 4)

isEqual = (5 == 5)

print(isEqual)

IsYes = "Yes" 
print(IsYes)


# Logical operators
#  In order of precedence: not                      and                             or 
#                       Returns the     if its t and t then it returns t          if either side of truth table is true then it is true
#                       opporsite of     if t and f then it would be f                True overpowers false in this
#                                         f and f return f
#                                           False overpowers True 


f = (False) 
t = (True)



print(not f) #TRUe
print(f and t) #False
print (f or t) #True
print( f or t and not f)  #True


# Casting ()

# chops everything after the decimal point

g = int(10.97893287879892317873)
print(g)

# Strings

s1 = "Goodnight "
s2 = "and "
s3 = "goodbye"
end = s1 + s2 + s3 #concatenation with strings
print(end)

end += ", sleep well"
print(end)

# escaped characters
print(end + "\n")

#  Math library
print(math.sqrt(16))
print(math.ceil(3.65))
print(math.floor(3.65))
print(math.pow(3,4))

# Conditionals

#  if       elif      else

t = True 
f = False

if f:
   print("Reached the first condition")

elif f:
 print("reached second condition")

else:
   print("reached else")

h = True

if 1 > 1 and 1 == 1:
   print("Reached the first condition")

elif 6 == 7 or 3 != 3:
 print("reached second condition")
elif 10 != 10:
 print('Third condition')
else:
 print("reached else")



#  Lists
# A list can hold any type, and can grow or shrink at any time

# index: 0 1  2 3  4   5  6
nums = [3,89,32,43,84,38,92]
print(nums)
print(nums[2])
print(nums[-1])
# get 43 using negatives
print(nums[-4])
print(nums[0] + nums[2])
nums[1] = 289
print(nums)

#  List Methods
# Special Built in methods

words = []

words.append("The cow jumps")
words.append("over the")
words.append("moon")
print(words)
words.remove("The cow jumps")
words.insert(0, "!")
print(words)
words[2] = "the sun"
length = len(words)
print(words)
print(length)



# Iteration (LOOPS)

# For Loop
# a For loop will itterate over a range
#  a range is a range of numbers. 
# #range(stop), range(start,stop), range(start,stop,step) ex:range(1oo) will count all the way to 100   range(50,100) will start at 50    range(0,100,2)from 0 to 100 counting by two

for i in range(5):
  print(i)

  animals = ["Sheep", "Deer", "Mouse"]

  print(f"list:{animals}")

  for animal in animals:
       print(f"We saw a {animal}")

nums = [5.1, 2.2, 5.3, 3.4, 8.5]

# for n in nums:
#   print(n + 1)


for i in range(len(nums)):
  print(nums[i])

 # Debugging
print(len(nums))
print(range(5))

# for i in range(0,5):
#  print(nums[i])



#200!
#while loop

# iteratues while a condition is true 
# wjem tje condition becomes false, it stops
x = 5

while x < 10:
 print(x)
 x += 1

 t = True
 f = False
 while t or f:
   print("hi")