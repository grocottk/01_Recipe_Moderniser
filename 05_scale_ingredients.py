
# Recipe Moderniser Component 5
# Asks the user to enter their scale factor, and then asks for the units and amounts of each ingredient...
# ... in order to properly scale and convert the ingredients.

# To Do List on ePUB

# Functions:


# Number Checking Function


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

# Replace line below with Component 3 eventually

scale_factor = float(input("What is your scale factor? "))



# Set up empty ingredient list


ingredients = []

# Loop asking users to enter an ingredient

stop = ""
while stop != "xxx":

    amount = number_checker("What is the amount for the ingredient? ")
    scaled = amount * scale_factor

    # Check to see if exit code is typed...
    # ...and check that the list contains at lest two valid items.

    if amount.lower() == "xxx" and len(ingredients) > 1:
        break

    # If less than two ingredients are inserted into th list, show an error message

    elif amount.lower() == "xxx" and len(ingredients) < 2:
        print("You need at least two ingredients in the list. "
              "Please enter more ingredients. ")

    # If exit code is not entered, add ingredient to list

    else:

        # Ask user for ingredients (via blank checker)

        get_ingredient = not_blank("Please enter your ingredients, and type the code 'xxx' when finished: ",
                                   "Please enter an ingredient name (this cannot be blank)",
                                   "yes")

        ingredients.append(get_ingredient)

# Print List

print("Your ingredients are {}".format(ingredients))
