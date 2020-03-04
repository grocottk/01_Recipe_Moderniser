
# Recipe Moderniser Component 6
# Asks the user to enter their units, and then converts to millileters or grams if applicable.

# To Do List on ePUB

# If no unit is given / unit is unknown, leave as is.

# Buioling list of milliliter unit conversions

unit_dictionary = {
    "tsp": 5,
    "tbs": 15,
    "cup": 240,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "stick": 113,
}

# Evaluates how much/unit of ingredient

amount = eval(input("How much? "))
amount = float(amount)

unit = input("Unit? ")

# Checks if the unit is in the unit dictionary

if unit in unit_dictionary:

    multiply_by = unit_dictionary.get(unit)
    amount = amount * multiply_by
    print("Amount in milliliters: {}".format(amount))

# If the unit is not in the unit dictionary, the unit is unchanged

else:

    print("{} is unchanged".format(amount))

