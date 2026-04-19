"""
sitka_high_low_zw.py
Student : Zachary White
Instructor: Darrell Payne
Class   : CSD 325
Date    : 04/17/2026

Description:
    Reads Sitka, AK daily weather data from a CSV file and lets the user
    choose to display a graph of HIGH temperatures (red) or LOW temperatures
    (blue) for 2018.  The program loops until the user selects Exit.
    Based on the original sitka_highs.py provided in the course materials.

Changes from original sitka_highs.py:
    1. Added sys import for clean exit with sys.exit().
    2. Wrapped the entire program in a while-loop so the menu repeats.
    3. Added an opening banner / menu that shows options: Highs, Lows, Exit.
    4. Added input() call to read the user's menu choice.
    5. Added 'Lows' branch: plots TMIN column in blue with its own title.
    6. Added 'Exit' branch: prints a goodbye message and calls sys.exit().
    7. Added input validation so unrecognised choices print a helpful message
       and loop back to the menu without crashing.
    8. Moved CSV reading inside the loop so it runs fresh each iteration
       (keeps code simple and avoids stale data issues).
"""

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

# ── Constants ──────────────────────────────────────────────────────────────
FILENAME = r"C:\CSD\CSD325\module-4\sitka_weather_2018_simple.csv"

# ── Main loop ──────────────────────────────────────────────────────────────
print("=" * 50)
print("   Sitka, AK Weather Viewer - 2018")
print("=" * 50)

while True:
    # Display menu each iteration
    print("\nPlease select an option:")
    print("  H - Highs  : View daily HIGH temperatures")
    print("  L - Lows   : View daily LOW  temperatures")
    print("  E - Exit   : Quit the program")

    choice = input("\nEnter your choice (H / L / E): ").strip().upper()

    if choice == 'E':
        # ── Exit branch ────────────────────────────────────────────────
        print("\nThank you for using the Sitka Weather Viewer.  Goodbye!\n")
        sys.exit(0)

    elif choice in ('H', 'L'):
        # ── Read CSV data ──────────────────────────────────────────────
        dates  = []
        values = []

        try:
            with open(FILENAME) as f:
                reader = csv.reader(f)
                header_row = next(reader)          # skip header

                for row in reader:
                    current_date = datetime.strptime(row[2], '%Y-%m-%d')
                    dates.append(current_date)

                    if choice == 'H':
                        values.append(int(row[5]))  # TMAX column
                    else:
                        values.append(int(row[6]))  # TMIN column

        except FileNotFoundError:
            print(f"\nError: '{FILENAME}' not found.  "
                  "Make sure the CSV is in the same folder as this script.")
            continue

        # ── Plot ───────────────────────────────────────────────────────
        fig, ax = plt.subplots()

        if choice == 'H':
            ax.plot(dates, values, c='red')
            plt.title("Daily High Temperatures - Sitka 2018", fontsize=24)
        else:
            ax.plot(dates, values, c='blue')
            plt.title("Daily Low Temperatures - Sitka 2018", fontsize=24)

        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    else:
        # ── Invalid input ──────────────────────────────────────────────
        print(f"\n  '{choice}' is not a valid option.  "
              "Please enter H, L, or E.")
