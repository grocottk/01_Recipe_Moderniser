
# Recipe Moderniser Assembled Outcome
# Assembles previously created Components into a large, Assembled Outcome, for testing purposes

import csv

# Functions:


# Blank Checking Function:

def not_blank(question, error_message, number_okay):

    error = error_message

# Beginning of Loop:

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        # Checks if the user has allowed numbers in their source

        if number_okay != "yes":

            # Look at each character in string, if any characters are numbers, give an error

            for letter in response:
                 if letter.isdigit():
                    has_errors = "yes"
                    break

        # If the response is blank, give an error message

        if response == "":
            print()
            print(error)
            print()
            continue

        # If the response contains errors (numbers etc.) give error

        elif has_errors != "":
            print()
            print(error)
            print()
            continue

        else:
            return response

# Main Routine:

# Asks the user for the name of the recipe, and checks to see if the recipe has numbers or is blank.

recipe_name = not_blank("Where is the name of your recipe? ",
                          "The recipe name cannot be blank, and cannot contain numbers.",
                          "no")

# Asks the user where the recipe is originally from
# (Defines the question, error message and whether numbers are allowed)

recipe_source = not_blank("Where is your recipe from? ",
                          "The recipe source cannot be blank, but may have numbers.",
                          "yes")
