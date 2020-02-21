
# Recipe Moderniser Component 2
# Asks user for the servings that a recipe makes, and the servings that are desired to make

# Functions:


# Main Routine:

current_size = float(input("How many servings does the recipe currently make? "))
print()
desired_size = float(input("How many servings would you like to make? "))
print()

scale_factor = desired_size / current_size

print("Scale Factor: {}".format(scale_factor))
