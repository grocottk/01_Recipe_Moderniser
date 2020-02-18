
# Recipe Moderniser Component 2
# Asks user for the source of their recipe (in the form of a link), and checks that it is not blank

# Blank Checking Function:


def not_blank(question, error_message, number_okay):

    error = error_message

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if number_okay != "yes":

            # Look at each character in string, if any characters are numbers, give an error

            for letter in response:
                if __name__ == '__main__':
                    if letter.isdigit():
                        has_errors = "yes"
                        break

        if response == "":
            print()
            print("Sorry, but you must enter something as your recipe name. You cannot leave this blank.")
            print()
            continue

        elif has_errors != "":
            print()
            print(error)
            print()
            continue

        else:
            return response

# Main Routine:

recipe_source = not_blank("Where us the recipe from? ", "The recipe source cannot be blank,", "Yes")

print()
print("You are making {}".format(recipe_source))
