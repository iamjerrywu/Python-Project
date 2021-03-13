"""
File: cantor_set_drawing.py
Name:
-----------------------------------
This program draws as fractal named cantor set
on GWindow calling the recursive function cantor_set.
Students will learn another way of controlling
base case --  using a parameter 'level'
"""

from campy.graphics.gobjects import GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause

# Constants
SPACE = 40           # The space between levels
START_X = 50         # The starting x of the line
START_Y = 50         # The starting y of the line
START_WIDTH = 850    # The lenth of cantor set level 1
LEVEL = 5            # The level of the cantor set
DELAY = 100          # The pause time in miliseconds


# Global Variables
window = GWindow(width=1000, height=700)   # The canvas to draw lines on


def main():
	cantor_set(START_X, START_Y, START_WIDTH, LEVEL)


def cantor_set(x, y, width, level):
	pass

		


if __name__ == '__main__':
	main()