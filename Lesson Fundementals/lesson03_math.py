#KEY CONCEPTS: math operators: +, -, *, /, //, %, **

add = 7 + 2
print("Sum:",add)
subtract = 9 - 7
print("differnce:",subtract)

multiply = 7 * 2
print("Product:",multiply)

float_divide = 7 / 2
print("Float Division:", float_divide)

integer_divide = 7 // 2
print("integer division:",integer_divide)

modulus_mod = 7 % 2
print("modules:",modulus_mod) 

exponent = 7 ** 2
print("Exponent:",exponent)


#PEMDAS (parentheses, exponents, multiplication/division, addition/subtraction)

result1 = (2 + 3) * 4
print("Result 1:",result1)

result2 = 2 ** 3 * 4
print("Result 2:",result2)

result3 = 5+2**3 *(4-1)
print("Result 3:",result3)

# Challenge 1: Rectangle Area  
# Calculate the area of a rectangle with a width of 8 and a height of 5. 
width = 8
height = 5
area = width * height
print(area)

# Challenge 2: Circle Area  
# Use the formula πr² to calculate the area of a circle with radius 7. (Use 3.14 for π.)  
r = 7 **2
π = 3.14
area = 7**2 * π
print("Area:",area)

# Challenge 3: Shopping Total  
# A book costs $12.99 and a notebook costs $3.50.  
# Calculate the total cost for 3 books and 4 notebooks. 
book = 12.99
notbook = 3.50
aon = 3
aob = 4
b_aob = book *aob
nb_aon = notbook * aon
total = nb_aon + b_aob
print(f"\tBook:${b_aob}\n\tNotebook:${nb_aon}\n\tTotal:${total}")

# Challenge 4: Even or Odd  
# Use the modulus operator to check if the number 57 is even or odd.  
num = 57
rem = num % 2
if rem > 0:
    print(f"\n\tThe number {num} is Odd")
elif rem == 0:

    print(f"\n\tThe number {num} is Even")