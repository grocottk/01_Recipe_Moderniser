
# Recipe Moderniser Component 7
# Uses a dictionary to convert ingredients' measurements form milliliters to grams

# To Do List on ePUB

# Importing Dictionary (from a csv file)

import csv

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

    # Gets an ingredient and changes it to be lowercase to match the dictionary

    ingredient = input("Please enter your ingredient: ").lower()

    # Checks if the unit is in the food dictionary

    if ingredient in food_dictionary:

        multiply_by = food_dictionary.get(ingredient)
        amount = amount * float(multiply_by) / 250

        # Prints the amount in grams if the ingredient is in the dictionary

        print("Amount in grams: {}".format(amount))

    # If the unit is not in the unit dictionary, the unit is unchanged

    else:

        print("{} is unchanged".format(amount))
