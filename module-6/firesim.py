"""
Student Group D : Zachary White  Jeff Victorino  Kris Kleiner  Sean Summers
Instructor      : Darrell Payne
Class           : CSD 325
Date            : 04/22/2026
Description:
    A terminal-based simulation of wildfires spreading through a forest.
    Trees (A) grow randomly, catch fire (@) by chance or from neighbors,
    and burn out leaving empty space.  A permanent lake (~) is placed near
    the center of the display in blue; water cannot burn or be overwritten
    and acts as a natural firebreak that flames cannot cross.
    Requires the third-party 'bext' module for colored terminal output.
Changes from original forestfiresim.py:
    1. Added WATER = '~' constant to represent water/lake cells.
    2. Added lake creation in createNewForest(): a rectangular block of
       WATER cells is placed roughly in the center of the grid.
    3. Added water-preservation rule in the main loop: WATER cells are
       always copied unchanged to nextForest, making them permanent.
    4. Fire spread logic only ignites TREE neighbors, so water cells are
       naturally immune and act as a firebreak.
    5. Added blue color output for WATER cells in displayForest().
"""
import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module.')
    print('Install it using: pip install bext')
    sys.exit()

# Constants
WIDTH = 79
HEIGHT = 22
TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'

INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:
        displayForest(forest)

        nextForest = {'width': forest['width'], 'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    continue  # Already set, skip

                if forest[(x, y)] == WATER:
                    # Water is permanent — cannot be changed
                    nextForest[(x, y)] = WATER

                elif (forest[(x, y)] == EMPTY) \
                    and (random.random() <= GROW_CHANCE):
                    # Empty cell randomly grows a tree
                    nextForest[(x, y)] = TREE

                elif (forest[(x, y)] == TREE) \
                    and (random.random() <= FIRE_CHANCE):
                    # Tree randomly catches fire (lightning strike)
                    nextForest[(x, y)] = FIRE

                elif forest[(x, y)] == FIRE:
                    # Fire spreads to neighboring trees (but NOT water)
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            neighbor = forest.get((x + ix, y + iy))
                            if neighbor == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # The burning cell becomes empty after it burns out
                    nextForest[(x, y)] = EMPTY

                else:
                    # No change — copy cell as-is
                    nextForest[(x, y)] = forest[(x, y)]

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Create a new forest dictionary with trees, empty spaces, and a central lake."""
    forest = {'width': WIDTH, 'height': HEIGHT}

    # Populate with trees and empty cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if random.random() <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY

    # Add lake roughly in the center of the display
    # Lake spans ~12 columns wide and ~8 rows tall
    for x in range(WIDTH // 2 - 6, WIDTH // 2 + 6):
        for y in range(HEIGHT // 2 - 4, HEIGHT // 2 + 8):
            forest[(x, y)] = WATER

    return forest


def displayForest(forest):
    """Render the forest to the terminal with color-coded symbols."""
    bext.goto(0, 0)

    for y in range(forest['height']):
        for x in range(forest['width']):
            cell = forest[(x, y)]
            if cell == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif cell == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif cell == WATER:
                bext.fg('blue')
                print(WATER, end='')
            else:
                print(EMPTY, end='')
        print()

    bext.fg('reset')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()