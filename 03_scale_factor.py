
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

enter_scale_factor = "yes"
while enter_scale_factor == "yes":

    desired_size = number_checker("How many servings would you like to make? ")
    print()

    scale_factor = desired_size / current_size

    if scale_factor < 0.25:
        enter_scale_factor = input("Warning: This scale factor is very small, "
                                   "which might make it hard to measure accurately. \n"
                                   "You might want to make the original recipe and keep leftovers. \n"
                                   "Do you want to fix this and make more servings? ").lower()

    elif scale_factor > 4:
        enter_scale_factor = input("Warning: This scale factor is very large, "
                                   "which might not scale accurately to the average kitchen. \n"
                                   "You might want to make the original recipe in multiple batches. \n"
                                   "Do you want to fix this and make less servings? ").lower()

    else:
        enter_scale_factor = "no"

print()
print("The scale factor of this recipe is {:.2f}".format(scale_factor))
