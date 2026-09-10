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
print(math.pow(3, 4))