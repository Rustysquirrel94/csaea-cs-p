import math
# 1
b = 50 
b *= 0.20
(f"The bill is {b}")

print((f"The tip is {b}"))

b += 50
print(f"The total is {b}")

# 5
password = "csaea2026"
attempt = "csaeA2026"

csaea2026 = True
password == True

if attempt == password:
 print("Acess Granted")
else:
    print("Acess Denied")

#  8
first = "Ada"
last = "Lovelace"
school = "CSAEA"
 

print(f"Hello my name is {first} {last} and from {school}")

# 10
groceries = ["milk", "eggs", "bread"]
 
groceries.append("Rice, Cheese")
print(groceries)
length = len(groceries)
print(length)

# 11
start = 10
 
while start > 0:
    print(start)
    start -= 1  
if start == 0: 
    print("liftoff")

# 9
cart = [12, 5, 30, 8]


print(f"The total is {sum(cart)}")
print(f"The number of items in the cart is {len(cart)}")

# 7
h = 50
a = 11
has_adult = True
 
if h >= 48 and a >= 10:
     print("You may Ride")   
elif has_adult == True:
     print("You May Ride with an adult")
else:    
    print("You May Not Ride")

# 3
F = 212
C = (F - 32) * 5 / 9
print(f"{F} farrenhieght is {(F - 32) * 5 / 9} degrees celcius")

# 2
s = 23
sps = 2
spp = 8


nop = (math.ceil(s * sps / spp ))
nor = ((nop * spp) - (s * sps))
print(f" The amount of pizzas is {nop} and the remainer is {nor}")

# 13
savings = 0
weekly_deposit = 15
goal = 100
W = 0
while savings < goal: 
   savings += weekly_deposit 
   W += 1



print(f"{W} Weeks")
print(f"{savings} in savings")
    

