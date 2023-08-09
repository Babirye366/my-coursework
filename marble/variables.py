# Assigning variables 
name = "Nakaye Marble"
food = "peas"
is_female = True
height_cm = 140

# Output variable values
print("Name:", name)
print("Likes:", food)
print("Is Female:", is_female)
print("Height (in cm):", height_cm)

# reassigning variables
height_m = height_cm / 100

# Updated variable values
print("Height (in meters):", height_m)

# swapping variables
a = 100
b = 400
print("\nBefore swapping: a =", a, "b =", b)
a, b = b, a
print("After swapping: a =", a, "b =", b)

# concatenating variables
eat = "peas"
at = " Olives"
message = eat + " at " + at + " "
print("\nMessage:", message)

# Variable interpolation
price = 30000
quantity = 15
total = price * quantity
print("Total:", total)

# Variable scope
def my_function():
    local_var = "Is an example of a local variable"
    print("\nHere:", local_var)

my_function()

