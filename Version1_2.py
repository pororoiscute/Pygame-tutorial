# Program: Getting user input
# Author: Paul Min
# Date: 3 July 2024
# Version 1.2

# TODO: # Ask user for a number
        # Loop the question so that it repeats until a valid answer is given.
        # Makes the code recyclable.

# Test that a number is being entered (Version 1)
done = False # This is a boolean. Starts with a capital letter.
while not done:
    print("Please enter your value: ")
    try:
        num = int(input())          # Waiting for user input as an integer.
        if num > 0:
            done = True     # This breaks out of the loop is a valid input was given.
        else:
            print("Please enter a value more than zero.")

    except ValueError:
        print("That is not an integer.")
        continue


print(f"The number that you entered is {num}")

# Test that a number is being entered (Version 1.2)
# Create a function to call (use) every time I ask a user for an input.
def test_float_num(question): # test_float is the name of the function
                            # and 'question' is a placeholder.                       
    # Test that a number is being entered (Version 1)
    done = False # This is a boolean. Starts with a capital letter.
    while not done:
        print(question)
        try:
            num = float(input())
            if num > 0:
                done = True
            else:
                print("That is not an integer. ")
        except ValueError:
            print("That is not an integer")
    
    return(num)

# ------ Main Program ------
# Call the function in various quesitons
num1  = test_float_num("Please enter your value.")
print(f"Your first nr entered is {num1}.")
num2 = test_float_num("Please insert your second number:")
print(f"Your 2nd nr entered is {num2}.")
num3 = test_float_num("Please insert your third number:")
print(f"Your 3rd nr entered is {num3}.")
solution = num1 + num2 + num3
print(f"Your numbers added up are equal to: {solution}.")'''