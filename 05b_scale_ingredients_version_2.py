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

        response = input(question)

        # Check to see if exit code has been entered

        if response.lower() == "xxx":
            return "xxx"

        # if exit code not entered, check that input is a number

        else:

            try:

                response = float(response)
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
            print("\n {} \n".format(error))
            continue

        # If the response contains errors (numbers etc.) give error
        elif has_errors != "":
            print("\n {} \n".format(error))
            continue

        else:
            return response


# Main Routine:

# Replace line below with Component 3 eventually
scale_factor = eval(input("What is your scale factor? "))

# Set up empty ingredient list
ingredients = []

# Loop asking users to enter an ingredient

stop = ""
while stop != "xxx":

    amount = number_checker("What is the amount of your ingredient? Press 'xxx' to exit: ")

    # Check to see if exit code is typed...
    # ...and check that the list contains at lest two valid items.

    if amount == "xxx" and len(ingredients) > 1:
        break

    # If less than two ingredients are inserted into th list, show an error message

    elif amount == "xxx" and len(ingredients) < 2:
        print("You need at least two ingredients in the list. "
              "Please enter more ingredients. ")

    # If exit code is not entered, add ingredient to list

    else:

        # Ask user for ingredients (via blank checker)
        scaled = amount * scale_factor
        get_ingredient = not_blank("Please enter your ingredients: ",
                                   "Please enter an ingredient name (this cannot be blank)",
                                   "yes")

        amount = float(amount) * scale_factor

        # The following removes the decimal point for whole numbers:

        if amount % 1 == 0:
            amount = int(amount)

        # This code keeps decimal numbers to as few places as possible

        # This restricts the number tp 1 decimal place

        elif amount * 10 % 1 == 0:
            amount = "{:.1f}".format(amount)

        # This restricts the number to 2 decimal places

        else:

            amount = "{:.2f}".format(amount)


        ingredients.append("{} units {}".format(amount, get_ingredient))

# Print Lists

for item in ingredients:
    print(item)
