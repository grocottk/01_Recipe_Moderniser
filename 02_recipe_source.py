
# Recipe Moderniser Component 2
# Asks user for the source of their recipe (in the form of a link), and checks that it is not blank

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

# Defines the question, error message and whether numbers are allowed

recipe_source = not_blank("Where is your recipe from? ",
                          "The recipe source cannot be blank, but may have numbers.",
                          "yes")

# Prints the source of the recipe

print()
print("The recipe is from {}".format(recipe_source))
