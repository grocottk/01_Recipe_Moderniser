
# Recipe Moderniser Component 9
# Improves the experience of inserting information on the recipe into the program.

import re

# Ingredient has a mixed fraction followed by a unit and ingredient
# (Change below into input statement at a later date)

recipe_line = "1 1/2 ml flour"

mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

# If the regular expression is functional, then print "Functional", if not, print "Not Functional"

if re.match(mixed_regex, recipe_line):

    print("Functional")

    # Get mixed number by matching the regular expression

    pre_mixed_number = re.match(mixed_regex, recipe_line)

    # Using the group method to isolare the number

    mixed_number = pre_mixed_number.group()

    # Replace the space with a 'plus' sign:

    amount = mixed_number.replace(" ", "+")

    # Change the above string into a decimal:

    amount = eval(amount)

    print(amount)

    # Get Unit and ingredient:

    compile_regex = re.compile(mixed_regex)

    # Prints the compiled Regular Expression

    print(compile_regex)

    # Inserts data gained so far into a list

    unit_ingredient = re.split(compile_regex, recipe_line)

    # Removes the extra whitespace (spaces) from a unit

    unit_ingredient = (unit_ingredient[1]).strip()

    # Prints the list

    print(unit_ingredient)

# Splits the text at the first space

get_unit = unit_ingredient.split(" ", 1)

# Prints the list, with no whitespace

print(get_unit)

# Sets the Unit to the first item in the list

unit = get_unit[0]

# Sets the Ingredient to the second item in the list

ingredient = get_unit[1]

# Prints the Unit

print(unit)

# Prints the Ingredient

print(ingredient)
