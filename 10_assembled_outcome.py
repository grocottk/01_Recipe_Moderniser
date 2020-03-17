
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
# (Makes sure that the number is a 'float' that is more than zero (0))


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
    sf = ""

    # Main Routine Goes Here

    enter_scale_factor = "yes"
    while enter_scale_factor == "yes":

        desired_size = number_checker("How many servings would you like to make? ")
        print()

        sf = desired_size / current_size

        # If the scale factor is less than 0.25, warn the user

        if sf < 0.25:
            enter_scale_factor = input("Warning: This scale factor is very small, "
                                       "which might make it hard to measure accurately. \n"
                                       "You might want to make the original recipe and keep leftovers. \n"
                                       "Do you want to fix this and make more servings? ").lower()

        # If the scale factor is more than 4, warn the user

        elif sf > 4:
            enter_scale_factor = input("Warning: This scale factor is very large, "
                                       "which might not scale accurately to the average kitchen. \n"
                                       "You might want to make the original recipe in multiple batches. \n"
                                       "Do you want to fix this and make less servings? ").lower()

        # If none of these are the case, return the scale factor

        else:
            enter_scale_factor = "no"

    return sf


# General Dictionary Checking Function

# Checks if the unit is in the dictionary

def general_converter(how_much, lookup, dictionary, conversion_factor):

    if lookup in dictionary:

        multiply_by = dictionary.get(lookup)
        how_much = how_much * float(multiply_by) / conversion_factor
        # print("Amount in milliliters: {}".format(how_much))

        converted = "yes"

    else:

        converted = "no"

    return [how_much, converted]

# Unit Checking Function


def unit_checker():

    unit_to_check = input("What is your unit? ")

    # Abbreviation Lists for various measurements

    teaspoon = ["tsp", "teaspoon", "t", "teaspoons"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp", "tablespoons"]
    ounce = ["oz", "fluid ounce", "fl oz", "fluid ounces"]
    cup = ["c", "cups", "cup"]
    pint = ["p", "pt", "fl pt", "pint", "pints"]
    quart = ["q", "qt", "fl qt", "quart", "quarts"]
    milliliter = ["millilitre", "ml", "cc", "mL", "milliliter", "milliliters", "millilitres"]
    liter = ["l", "litre", "L", "litres", "liters", "liter"]
    deciliter = ["dl", "decilitre", "dL", "decilitres"]
    pound = ["lb", "lbs", "#", "pound", "pounds"]
    stick = ["knob"]
    grams = ["g", "gram", "grams"]

    if unit_to_check == "":

        # print("You choose {}".format(unit_to_check))
        return unit_to_check

    elif unit_to_check.lower() in grams:

        return "g"

    elif unit_to_check == "T" or unit_to_check.lower() in tablespoon:

        return "tbs"

    elif unit_to_check.lower() in teaspoon:

        return "tsp"

    elif unit_to_check.lower() in ounce:

        return "ounce"

    elif unit_to_check.lower() in cup:

        return "cup"

    elif unit_to_check.lower() in pint:

        return "pint"

    elif unit_to_check.lower() in quart:

        return "quart"

    elif unit_to_check.lower() in milliliter:

        return "milliliter"

    elif unit_to_check.lower() in liter:

        return "liter"

    elif unit_to_check.lower() in deciliter:

        return "deciliter"

    elif unit_to_check.lower() in pound:

        return "pound"

    elif unit_to_check.lower() in stick:

        return "stick"

# Main Routine

# Building list of milliliter unit conversions


unit_dictionary = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "stick": 113,
    "liter": 1000,
    "milliliter": 1,
    "deciliter": 100,
}

# Food Dictionary:


# Opens the Dictionary File

groceries = open('01_ingredients_ml_to_g.csv')

# Insert data into a list

csv_groceries = csv.reader(groceries)

# Create a dictionary to hold the data

food_dictionary = {}

# Add the data from the list (from the csv file) into the dictionary
# Note: The first item in a row is the ingredient, while the next is the amount of the ingredient in grams

for row in csv_groceries:

    food_dictionary[row[0]] = row[1]

# print(food_dictionary)

# Prints the dictionary as a whole (Useful for testing, but ultimately removed)

# print(food_dictionary)

# Ingredient Getting Function:
# (Function also checks the amount, units and ingredients to see if they are valid)


def get_all_ingredients():

    # Creates an empty list to eventually contain ingredients

    all_ingredients = []

    stop = ""

    # Tells users information at the beginning of the loop

    print("Please enter ingredients one at a time, and enter 'xxx' when you have finished entering ingredients ")

    # Loop asking users to enter an ingredient

    while stop != "xxx":

        # Ask user for ingredients (via blank checker)

        get_ingredient = not_blank("Recipe Line: ",
                                   "This can't be blank",
                                   "yes")

        # Check to see if exit code is typed...
        # ...and check that the list contains at lest two valid items.

        if get_ingredient.lower() == "xxx" and len(all_ingredients) > 1:
            break

        # If less than two ingredients are inserted into th list, show an error message

        elif get_ingredient.lower() == "xxx" and len(all_ingredients) < 2:
            print("You need at least two ingredients in the list. "
                  "Please enter more ingredients. ")

        # If exit code is not entered, add ingredient to list

        else:
            all_ingredients.append(get_ingredient)

    return all_ingredients

# Main Routine:


# Set up a list to hold converted recipe
modernised_recipe = []

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

# Get amounts, units and ingredients from the user:

full_recipe = get_all_ingredients()

# Split each line of the recipe into amount, unit and ingredient...

# The regular expression that is used in splitting

mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

# The 'for' loop that allows for constant input

for recipe_line in full_recipe:

    # Strips whitespace from the inputted recipe

    recipe_line = recipe_line.strip()

    # Checks to see if the regular expression is functional

    if re.match(mixed_regex, recipe_line):

        # Get mixed number by matching the regular expression
        pre_mixed_number = re.match(mixed_regex, recipe_line)

        # Using the group method to isolate the number
        mixed_number = pre_mixed_number.group()

        # Replace the space with a 'plus' sign:
        amount = mixed_number.replace(" ", "+")

        # Change the above string into a decimal:
        amount = eval(amount)

        # Applies Scale Factor to Decimals
        amount = amount * scale_factor

        # Get Unit and ingredient:
        compile_regex = re.compile(mixed_regex)

        # Inserts data gained so far into a list
        unit_ingredient = re.split(compile_regex, recipe_line)

        # Removes the extra whitespace (spaces) from a unit
        unit_ingredient = (unit_ingredient[1]).strip()

    else:

        # Splits the code at the first 'space'

        get_amount = recipe_line.split(" ", 1)

        try:

            # Converts the amount to a 'float' if possible

            amount = eval(get_amount[0])

            amount = amount * scale_factor

        except NameError:

            # When no number is present:

            amount = get_amount[0]

            # Adds the recipe line into the modernised recipe

            modernised_recipe.append(recipe_line)
            continue

        # Combines Unit and ingredient together

        unit_ingredient = get_amount[1]

    # Getting the unit and ingredient:

    # Splits the text at the first space
    get_unit = unit_ingredient.split(" ", 1)

    # Sets the Unit to the first item in the list
    # (Converts the unit into milliliters)

    unit = get_unit[0]

    # Adapts to number of spaces used in recipe line

    unit = get_unit[0]

    num_spaces = recipe_line.count(" ")

    if num_spaces > 1:

        # Sets the Ingredient to the second item in the list
        # (Converts the ingredient into grams)

        ingredient = get_unit[1]

    else:

        modernised_recipe.append("{} {} {}".format(amount, unit, unit_ingredient))
        continue

    # Formats the list in the amount, unit and ingredient format

    modernised_recipe.append("{} {} {}".format(amount, unit, ingredient))

# For every item in the list, print the item

for item in modernised_recipe:

    print(item)
