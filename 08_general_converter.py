
# Recipe Moderniser Component 8
# Uses a function to convert units more efficiently in general

# To Do List on ePUB

# Functions:


# General Dictionary Checking Function

# Checks if the unit is in the dictionary

def general_converter(how_much, lookup, dictionary, conversion_factor):

    if lookup in dictionary:

        multiply_by = dictionary.get(unit)
        how_much = how_much * multiply_by * conversion_factor
        print("Amount in milliliters: {}".format(how_much))

    return how_much

# Unit Checking Function


def unit_checker():

    unit_to_check = input("What is your unit? ")

    # Abbreviation Lists for various measurements

    teaspoon = ["tsp", "teaspoon", "t"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp"]
    ounce = ["oz", "fluid ounce", "fl oz"]
    cup = ["c", "cups"]
    pint = ["p", "pt", "fl pt"]
    quart = ["q", "qt", "fl qt"]
    milliliter = ["millilitre", "ml", "cc", "mL"]
    liter = ["l", "litre", "L"]
    deciliter = ["dl", "decilitre", "dL"]
    pound = ["lb", "lbs", "#"]
    stick = ["knob"]

    if unit_to_check == "":

        print("You choose {}".format(unit_to_check))
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

# Loop Begins

keep_going = ""
while keep_going == "":

    # Evaluates how much/unit of ingredient (allows for equations to be done in converter,
    # however does not allow fractions)

    amount = eval(input("How much? "))
    amount = float(amount)

    # Gets unit an changes it to match the dictionary

    unit = unit_checker()

    # Calls General Converter Function

    amount = general_converter(amount, unit, unit_dictionary, 1)

# Loop Ends

keep_going = input("Press enter to continue, or 'x' to quit")
