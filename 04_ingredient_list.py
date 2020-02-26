
# Recipe Moderniser Component 4
# Asks the user to enter the names of their ingredients, then inserts them into a list...
# ...and prints the list for the user.

# To Do List on ePUB

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

# Set up empty ingredient list


ingredients = []

# Loop asking users to enter an ingredient

stop = ""
while stop != "xxx":

    # Ask user for ingredients (via blank checker)

    get_ingredient = not_blank("Please enter your ingredients: ",
                               "The name can not be blank",
                               "yes")

    # Check to see if exit code is typed...
    # ...and check that the list contains at lest two valid items.

    if get_ingredient.lower() == "xxx" and len(ingredients) > 1:
        break

    elif get_ingredient.lower() == "xxx" and len(ingredients) < 2:
        print("You need at least two ingredinets in teh list. "
              "Please enter more ingredients. ")

    # If exit code is not entered, add ingredient to list

    else:
        ingredients.append(get_ingredient)

# Print List

print(ingredients)
