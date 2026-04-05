# ============================================================
# Name:        Zachary White
# Instructor:  Darrell Payne
# Date:        March 29, 2026
# Assignment:  Bottles of Beer on the Wall
# Purpose:
#   This program simulates the classic countdown song
#   "100 Bottles of Beer on the Wall." The user specifies
#   how many bottles to start with, and the program counts
#   down to zero while displaying the correct song lyrics
#   at each step.
#
#   Key behaviors:
#     1. Prompt the user for a starting bottle count.
#     2. Validate input to ensure only positive integers
#        are accepted.
#     3. Pass the validated count to a countdown function
#        that handles all lyric logic.
#     4. Correctly switch from plural ("bottles") to
#        singular ("bottle") when the count reaches 1.
#     5. Return to main() after the countdown and remind
#        the user to buy more beer.
#
# Logic:
#   1. Display a welcome message to the user.
#   2. Ask the user how many bottles are on the wall.
#   3. Validate: reject non-integers and numbers <= 0.
#   4. Call countdown() and pass the validated number.
#   5. Inside countdown(), loop from the starting number
#      down to 1:
#        - If count > 1, print plural lyrics.
#        - If count == 1, print singular lyrics.
#        - Subtract 1 from the count each iteration.
#   6. After the loop ends, return to main().
#   7. Print the closing reminder to buy more beer.
# ============================================================


def countdown(bottles):
    """
    Accepts an integer (bottles) and counts down to zero,
    printing the correct verse of the song at each step.
    Handles the switch from plural to singular at count == 1.
    """

    # Loop from the starting count down to 1 (inclusive)
    for i in range(bottles, 0, -1):

        if i > 1:
            # --- Plural verse (2 or more bottles remaining) ---

            # Print the first line of the verse using the current count
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")

            # Check what the NEXT count will be to set the correct wording
            if i - 1 == 1:
                # Next count is 1, so use singular in the second line
                print(f"Take one down, pass it around, "
                      f"1 bottle of beer on the wall.\n")
            else:
                # Next count is still plural (more than 1)
                print(f"Take one down, pass it around, "
                      f"{i - 1} bottles of beer on the wall.\n")

        else:
            # --- Singular verse (exactly 1 bottle remaining) ---

            # Print the singular form of the verse
            print("1 bottle of beer on the wall, 1 bottle of beer.")

            # Final line - no bottles left after this one
            print("Take one down, pass it around, "
                  "no more bottles of beer on the wall.\n")

    # The loop has finished - all bottles have been counted down


def main():
    """
    Entry point of the program. Displays a welcome message,
    collects and validates user input, calls the countdown
    function, then prints a closing reminder.
    """

    # Display a welcome banner to the user
    print("=" * 60)
    print("       Welcome to Bottles of Beer on the Wall!")
    print("=" * 60)

    # --- Input validation loop ---
    # Keep asking until the user provides a valid positive integer
    while True:
        try:
            # Prompt the user for the starting bottle count
            bottles = int(input("\nHow many bottles of beer are on the wall? "))

            # Reject zero and negative numbers
            if bottles <= 0:
                print("Please enter a number greater than 0.")
                continue  # Go back to the top of the loop

            # If we reach here, the input is valid - exit the loop
            break

        except ValueError:
            # Catches non-integer input (letters, decimals, symbols, etc.)
            print("Invalid input. Please enter a whole number.")

    # Print a blank line for readability before the song begins
    print()

    # --- Call the countdown function ---
    # Pass the validated bottle count to begin the song
    countdown(bottles)

    # --- Closing message ---
    # Displayed after countdown() returns to main()
    print("=" * 60)
    print("  No more bottles of beer on the wall!")
    print("  Don't forget to go to the store and buy more beer!")
    print("=" * 60)


# --- Program entry point ---
# Ensures main() only runs when this file is executed directly,
# not when it is imported as a module into another program
if __name__ == "__main__":
    main()