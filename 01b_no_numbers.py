
# Recipe Moderniser Component 1B
# A small component that checks if there are numbers in a recipe name

# Ask user for string

recipe_name = input("What is the name of your recipe? ")

error = "Sorry, but you must enter a string as your recipe name. You cannot have numbers in your recipe name."

has_errors = ""

# Look at each character in string, if any characters are numbers, give an error

for letter in recipe_name:
    if __name__ == '__main__':
        if letter.isdigit() == True:
            print(error)
            has_errors = "yes"
            break

    # Give user feedback..

        if has_errors != "Yes":
            print("This entry is valid")
