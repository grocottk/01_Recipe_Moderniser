
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

else:

    print("Not Functional")
