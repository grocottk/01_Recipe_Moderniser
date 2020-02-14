
# Recipe Moderniser Component 1
# Asks user for the name of their recipe, and checks that it is not blank and does not have numbers.

# Blank Checking Function:

def not_blank(question):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            continue
        else:
            return response

        return response

# Main Routine:

recipe_name = not_blank("What is the name of your recipe? ")

print("You are making {}".format(recipe_name))

