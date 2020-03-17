
# Recipe Moderniser Component 8b
# Combines Component 8 with Component 7 in order to implement the code into the Assembled Outcome more efficiently

# To Do List on ePUB

# Imports:

import csv

# Functions:


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

    if unit_to_check == "":

        # print("You choose {}".format(unit_to_check))
        return unit_to_check

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

# Prints the dictionary as a whole (Useful for testing, but ultimately removed)

# print(food_dictionary)

# Main Routine

# Loop Begins

keep_going = ""
while keep_going == "":

    # Evaluates how much/unit of ingredient (allows for equations to be done in converter,
    # however does not allow fractions)

    amount = eval(input("How much? "))
    amount = float(amount)

    # Gets unit an changes it to match the dictionary

    unit = unit_checker()

    # Gets an ingredient and changes it to be lowercase to match the dictionary

    ingredient = input("Please enter your ingredient: ").lower()

    # Converts item to milliliters if possible

    amount = general_converter(amount, unit, unit_dictionary, 1)

    print(amount)

    # If we converted to milliliters

    if amount[1] == "yes":

        amount_2 = general_converter(amount[0], ingredient, food_dictionary, 250)

        # If the ingredient is in the list, convert it

        if amount_2[1] == "yes":

            print(amount_2)

        # If the ingredient is not in the list, leave it as milliliters

        else:

            print("unchanged")

    # if the main unit is not in milliliters, leave the unit as milliliters

    else:

        print("unchanged")

    # keep_going = input("enter or q")
