# ============================================================
#  Zachary White
#  CSD 325 - Module 1 Assignment: Bottles of Beer
# ============================================================

def countdown(bottles):
    """Count backwards from the given number, displaying beer song lyrics."""
    for i in range(bottles, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            if i - 1 == 1:
                print(f"Take one down, pass it around, 1 bottle of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, {i - 1} bottles of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down, pass it around, no more bottles of beer on the wall.\n")


def main():
    print("=" * 60)
    print("       Welcome to the Bottles of Beer on the Wall!")
    print("=" * 60)

    while True:
        try:
            bottles = int(input("\nHow many bottles of beer are on the wall? "))
            if bottles <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print()
    countdown(bottles)

    print("=" * 60)
    print("  No more bottles of beer on the wall!")
    print("  Don't forget to go to the store and buy more beer!")
    print("=" * 60)


if __name__ == "__main__":
    main()