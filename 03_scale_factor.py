
# Recipe Moderniser Component 3
# Asks the uset the amount of servings that they currently make, the number of servings that they desire to make...
# ... and calculates the desired scale factor of their recipe. It also warns the user if their factor is outside limits.

# Functions:

# Number Checking Function

def number_checker(question):

    error = "Please enter a number that is more than zero."

    valid = False
    while not valid:

        try:
            response = float(input(question))

            if response <= 0:
                print(error)

            else:

                return response

        except ValueError:
            print(error)

# Main Routine:

current_size = number_checker("How many servings does the recipe currently make? ")
print()
desired_size = number_checker("How many servings would you like to make? ")
print()

scale_factor = desired_size / current_size

print("The scale factor of this recipe is {}".format(scale_factor))
