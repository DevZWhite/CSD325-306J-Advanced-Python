"""Forest Fire Sim, modified for Module 6
A simulation of wildfires spreading in a forest.

Module 6 revisions:
- Added a lake near the center of the forest.
- Added WATER symbol using ~
- Display water in blue.
- Water cannot burn or be replaced.
- Water acts as a firebreak that flames cannot cross.
"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module.')
    print('Install it using: pip install bext')
    sys.exit()

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
                    continue

                if forest[(x, y)] == WATER:
                    nextForest[(x, y)] = WATER

                elif ((forest[(x, y)] == EMPTY)
                      and (random.random() <= GROW_CHANCE)):
                    nextForest[(x, y)] = TREE

                elif ((forest[(x, y)] == TREE)
                      and (random.random() <= FIRE_CHANCE)):
                    nextForest[(x, y)] = FIRE

                elif forest[(x, y)] == FIRE:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    nextForest[(x, y)] = EMPTY

                else:
                    nextForest[(x, y)] = forest[(x, y)]

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    forest = {'width': WIDTH, 'height': HEIGHT}

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if random.random() <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY

    # Add lake in center
    for x in range(WIDTH // 2 - 6, WIDTH // 2 + 6):
        for y in range(HEIGHT // 2 - 2, HEIGHT // 2 + 2):
            forest[(x, y)] = WATER

    return forest


def displayForest(forest):
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == WATER:
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
