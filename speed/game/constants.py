"""Contains constants used throughout the game.
"""

import os

MAX_X = 60
MAX_Y = 20
FPS = 10
# Calculated from FPS
FRAME_LENGTH = 1 / FPS
STARTING_WORDS = 5
PATH = os.path.dirname(os.path.abspath(__file__))
LIBRARY = PATH + '/words.txt'
BACKGROUND = ' '
