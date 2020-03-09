
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

# Prints the dictionary as a whole

print(food_dictionary)
