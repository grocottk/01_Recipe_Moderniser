
# Recipe Moderniser Component 1
# Asks user for the name of their recipe, and checks that it is not blank and does not have numbers.

# Blank Checking Function:

def not_blank(question):

    error = "Sorry, but you must enter a string as your recipe name. You cannot have numbers in your recipe name."

    has_errors = ""

    valid = False
    while not valid:
        response = input(question)

        # Look at each character in string, if any characters are numbers, give an error

        for letter in response:
            if __name__ == '__main__':
                if letter.isdigit() == True:
                    has_errors = "yes"
                    break

        if response == "":
            print()
            continue

        elif has_errors != "":
            print(error)
            continue

        else:
            return response

        return response



# Main Routine:

recipe_name = not_blank("What is the name of your recipe? ")

print("You are making {}".format(recipe_name))
