
# Recipe Moderniser Component 2
# Asks user for the servings that a recipe makes, and the servings that are desired to make

# Functions:

# Number Checking Function

def number_checker(question):

    error = "You cannot enter a number that is zero or less. Please try again"

    valid = False
    while not valid:
        try:
            response = float(input(question))

        except ValueError:
            print(error)

# Main Routine:

current_size = float(number_checker("How many servings does the recipe currently make? "))
print()
desired_size = float(number_checker("How many servings would you like to make? "))
print()

scale_factor = desired_size / current_size

print("Scale Factor: {}".format(scale_factor))
