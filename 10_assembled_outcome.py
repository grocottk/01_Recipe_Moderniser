
# Recipe Moderniser Assembled Outcome
# Assembles previously created Components into a large, Assembled Outcome, for testing purposes

# Modules:

# Comma Separated Variables

import csv

# Regular Expressions

import re

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

# Number Checking Function:


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

# Getting Scale Factor Function


def get_scale_factor():

    current_size = number_checker("How many servings does the recipe currently make? ")
    print()

    # Main Routine Goes Here

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

    return scale_factor

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

# Get serving sizes and Scale Factor:

scale_factor = get_scale_factor()

# Prints Scale Factor

print(scale_factor)
