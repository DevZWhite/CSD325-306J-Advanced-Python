# Name: Zachary White
# Instructor: Darrell Payne
# Date: January 28, 2026
# Assignment: Miles to Kilometers Converter

# Purpose:
# This program converts a user-entered distance in miles to kilometers.
# It validates user input to ensure a numeric, non-negative value is entered
# before performing the conversion and displaying the results.

# Logic:
# 1. A function is defined to convert miles to kilometers using a fixed conversion rate.
# 2. The main function runs inside a loop to allow input validation.
# 3. The user is prompted to enter the number of miles driven.
# 4. A try/except block is used to catch non-numerical input.
# 5. If the input is negative, the user is prompted again.
# 6. Once valid input is received, the miles are converted to kilometers.
# 7. The program displays both the miles and the converted kilometers.


def miles_to_kilometers(miles):
    # Converts miles to kilometers.
    # Formula:
    # kilometers = miles * 1.60934
    return miles * 1.60934


def main():
    # Loop continues until valid input is entered
    while True:
        try:
            # Prompt the user for miles driven
            miles = float(input("Enter the number of miles driven: "))

            # Validate that the input is not negative
            if miles < 0:
                print("Miles cannot be negative. Please enter a valid number.")
                continue

            # Convert miles to kilometers using the function
            kilometers = miles_to_kilometers(miles)

            # Display the results
            print(f"\nMiles driven: {miles}")
            print(f"Kilometers driven: {kilometers:.2f}")

            # Exit the loop once valid input is processed
            break

        # Handle non-numeric input
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# Call the main function to start the program
main()
