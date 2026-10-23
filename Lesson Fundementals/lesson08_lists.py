# LISTS IN PYTHON
# Lists store multiple values in one variable.
# They are ordered, mutable (changeable), and allow duplicates.

empty_list = []

# create lists
animals=["donkey","pangolin","blobfish"]
numbers = [2,4,6,8,10]
mixed = ["piffle",42,True,99.21]

print("Animals list:", animals)
print("Numbers list:", numbers)
print("Mixed data types list", mixed)

# print the third element in animals.
print(animals[2])
# print the last element in numbers
print(numbers[-1])
#print the first element in the mixed list
print(mixed[0])

animals[-1] = "babirusa"
print(animals)

#  add elements to end of a list
animals.append("glass frog")

print(animals)

# insert elament at specific index
animals.insert(2,"aye-aye")
print(animals)
animals.insert(1,"camel")
print(animals)
      
# remove elaments
animals.remove("aye-aye")
print(animals)

# remove (pop off) last element and save it into a variable
last_animal = animals.pop()

print(last_animal)
print(animals)

### **Challenge 1: Animal Swap**

# Store this list in a variable: [ 1, 2, 3, 4, 5, 6 ] 
# Ask the user to enter a new integer.
# Replace the **third integer** in the original list with the user’s input, and then print the updated list.
# *Hint: use indexing and assignment.*

list_ch1 = [ 1, 2, 3, 4, 5, 6 ] 
user_choice = int(input("enter integer"))
list_ch1.insert(2,user_choice)
list_ch1.pop
print(list_ch1)

### **Challenge 2: Shopping List Manager**

# Initialize an empty list called `shopping`.
# Add three items of your choice using `.append()`.
# Then insert one extra item at the second position and remove one item of your choice.
# Finally, print the final shopping list.

shopping = []
shopping.append("eggs")
shopping.append("milk")
shopping.append("cheese")
shopping.insert(2,"Crackers")

shopping.remove("cheese")
print(shopping)

nums = [3, 7, 1, 9, 4, 2, 5, 8, 6, 0]
print("Numbers:", nums)

print("Length of list:", len(nums))
print("Min:", min(nums))
print("Max:", max(nums))
print("Sum:", sum(nums))

nums.sort()
print(nums)

animals.sort()
print(animals)
nums.reverse()

if "cat" in animals:
    print("Cat is in the list")
else:
    print("Cat is not in the list")

### Challenge 3: Number Stats

# Create a list of five floats called measurements.
# Print the length, minimum, maximum, and sum of the list using built-in functions.

measurements = [2.5,3.9,6.7,9.0,2.3]
print("Length:", len(measurements))
print("Max:", max(measurements))
print("Sum:", sum(measurements))
