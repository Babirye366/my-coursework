# Creating a set of food
food_set = {"beans", "peas", "chicken", "fries"}

# Length of the set
print("Length of the food set:", len(food_set))

# Data type of the set
print("Data type of the food set:", type(food_set))

# Accessing elements in the set
for item in food_set:
    print("Food item:", item)

# Adding items to the set
food_set.add("banana")
food_set.add("cereal")
print("Updated food set:", food_set)

# Creating another set
additional_set = {"soup", "bread"}

# Combining two sets (Union)
combined_set = food_set.union(additional_set)
print("Combined set:", combined_set)
